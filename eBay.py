from marketplace import Marketplace
import json


class Ebay(Marketplace):

    name = "eBay"

    def generate_search_url(self, search_word, page_number):
        return f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={search_word}&_sacat=0&_dmd=1&_ipg=60&_pgn={page_number}&rt=nc"

    def extract_product(self, search_word, data):
        page_number = 1
        while True:
            print(page_number)
            soup = self.create_soup(search_word, page_number, data, self.name)
            list_of_products = soup.find_all('li', class_='s-item')[1:61]
            if len(list_of_products) == 0:
                print("no more pages")
                break
            else:
                for product in list_of_products:
                    product_properties = self.extracting_properties(product)
                    data.append(product_properties)
            page_number += 1
        json_string = json.dumps(data, indent=2)
        return json.loads(json_string)

    def extract_product_id(self, search_word, data):
        soup = self.create_soup(search_word, 1, data, self.name)
        item_to_extract_search_word_id = soup.find_all('span', class_='clipped')[0]
        search_word_id = item_to_extract_search_word_id['id']
        return search_word_id

    @staticmethod
    def extracting_properties(product):
        return {'title': product.find('div', class_='s-item__title').text,
                'description': product.find('div', class_='s-item__subtitle').text,
                'price': product.find('span', class_='s-item__price').text,
                'img': product.find('div', class_='s-item__image-wrapper image-treatment').find('img')['src']}


