from cards import Card
class Hand():
    def __init__(self,cards_list):
        self.cards_list = cards_list
    def add_card(self,deck):
        self.cards_list.append(deck.draw())

class BlackJackHand(Hand):
    def __init__(self,cards_list):
        super().__init__(cards_list)
    def check_total(self):
        total = 0
        ace_as_eleven = True
        for card in self.cards_list:
            if card.value > 10:
                total+=10
            elif card.value == 1:
                #Ace added this is going to be an issue :/
                if total <= 10: 
                    ace_as_eleven = True
                    total+=11
                else:
                    total+=1
            else:
                total += card.value
            if total>21 and ace_as_eleven ==False:
                print('Bust')
                break
            elif total>21:
                total -=10
                ace_as_eleven = True
        return total
c1 = Card(1,1)
c2 = Card(10,2)
cards_list = [c1,c2]

hand = BlackJackHand(cards_list)

print(hand.check_total())


