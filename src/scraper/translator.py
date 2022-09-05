import json

import goslate

from base_logger import lg
from config import SCRAPER_TRANSLATION_OUTPUT_DIRECTORY, ERROR_TRANSLATION_FAILED
from utils import get_latest_raw_result_filepath


def read():
    with open(get_latest_raw_result_filepath()) as f:
        lines = f.readlines()

    lg.info(f"Found {len(lines)} datapoints")
    return lines

def transform(input_data):
    transformed_data = []
    gs = goslate.Goslate()

    dest_languages = ['en', 'sv']
    progress = 0
    final = len(input_data) * len(dest_languages)
    for line in input_data:
        lg.info(f"{progress} / {final}")
        json_line = json.loads(line)
        scraped_content = json_line['scraped_content']
        for language in dest_languages:
            try:
                progress +=1
                translation = gs.translate(scraped_content, language)
            except Exception as e:
                lg.warning(f"Error {e}")
                translation = ERROR_TRANSLATION_FAILED
                #TODO add enumeration of progress to logging

            translated_object = {
                "scraped_date": json_line['scraped_date'],
                "scraped_timestamp": json_line['scraped_timestamp'],
                "url": json_line['url'],
                "language": language,
                "translation": translation,
            }

            transformed_data.append(translated_object)

    lg.info(f"Generated {len(transformed_data)} translations")
    return transformed_data

def write(transformed_data):
    scraper_translation_output_file = get_latest_raw_result_filepath().split(sep='/')[-1]
    with open(SCRAPER_TRANSLATION_OUTPUT_DIRECTORY + scraper_translation_output_file, "a+") as outfile:
        for line in transformed_data:
            json.dump(line, outfile)
            outfile.write('\n')



def main():
    input_data = read()
    transformed_input_data = transform(input_data)
    write(transformed_input_data)

def test():
    lg.getLogger().setLevel(lg.DEBUG)
    input_data = [read()[0]]
    transformed = transform(input_data)
    write(transformed)

if __name__ == "__main__":
    test()
else:
    main()