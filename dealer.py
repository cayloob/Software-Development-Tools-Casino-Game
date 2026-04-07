# controls the dealer (AI and hand)
import hands
import cards


class DealerBlackJackHand(BlackJackHand):
    # dealer special rule: one card starts
    # face up
    def __init__(self):
        super.__init__(BlackJackHand(cardslist))
    


class DealerAI(self):
    # dealer AI rules: dealer always hits on
    # <=15, else stands
    # Dealer wins ties, except on 21
    pass
