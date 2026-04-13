import pygame
from cards import Card, Deck
from hands import BlackJackHand
import dealer
pygame.init()

'''AU_logo = pygame.image.load("AU_logo.png")
logo_rect = AU_logo.get_rect()'''


screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((screen_width, screen_height - 60))

screen.fill("antiquewhite3")

font = pygame.font.SysFont('roboto', 60)

pygame.display.set_caption('The Alfred Casino')
# Initializing all of the objects to be used in the program.
clock = pygame.time.Clock()
hand = BlackJackHand()
deck = Deck()
deck.shuffle()
win = 0
font = pygame.font.Font(None, 36)
total = 0
dealer_hand = dealer.DealerBlackJackHand(deck=deck)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the event type is a button press
        if event.type == pygame.KEYDOWN:
            # If its an 's' Key then player wants to stand, run the stand code
            if event.key == pygame.K_s:
                win = dealer.dealer_play(dealer_hand, hand, deck)
            # If its an 'h' Key then player wants to hit, run the hit code
            if event.key == pygame.K_h:
                hand.add_card(deck)
                total = hand.check_total()

    if win == -1:
        # If the player lost run this code
        screen.fill("red")
    elif win == 1:
        # If the player won run this code
        screen.fill("green")
    else:
        # If it is in a normal state run this code
        screen.fill("black")
    # Create the score text and blit to screen
    score_surface = font.render(f"Total: {total}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    for i, card in enumerate(hand.cards_list):
        # Making the player's cards appear on the screen
        card.create()
        screen.blit(card.image,
                    ((card.rect.center[0]+(20*i)+100),
                     (card.rect.center[1]+(20*i)+100)))

    for i, card in enumerate(dealer_hand.cards_list):
        # Making the dealer's cards appear on the screen
        card.create()
        screen.blit(card.image,
                    ((card.rect.center[0]+(20*i)-100),
                     (card.rect.center[1]+(20*i)-100)))

    pygame.display.flip()  # refresh screen display
    clock.tick(60)  # wait until next frame (runs 60FPS)
