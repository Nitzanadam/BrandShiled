from eBay import Ebay
from Amazon import Amazon


def scrap(marketplace_name, search_word):
    marketplace_lowercase = marketplace_name.lower()
    if marketplace_lowercase == "ebay":
        scraping_market = Ebay()
    elif marketplace_lowercase == "amazon":
        scraping_market = Amazon()
    else:
        print("marketplace not found")
        exit()

    json_data = scraping_market.extract_product(search_word, [])
    search_word_id = scraping_market.extract_product_id(search_word, [])
    scraping_market.save_properties_as_json(json_data, marketplace_name,search_word_id)


marketplace_name = input("please enter marketplace name: ")
search_word = input("please enter search_word: ")
scrap(marketplace_name, search_word)
