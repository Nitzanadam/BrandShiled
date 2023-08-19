from marketplace import Marketplace


class Amazon(Marketplace):
    name = "Amazon"

    def generate_search_url(self, search_word, page_number):
        return f"https://www.amazon.com/-/he/s?k={search_word}&page=2&crid=IPIXIEJMBYS2&qid=1692275677&sprefix=rolex%2Caps%2C471&ref=sr_pg_{page_number}"

    def extract_product(self, search_word, page_number):
        """implement id needed"""
        print("extract_product")

    def extract_product_id(self, search_word, page_number):
        """implement id needed"""
        print("extract_product_id")

