# controls the dealer (AI and hand)
import hands
import cards


class DealerBlackJackHand(BlackJackHand):
    # dealer special rule: one card starts
    # face up
    def __init__(self):
        super.__init__(BlackJackHand(cardslist))
        self.add_card()
        self.add_card()
        # one card should be visible, one should be hidden

class DealerAI(self):
    # dealer AI rules: dealer always hits on
    # <=15, else stands
    # Dealer wins ties, except on 21
    currval=check_total
    if currval<16:
        # hit
        DealerHand.add_card()


def EndGame():
    # check if dealer's hand is acceptable
    # then check if player's hand wins
    if playertotal > 21:
        print("You lose"):
    else:
        dealertotal = DealerHand.check_total()
        if dealertotal>21:
            print("You win!")