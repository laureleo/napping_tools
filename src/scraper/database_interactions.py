import pandas as pd
import psycopg2
from sqlalchemy import create_engine

from base_logger import lg
from config import SCRAPER_OUTPUT_DIRECTORY
from config import SCRAPER_TRANSLATION_OUTPUT_DIRECTORY
from utils import get_all_filenames_in_directory_without_extensions

"""
Install the graphical client
"""
DATABASE_TYPE = 'postgresql'
DRIVER_TYPE = '+psycopg2'
DB_PROD_NAME = 'tiny_db_production'
DB_OWNER_NAME = 'tiny_db_owner'
DB_OWNER_PWD = 'tiny_db_pwd'
SCHEMA_NAME = 'world_news_explorer'
RAW_NEWS_TABLE_NAME = 'raw_news'
TRANSLATED_NEWS_TABLE_NAME = 'translated_news'
PORT = 5433
HOST = 'localhost'

def build_database():
    conn = psycopg2.connect(
        database="victor.wiklund", user='victor.wiklund', password='', host=HOST, port=PORT
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cmds = [f"create database {DB_PROD_NAME}",
    f"create role {DB_OWNER_NAME} with login password '{DB_OWNER_PWD}'",
    f"grant all privileges on database {DB_PROD_NAME} to {DB_OWNER_NAME}"
            ]
    for cmd in cmds:
        try:
            cursor.execute(cmd)
        except Exception as e:
            lg.warning(e)
    conn.close()

def execute_sql(commands, return_data = False):
    """
    :param commands: A list of sql query strings
    :param return_data: If True, fetches the result from the last query executed. Useful for select statements

    :return result: The result of the last query executed,
    """
    conn = psycopg2.connect(
        database=f"{DB_PROD_NAME}", user=f'{DB_OWNER_NAME}', password={DB_OWNER_PWD}, host=HOST, port= PORT
    )
    conn.autocommit = True
    cursor = conn.cursor()

    for cmd in commands:
        try:
            lg.info(f"Executing {cmd}")
            cursor.execute(cmd)
        except Exception as e:
            lg.warning(e)


    if return_data == True:
        return cursor.fetchall()

    conn.close()

#TODO make it generated the sql for creating the table by reading the file
commands = [
    f"create schema if not exists {SCHEMA_NAME}",
    f""" create table if not exists {SCHEMA_NAME}.{RAW_NEWS_TABLE_NAME}(
            constraint pk_raw_news primary key (scraped_date, url),
            scraped_date varchar(255),
            scraped_timestamp varchar(255),
            url varchar(255),
            scraped_content varchar(10000),
            country varchar(255),
            newspaper varchar(255),
            error varchar(255)
            )
    """,
    f"""create table if not exists {SCHEMA_NAME}.{TRANSLATED_NEWS_TABLE_NAME}(
            constraint pk_raw_translated_news primary key (scraped_date, url, language),
            constraint fk_raw_news foreign key(scraped_date, url) references {SCHEMA_NAME}.{RAW_NEWS_TABLE_NAME}(scraped_date, url),
            scraped_date varchar(255),
            scraped_timestamp varchar(255),
            url varchar(255),
            translation varchar(10000),
            language varchar(255),
            error varchar(255)
            );
        """,
]

def upload_json_into_database(source_directory, dest_schema, dest_table, primary_key, dates = []):
    """
    :param date a list of dates (in string format) to load into the database
    :param source_directory, which directory to look for files in
    :param primary_key: A list of column names. These are used to drop any duplicate entries,

    example: upload_json_into_database(SCRAPER_OUTPUT_DIRECTORY, SCRAPER_DEST_TABLE, [date, url], [2022-01-01, 2022-03-09])

    """
    engine = create_engine(f'{DATABASE_TYPE}{DRIVER_TYPE}://{DB_OWNER_NAME}:{DB_OWNER_PWD}@{HOST}:{PORT}/{DB_PROD_NAME}')

    if len(dates) == 0:
        lg.info("No date argument given. Beginning automatic inference")
        dates_in_db = execute_sql([f"select distinct scraped_date from {dest_schema}.{dest_table}"], return_data=True)
        dates_in_db = [d[0]for d in dates_in_db]
        dates_in_raw = get_all_filenames_in_directory_without_extensions(source_directory)

        dates = [d for d in dates_in_raw if d not in dates_in_db]
        lg.info(f"Found the following dates in the raw scraper folder not present in the database {dates}")

    if len(dates) == 0:
        lg.info("No valid dates found. Exiting")
    else:
        for d in dates:
            lg.info(f"Attempting to upload data for day {d} into database from {source_directory}")
            try:
                filepath = source_directory + d + '.json'
                df = pd.read_json(filepath, lines=True)
                df = df.drop_duplicates(subset=primary_key)
                df.to_sql(dest_table, schema=SCHEMA_NAME, con = engine, index=False, if_exists='append',chunksize=10, method='multi')
                lg.info("Success :)")
            except Exception as e:
                lg.warning(e)

def setup ():
    build_database()
    execute_sql(commands)

def test():
    lg.getLogger().setLevel(lg.DEBUG)

    test_date = '9999-09-09'
    test_url = 'test_url'
    test_language = 'en'

    lg.debug("Test 1 Data upsert")
    sql = [f"insert into {SCHEMA_NAME}.{RAW_NEWS_TABLE_NAME} (scraped_date, url) values ('{test_date}', '{test_url}')",
           f"insert into {SCHEMA_NAME}.{TRANSLATED_NEWS_TABLE_NAME} (scraped_date, url, language) values ('{test_date}', '{test_url}', '{test_language}')"
           ]
    execute_sql(sql)

    lg.debug("Test 2: Data retrieval")
    result = execute_sql([f"select * from {SCHEMA_NAME}.{RAW_NEWS_TABLE_NAME} order by scraped_date desc limit 5"], return_data=True)
    for r in result:
        lg.debug(str(r))

    result = execute_sql([f"select * from {SCHEMA_NAME}.{TRANSLATED_NEWS_TABLE_NAME} order by scraped_date desc limit 5"], return_data=True)
    for r in result:
        lg.debug(str(r))

    lg.debug("Cleaning up")
    sql = [f"delete from {SCHEMA_NAME}.{TRANSLATED_NEWS_TABLE_NAME} where scraped_date = '{test_date}' and url = '{test_url}' and language = '{test_language}'",
           f"delete from {SCHEMA_NAME}.{RAW_NEWS_TABLE_NAME} where scraped_date =  '{test_date}' and url = '{test_url}'"
           ]

    execute_sql(sql)




def upload_into_translated_news():
    upload_json_into_database(
        source_directory = SCRAPER_TRANSLATION_OUTPUT_DIRECTORY,
        dest_schema = SCHEMA_NAME,
        dest_table= TRANSLATED_NEWS_TABLE_NAME,
        primary_key=['scraped_date', 'url', 'language'],
    )

def upload_into_raw_news():
    upload_json_into_database(
        source_directory= SCRAPER_OUTPUT_DIRECTORY,
        dest_schema = SCHEMA_NAME,
        dest_table= RAW_NEWS_TABLE_NAME,
        primary_key=['scraped_date', 'url'],
    )

if __name__ == "__main__":
    setup()
    test()
    upload_into_translated_news()
