import pygame
from cards import Card, Deck
from hands import BlackJackHand
import dealer


class casino:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height - 60))
        pygame.display.set_caption('The Alfred Casino')
        self.font = pygame.font.SysFont("arial", 60)
        self.clock= pygame.time.Clock()

        self.hand = BlackJackHand()
        self.deck = Deck()
        self.deck.shuffle()
        self.win = 0
        self.total = 0
        self.dealer_hand = dealer.DealerBlackJackHand(deck= self.deck)

        self.running = True

        self.main_menu()

    def main_menu(self):
        self.screen.fill("antiquewhite3")
        pygame.display.update()

        welcome = self.font.render("Welcome to the Alfred University Casino", True, "white")
        weclome_rect= welcome.get_rect()
        weclome_rect.center = (self.screen_width/2, self.screen_height/6)

        play_blackjack = self.font.render("Play Blackjack", True, "white")
        play_blackjack_rect = play_blackjack.get_rect()
        play_blackjack_rect.center = (self.screen_width/2, self.screen_height/2)

        pygame.draw.rect(self.screen, "gray54", play_blackjack_rect)
        self.screen.blit(play_blackjack, play_blackjack_rect)
        self.screen.blit(welcome, weclome_rect)
            
        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_blackjack_rect.collidepoint(mouse_pos):
                        self.blackjack()

        #pygame.quit()

    def blackjack(self):
        self.screen.fill("antiquewhite3")
        pygame.display.update()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

                #Check if the event type is a button press
                if event.type == pygame.KEYDOWN:
                    #If its an 's' Key then player wants to stand, run the stand code
                    if event.key == pygame.K_s:
                        self.win = dealer.dealer_play(self.dealer_hand,self.hand,self.deck)
                    #If its an 'h' Key then player wants to hit, run the hit code
                    if event.key == pygame.K_h:
                        self.hand.add_card(self.deck)
                        self.total = self.hand.check_total()

            if self.win == -1:
                #If the player lost run this code
                self.screen.fill("red")
            elif self.win == 1:
                #If the player won run this code
                self.screen.fill("green")
            else:
                #If it is in a normal state run this code
                self.screen.fill("antiquewhite3")
            #Create the score text and blit to screen
            score_surface = self.font.render(f"Total: {self.total}", True, (255, 255, 255))
            self.screen.blit(score_surface, (10, 10))

            for i, card in enumerate(self.hand.cards_list):
            # Making the player's cards appear on the screen
                card.create()
                self.screen.blit(card.image,
                            ((card.rect.center[0]+(20*i)+100),
                            (card.rect.center[1]+(20*i)+100)))

            for i, card in enumerate(self.dealer_hand.cards_list):
                # Making the dealer's cards appear on the screen
                card.create()
                self.screen.blit(card.image,
                            ((card.rect.center[0]+(20*i)-100),
                            (card.rect.center[1]+(20*i)-100)))

            pygame.display.flip()  # refresh screen display
            self.clock.tick(60)  # wait until next frame (runs 60FPS)
