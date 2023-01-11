from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_log(self):
        # open page
        self.open("https://www.tipsport.cz/")
        # fill fields
        self.send_keys('input[id="userNameId"]', 'test@test.cz')
        self.send_keys('input[id="passwordId"]', '123456789')
        # click the submit button
        self.click('button[id="btnLogin"]')
        #verify element
        self.is_element_present('div[class="sc-iZnKfu jQhumo"]')
