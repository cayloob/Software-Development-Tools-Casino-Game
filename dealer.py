# controls the dealer (AI and hand)
import hands
import cards


class DealerBlackJackHand(hands.BlackJackHand):
    # dealer special rule: one card starts
    # face up
    def __init__(self, deck, cards_list=[]):
        super().__init__(cards_list)
        self.add_card(deck)
        self.add_card(deck)
        # one card should be visible, one should be hidden


def dealer_play(dealer_hand, player_hand, deck):
    # dealer AI rules: dealer always hits on
    # <=15, else stands
    # Dealer wins ties, except on 21
    curval = dealer_hand.check_total()

    while curval < 16:
        dealer_hand.add_card(deck)
        curval = dealer_hand.check_total()
    return EndGame(player_hand, dealer_hand)


def EndGame(PlayerHand, DealerHand):
    # check if dealer's hand is acceptable
    # then check if player's hand wins
    playertotal = PlayerHand.check_total()
    if playertotal == 21:
        print("Blackjack! You win!")
        return 1
    elif playertotal > 21:
        print("You busted. You lose...")
        return -1
    else:
        dealertotal = DealerHand.check_total()
        if dealertotal > 21:
            print("Dealer busted. You win!")
            return 1
        elif dealertotal < playertotal:
            print("Your hand is higher than the dealer's. You win!")
            return 1
        else:
            print("The dealer's hand is better. You lose...")
            return -1
