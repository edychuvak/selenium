from seleniumbase import BaseCase

class BetPage(BaseCase):
    bet_add_to_ticket = 'div[class="btnRate"]'
    bet_value = 'input[class^="a-inputMaterialText__input"]'

    def open_page(self):
        self.open("https://www.tipsport.cz/")
