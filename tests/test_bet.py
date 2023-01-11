from page_objects.bet_page import BetPage

class BetTest(BetPage):
    def setUp(self):
        super().setUp()
        self.open_page()
    def test_bet(self):
        self.click(BetPage.bet_add_to_ticket)
        self.set_value(self.bet_value, '999')
