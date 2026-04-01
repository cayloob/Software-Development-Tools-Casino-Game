class Hand():
    def __init__(self,cards_list):
        self.cards_list = cards_list
    def add_card(self,deck):
        self.cards_list.append(deck.draw())

class BlackJackHand(Hand):
    def __init__(self,cards_list):
        super().__init__(cards_list)
    def check_total(self):
        for card in self.cards_list:
            pass