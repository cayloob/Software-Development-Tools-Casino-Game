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


class DealerBlackJackAI(DealerBlackJackHand):
    # dealer AI rules: dealer always hits on
    # <=15, else stands
    # Dealer wins ties, except on 21
    currval = DealerBlackJackHand.check_total()
    if currval < 16:
        # hit
        DealerBlackJackHand.add_card()
    else:
        return EndGame(PlayerHand, DealerBlackJackHand)


def EndGame(PlayerHand, DealerHand):
    # check if dealer's hand is acceptable
    # then check if player's hand wins
    playertotal = PlayerHand.check_total()
    if playertotal == 21:
        print("Blackjack! You win!")
    elif playertotal > 21:
        print("You busted. You lose...")
    else:
        dealertotal = DealerHand.check_total()
        if dealertotal > 21:
            print("Dealer busted. You win!")
        elif dealertotal < playertotal:
            print("Your hand is higher than the dealer's. You win!")
        else:
            print("The dealer's hand is better. You lose...")
