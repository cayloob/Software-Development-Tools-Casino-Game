import pygame
from cards import Card, Deck
from hands import BlackJackHand
import dealer
import random

class casino:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height - 60))
        pygame.display.set_caption('The Alfred Casino')
        self.font = pygame.font.SysFont("arial", 60)
        self.font2 = pygame.font.SysFont("arial", 100)
        self.font3 = pygame.font.SysFont("arial", 35)
        self.clock= pygame.time.Clock()

        self.fiat_bux= 1000

        self.coin_head = pygame.image.load("assets\coin_head.png").convert_alpha()
        self.coin_tail = pygame.image.load("assets\coin_tail.png").convert_alpha()

        self.coin_head_rect = self.coin_head.get_rect()
        self.coin_tail_rect = self.coin_tail.get_rect()

        self.quit= self.font.render("Leave Casino", None, "white")
        self.quit_rect= self.quit.get_rect()
        
        self.play_again = self.font.render("Play again", None, "white")
        self.play_again_rect = self.play_again.get_rect()

        self.back_to_main = self.font.render("Back to Menu", None, "white")
        self.back_to_main_rect = self.back_to_main.get_rect()

        self.hand = BlackJackHand()
        self.deck = Deck()
        self.deck.shuffle()
        self.win = 0
        self.total = 0
        self.dealer_hand = dealer.DealerBlackJackHand(deck= self.deck)

        self.choice= 0
        self.game = None

        self.running = True

        self.main_menu()

    def main_menu(self):
        self.screen.fill("antiquewhite3")

        welcome = self.font.render("Welcome to the Alfred University Casino", True, "white")
        weclome_rect= welcome.get_rect()
        weclome_rect.center = (self.screen_width/2, self.screen_height/6)

        play_blackjack = self.font.render("Play Blackjack", True, "white")
        play_blackjack_rect = play_blackjack.get_rect()
        play_blackjack_rect.center = (self.screen_width/2, self.screen_height/2)

        flip = self.font3.render("Flip a Coin", True, "white")
        flip_rect = flip.get_rect()
        flip_rect.center = (self.screen_width-100, self.screen_height-100)

        f_bux = self.font3.render(f"Fiat Bux: {self.fiat_bux}", True, "white")
        f_bux_rect = f_bux.get_rect()
        f_bux_rect.center = (250, 100)

        self.coin_head_rect.center = (100, 100)

        pygame.draw.rect(self.screen, "gray54", play_blackjack_rect)
        pygame.draw.rect(self.screen, "gray54", flip_rect)
        self.screen.blit(play_blackjack, play_blackjack_rect)
        self.screen.blit(flip,flip_rect)
        self.screen.blit(welcome, weclome_rect)
        self.screen.blit(self.coin_head, self.coin_head_rect)
        self.screen.blit(f_bux,f_bux_rect)
            
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
                    if flip_rect.collidepoint(mouse_pos):
                        self.coin_toss()
    
                  
    def blackjack(self):
        self.screen.fill("antiquewhite3")

        self.win = 0
        self.total = 0

        self.game = "blackjack"

        self.fiat_bux -= 100

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

                #Check if the event type is a button press
                if event.type == pygame.KEYDOWN:
                    #If its an 's' Key then player wants to stand, run the stand code
                    if event.key == pygame.K_s:
                        if self.win == 0:
                            self.win = dealer.dealer_play(self.dealer_hand,self.hand,self.deck)
                    #If its an 'h' Key then player wants to hit, run the hit code
                    if event.key == pygame.K_h:
                        if self.win == 0:
                            self.hand.add_card(self.deck)
                            self.total = self.hand.check_total()
                            if self.total > 21:
                                self.win = -1

            if self.win != 0:
                self.game_over()
            else:
                #If it is in a normal state run this code
                self.screen.fill("antiquewhite3")
            #Create the score text and blit to screen
            score_surface = self.font.render(f"Total: {self.total}", True, "white")
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

    def game_over(self):
        won= self.font2.render("You Win!", True, "white")
        won_rect = won.get_rect()
        won_rect.center = (self.screen_width/2, self.screen_height/6)

        lost= self.font2.render("You Lose!", True, "white")
        lost_rect = lost.get_rect()
        lost_rect.center = (self.screen_width/2, self.screen_height/6)

        self.play_again_rect.center = (self.screen_width/2, self.screen_height/2)
        self.quit_rect.center = (self.screen_width *.75, self.screen_height/2)
        self.back_to_main_rect.center = (self.screen_width/4, self.screen_height/2)

        if self.win == -1:
            self.screen.fill("red")
            self.screen.blit(lost, lost_rect)
        else:
            self.fiat_bux += 100
            self.screen.fill("chartreuse3")
            self.screen.blit(won, won_rect)

        pygame.draw.rect(self.screen, "gray54", self.play_again_rect)
        pygame.draw.rect(self.screen, "gray54", self.quit_rect)
        pygame.draw.rect(self.screen, "gray54", self.back_to_main_rect)

        self.screen.blit(self.quit, self.quit_rect)
        self.screen.blit(self.play_again, self.play_again_rect)
        self.screen.blit(self.back_to_main, self.back_to_main_rect)

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.quit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        self.running = False
                    if self.play_again_rect.collidepoint(mouse_pos):
                        if self.game == 'blackjack':
                            self.blackjack()
                        else:
                            self.coin_toss()
                    if self.back_to_main_rect.collidepoint(mouse_pos):
                        self.main_menu()

    def coin_toss(self):
        self.screen.fill("antiquewhite3")

        self.win = 0
        self.game = "coin_toss"

        heads = self.font2.render("HEADS", True, "white")         
        heads_rect = heads.get_rect()
        heads_rect.center = (self.screen_width/4,self.screen_height/2)

        o= self.font.render("or", True, "white")         
        o_rect = o.get_rect()
        o_rect.center = (self.screen_width/2,self.screen_height/2)

        tails = self.font2.render("TAILS", True, "white")         
        tails_rect = tails.get_rect()
        tails_rect.center = (self.screen_width* .75,self.screen_height/2)

        f_bux = self.font3.render(f"Fiat Bux: {self.fiat_bux}", True, "white")
        f_bux_rect = f_bux.get_rect()
        f_bux_rect.center = (250, 100)

        self.coin_head_rect.center = (100, 100)

        pygame.draw.rect(self.screen, "gray54", heads_rect)
        pygame.draw.rect(self.screen, "gray54", tails_rect)
        self.screen.blit(heads, heads_rect)
        self.screen.blit(o, o_rect)
        self.screen.blit(tails, tails_rect)
        self.screen.blit(f_bux,f_bux_rect)
        self.screen.blit(self.coin_head, self.coin_head_rect)

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if heads_rect.collidepoint(mouse_pos):
                        self.choice = 1
                        self.result()
                    if tails_rect.collidepoint(mouse_pos):
                        self.result()
                        
    def result(self):
        self.screen.fill("antiquewhite3")

        result = self.font2.render("It was",True, "white")
        result_rect = result.get_rect()
        result_rect.center = (self.screen_width/2.25,self.screen_height/3.5)

        cont = self.font.render("Continue",True, "white")
        cont_rect = cont.get_rect()
        cont_rect.center = (self.screen_width/2,self.screen_height*.75)

        toss = random.randint(1,2)
        if toss == self.choice:
            self.fiat_bux += 100
            self.win= 1
            won = self.font.render("You won 100 coins!", True, "white")
            won_rect = won.get_rect()
            won_rect.center = (self.screen_width/2,self.screen_height/2)
            self.screen.blit(won, won_rect)

        else:
            self.win = -1
            lost = self.font.render("You Lose, Try again.", True, "white")
            lost_rect = lost.get_rect()
            lost_rect.center = (self.screen_width/2,self.screen_height/2)
            self.screen.blit(lost, lost_rect)
        if toss == 1:
            coin= pygame.transform.scale(self.coin_head, (200,200))
            coin_rect = self.coin_head_rect
        else:
            coin= pygame.transform.scale(self.coin_tail, (200,200))
            coin_rect= self.coin_tail_rect

        coin_rect.center = (self.screen_width* .55,self.screen_height/4)

        pygame.draw.rect(self.screen, "gray54", cont_rect)
        self.screen.blit(coin, coin_rect)
        self.screen.blit(result, result_rect)
        self.screen.blit(cont, cont_rect)

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if cont_rect.collidepoint(mouse_pos):
                        self.game_over()
        
        

casino()
