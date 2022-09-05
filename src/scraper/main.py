import argparse

from base_logger import lg
from config import websites_to_scrape
from scraper import NewsScraper


def scrape_single_website(newspaper_name, website_configs):
    website_parameters = website_configs[newspaper_name]

    ns = NewsScraper(
        url = website_parameters['url'],
        xpath = website_parameters['xpath'],
        country = website_parameters['country'],
        newspaper = website_parameters['newspaper'],
    )
    ns.run_and_write()

def scrape_all_websites(websites_to_scrape):
    for ws in websites_to_scrape:
        scrape_single_website(ws, websites_to_scrape)


def setup_argument_parser():
    # Define the parser and default arguments
    parser = argparse.ArgumentParser(description='A program that scrapes news from websites')
    parser.add_argument("--xpath",
                        help="If set, tries to scrape content at specified xpath",
                        default='//*')
    parser.add_argument("-n", "--newspaper",
                        help="If set, tries to find the website configuration in the config file and attempts the scrape")

    parser.add_argument("-d", "--debug",
                        action='store_true',
                        help="If set, print additional debug info")
    return parser

parser = setup_argument_parser()
args = vars(parser.parse_args())
if args['debug']:
    lg.getLogger().setLevel(lg.DEBUG)
elif args['newspaper']:
    scrape_single_website(newspaper_name=args['newspaper'], website_configs=websites_to_scrape)
else:
    scrape_all_websites(websites_to_scrape)