import pygame
from cards import Card, Deck
from hands import BlackJackHand
pygame.init()

'''AU_logo = pygame.image.load("AU_logo.png")
logo_rect = AU_logo.get_rect()'''


screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((screen_width, screen_height - 60))

screen.fill("antiquewhite3")

font = pygame.font.SysFont('roboto', 60)

pygame.display.set_caption('The Alfred Casino')

clock= pygame.time.Clock()
hand = BlackJackHand()
deck = Deck()
deck.shuffle()

font = pygame.font.Font(None, 36) 
total = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            hand.add_card(deck)
            total = hand.check_total()

    if total > 21:
        screen.fill("red")
    else:
        screen.fill("green")

    score_surface = font.render(f"Total: {total}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    for i,card in enumerate(hand.cards_list):
        card.create()
        screen.blit(card.image,((card.rect.center[0]+(10*i)),(card.rect.center[1]+(10*i))))

    pygame.display.flip() # refresh screen display
    clock.tick(60) # wait until next frame (runs 60FPS)
