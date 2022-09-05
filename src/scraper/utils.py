import glob
import os

from base_logger import lg
from config import SCRAPER_OUTPUT_DIRECTORY
from config import SCRAPER_TRANSLATION_OUTPUT_DIRECTORY


def get_latest_raw_result_filepath():
    lg.debug(f"Checking {SCRAPER_OUTPUT_DIRECTORY}" + "*")
    result_files = glob.glob(SCRAPER_OUTPUT_DIRECTORY + '*')
    latest_result = max(result_files, key=os.path.getctime)
    lg.info(f"Returning {latest_result}")
    return latest_result

def get_all_filenames_in_directory_without_extensions(directory):
    lg.debug(f"Checking {directory}" + "*")
    result_filepaths = glob.glob(directory + '*')
    result_filenames = [r.split(sep='/')[-1] for r in result_filepaths]
    result_filenames = [r.split(sep='.')[0] for r in result_filenames]
    lg.debug(f"Returning {len(result_filenames)}, for example {result_filenames[:10]}")
    return result_filenames


def get_latest_translated_result_filepath():
    lg.debug(f"Checking {SCRAPER_TRANSLATION_OUTPUT_DIRECTORY}" + '*')
    result_files = glob.glob(SCRAPER_TRANSLATION_OUTPUT_DIRECTORY + '*')
    latest_result = max(result_files, key=os.path.getctime)
    lg.info(f"Returning {latest_result}")
    return latest_result

def test():
    lg.getLogger().setLevel(lg.DEBUG)
    get_latest_raw_result_filepath()
    get_latest_translated_result_filepath()
    get_all_filenames_in_directory_without_extensions(SCRAPER_OUTPUT_DIRECTORY)
    get_all_filenames_in_directory_without_extensions(SCRAPER_TRANSLATION_OUTPUT_DIRECTORY)

if __name__ == "__main__":
    test()