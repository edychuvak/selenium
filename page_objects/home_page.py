from seleniumbase import BaseCase

class HomePage(BaseCase):
    logo_icon = ".headLogo"
    get_pobocky = 'a[href="/pobocky"]'
    get_text = 'a[href="/vegas"]'
    copyring_text = ".o-footerCopyright__row"
    menu_links = "//li[(@class=' o-subMenu__element')]"


    def open_page(self):
        self.open("https://www.tipsport.cz/")