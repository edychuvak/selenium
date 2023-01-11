from page_objects.home_page import HomePage

class HomeTest(HomePage):

    def setUp(self):
        super().setUp()
        #print("Running before each test")
        # open home page
        self.open_page()

    def tearDown(self):
        #print("Running after each test")
        super().tearDown()

    def test_home_page(self):
        # assert page title
        self.assert_title("Tipsport | Největší komunita sázkařů | Kurzové sázky a online casino")
        # asser logo
        self.assert_element(HomePage.logo_icon)
        #click on the get button and assert the url
        self.click(HomePage.get_pobocky)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "https://www.tipsport.cz/pobocky")
        self.assert_true("pobocky" in get_started_url)

        self.assert_text("Vegas", HomePage.get_text)
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2023 Tipsport.net a.s.", HomePage.copyring_text)

    def test_menu_links(self):
        expected_links = ['LIVE', 'VÝSLEDKY', 'FÓRUM', 'TIKET ARÉNA', 'ANALÝZY', 'BLOGY', 'SOUTĚŽE', 'BONUSY', 'TV', 'MOBILNÍ APLIKACE', 'NÁPADY']

        #find menu links
        menu_links_el = self.find_elements(HomePage.menu_links)

        #loop through our menu links

        for idx, link_el in enumerate(menu_links_el):
            #print(idx, link_el.text)
            self.assertEqual(expected_links[idx], link_el.text)




