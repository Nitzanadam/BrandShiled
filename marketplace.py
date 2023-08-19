from abc import ABC,abstractmethod
import requests
from bs4 import BeautifulSoup
import json


class Marketplace(ABC):
    @abstractmethod
    def generate_search_url(self, search_word, page_number):
        """built the url of the scraping page"""

    @abstractmethod
    def extract_product(self, search_word, data):
        """extracting the data we want to scrap"""

    @abstractmethod
    def extract_product_id(self, search_word,data):
        """extracting the data we want to scrap"""

    def create_soup(self, search_word, page_number, data, name):
        url = self.generate_search_url(search_word, page_number)
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            return soup
        except requests.exceptions.RequestException as e:
            print("An error occurred during the request:", e)
            json_string = json.dumps(data, indent=2)
            json_data = json.loads(json_string)
            search_word_id = self.extract_product_id(search_word, data)
            self.save_properties_as_json(json_data, name, search_word_id)
            print("the last scrap page ", page_number)
            exit()

    @staticmethod
    def save_properties_as_json(json_data, marketplace_name, search_word_id):
        with open(f'{marketplace_name}_{search_word_id}.json', 'w') as f:
            json.dump(json_data, f, indent=4)

