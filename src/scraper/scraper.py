import json
import re

import lxml.html
import requests as r

# TODO: Relative imports might be a bad idea
from base_logger import lg
from config import SCRAPER_OUTPUT_FILE
from config import TIMESTAMP
from config import TODAY


class NewsScraper:
    """
    :param
    url: String
        The site to extract data from
    xpath: String
        Path to the xml element(s) to extract
    country : String
        Country for the website

    Given a url, extracts the html response,
    parses it as a xml tree,
    then uses the given xml path to extact an element,
    converting it to text.

    :return
    A json object containing
    url, scraped_content, scraped_date, country

    Initial website list based on https://www.nationsonline.org/oneworld/news.html


    """
    def __init__(self,
                 url,
                 xpath='//div',
                 country='Unknown',
                 newspaper = 'Unknown'):
        self.url = url
        self.scraped_content = ''
        self.response = None
        self.xmltree = None
        self.raw_element = None
        self.xpath = xpath
        self.country = country
        self.newspaper = newspaper
        self.error = None
        self.headers = {
            # Used to tell the target site who you are. The agent below is for Chrome browsers
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

        lg.debug("Created scraper with the following parameters:")
        lg.debug(self.__dict__)


    def get_response(self, url):
        response = r.get(url, headers = self.headers)
        lg.debug(f"Response status code {response.status_code}")
        html = response.text

        return html

    def build_xml_tree(self, html):
        return lxml.html.fromstring(html)

    def extract_element(self, xpath):
        return self.xmltree.xpath(xpath)

    def parse_element(self):
        """
        This function should be overwritten in case an eye needs some special processing powers

        Skips content if the parsed content is too long to reduce load

        Should return the parsed element of interest
        :return:
        """
        content = self.raw_element[0].text_content()
        content =  re.sub('\s+', ' ', content)

        if len(content) >= 1000:
            content = "Parsed content was too long to be returned"
        return content

    def show_self(self):
        for key in self.__dict__:
            if key not in ['response', 'xmltree', 'raw_element']:
                lg.info(f"{key}: {self.__dict__[key]}")
            else:
                lg.debug(f"{key}: {self.__dict__[key]}")

    def run(self):
        """
        Go to the provided url and collect the given xpath

        """
        lg.info(f"Collecting data for {self.url}")
        try:
            lg.debug(f"Loaded requests with settings {r.Session().headers}")
            self.response = self.get_response(self.url)
            lg.debug(self.response[:1000])
            try:
                self.xmltree = self.build_xml_tree(self.response)
                lg.debug(self.xmltree)
                try:
                    self.raw_element = self.extract_element(self.xpath)
                    lg.debug(self.raw_element)
                    try:
                        self.scraped_content= self.parse_element()
                    except Exception as e:
                        #TODO make error messages into variables
                        lg.warning("Failed to parse the raw element into text")
                        self.error = e
                except Exception as e:
                    lg.warning("Failed to extract raw element from xml path")
                    self.error = e
            except Exception as e:
                lg.warning("Failed to build xml tree")
                self.error = e
        except Exception as e:
            lg.warning("Failed to get a response")
            self.error = e

        lg.warning(f"errors: {self.error}")
        lg.debug(f"Attempt was made with website {self.url}\nand xml {self.xpath}")
        lg.info(f"\t{self.scraped_content}")
        return self.url, self.scraped_content

    def write(self):
        """
        Writes scrape_timestamp, url and headlines to a json file
        :return:
        """
        result = {
            "scraped_date": TODAY,
            "scraped_timestamp": TIMESTAMP,
            "url": self.url,
            "scraped_content":self.scraped_content,
            "country": self.country,
            "newspaper": self.newspaper,
            "error": str(self.error),
        }

        with open(SCRAPER_OUTPUT_FILE, "a+") as outfile:
            json.dump(result, outfile)
            outfile.write('\n')

            #TODO make create raw get_latest_result_filepathdirectory if not exists

    def run_and_write(self):
        self.run()
        self.write()

def test():
    lg.getLogger().setLevel(lg.DEBUG)

    ns = NewsScraper(
        url="https://www.aftonbladet.se/",
        xpath="//h2[@class='hyperion-css-19rutrz']",
        country="Sweden",
        newspaper="Aftonbladet"
    )
    ns.run()
    lg.getLogger().setLevel(lg.INFO)

if __name__ == "__main__":
    lg.info("Running scraper on aftonbladet for testing purposes in debug modet")
    test()