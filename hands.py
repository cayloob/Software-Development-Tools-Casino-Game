from cards import Card, Deck
import pygame


class Hand():
    def __init__(self, cards_list):
        self.cards_list = cards_list

    def add_card(self, deck):
        self.cards_list.append(deck.draw())

    def __str__(self):
        hand = ''
        for card in self.cards_list:
            hand = hand + str(card)+' '
        return hand


class BlackJackHand(Hand):
    def __init__(self, bet, cards_list=[],money=100):
        super().__init__(cards_list)
        self.money = money
        self.bet = bet
    def check_total(self):
        total = 0
        ace_as_eleven = False
        for card in self.cards_list:
            if card.value > 10:
                total += 10
            elif card.value == 1:
                # Ace added this is going to be an issue :/
                if total <= 10:
                    ace_as_eleven = True
                    total += 11
                else:
                    total += 1
            else:
                total += card.value
            if total > 21 and ace_as_eleven is True:
                total -= 10
                ace_as_eleven = True
            elif total > 21:
                print('Bust')
        return total


# c1 = Card(1, 1)
# c2 = Card(10, 2)
# cards_list = [c1, c2]

# deck = Deck()
# deck.shuffle()

# hand = BlackJackHand()

# hand.add_card(deck)
# hand.add_card(deck)
# print(hand.check_total())
# hand.add_card(deck)
# hand.add_card(deck)
# print(hand.check_total())
# print(hand)
