import pygame
from slots import slots_machine
from cards import Card, Deck
from hands import BlackJackHand
import dealer
import random


class casino:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
        self.screen = pygame.display.set_mode((self.screen_width,
                                              self.screen_height - 60))
        pygame.display.set_caption('The Alfred Casino')
        self.font = pygame.font.SysFont("arial", 60)
        self.font2 = pygame.font.SysFont("arial", 100)
        self.font3 = pygame.font.SysFont("arial", 35)
        self.clock = pygame.time.Clock()

        self.fiat_bux = 1000.

        tail = "assets\coin_tail.png"
        head = "assets\coin_head.png"
        self.coin_head = pygame.image.load(head).convert_alpha()
        self.coin_tail = pygame.image.load(tail).convert_alpha()

        self.coin_head_rect = self.coin_head.get_rect()
        self.coin_tail_rect = self.coin_tail.get_rect()

        self.wheel = pygame.image.load("assets\wheel_spin2.png.png").convert_alpha()
        self.wheel_rect = self.wheel.get_rect()

        self.quit = self.font.render("Leave Casino", None, "white")
        self.quit_rect = self.quit.get_rect()

        self.play_again = self.font.render("Play again", None, "white")
        self.play_again_rect = self.play_again.get_rect()

        self.back_to_main = self.font.render("Back to Menu", None, "white")
        self.back_to_main_rect = self.back_to_main.get_rect()

        self.choose_bet = self.font.render('Choose your bet', True, ('white'))
        self.choose_bet_rect = self.choose_bet.get_rect(center = (self.screen_width/2, self.screen_height * .8))

        
        pygame.mixer.init()
        pygame.mixer.music.load("assets/casino_music3.mp3")
        pygame.mixer.music.play(-1)  # -1 = loop forever
        self.is_muted = False

        
        self.mute_btn = pygame.image.load("assets/mute_button.png").convert_alpha()
        self.mute_btn = pygame.transform.scale(self.mute_btn, (60, 60))  # resize if needed
        self.mute_btn_rect = self.mute_btn.get_rect()


        self.hand = BlackJackHand()
        self.deck = Deck()
        self.deck.shuffle()
        self.win = 0
        self.total = 0
        self.dealer_hand = dealer.DealerBlackJackHand(deck=self.deck)

        self.bet = 0
        self.free_games = 0

        self.wheel_spins = 1

        self.choice = 0
        self.game = None

        self.running = True

        self.main_menu()

    def main_menu(self):
        self.screen.fill("antiquewhite3")

        welcome = self.font.render("Welcome to the Alfred University Casino",
                                   True, "white")
        weclome_rect = welcome.get_rect()
        weclome_rect.center = (self.screen_width/2, self.screen_height/6)

        play_blackjack = self.font.render("Play Blackjack", True, "white")
        play_blackjack_rect = play_blackjack.get_rect()
        play_blackjack_rect.center = (self.screen_width/4,
                                      self.screen_height/2)
        
        play_slots = self.font.render("Alfie's Treasure", True, "white")
        play_slots_rect = play_slots.get_rect()
        play_slots_rect.center = (self.screen_width *.75,
                                      self.screen_height/2)

        flip = self.font3.render("Flip a Coin", True, "white")
        flip_rect = flip.get_rect()
        flip_rect.center = (self.screen_width-100, self.screen_height-100)

        f_bux = self.font3.render(('Fiat Bux: ' + str(round(self.fiat_bux, 2)) + '0'), True, "white")
        f_bux_rect = f_bux.get_rect()
        f_bux_rect.center = (250, 100)

        self.coin_head_rect.center = (100, 100)

        self.wheel = pygame.image.load("assets\wheel_spin2.png.png").convert_alpha()
        self.wheel_rect = self.wheel.get_rect()
        self.wheel_rect.center = (100, self.screen_height - 150)

        self.mute_btn_rect.topleft = (self.screen_width - 70, 10)
        self.screen.blit(self.mute_btn, self.mute_btn_rect)

        pygame.draw.rect(self.screen, "gray54", play_blackjack_rect)
        pygame.draw.rect(self.screen, "gray54", play_slots_rect)
        pygame.draw.rect(self.screen, "gray54", flip_rect)
        self.screen.blit(play_blackjack, play_blackjack_rect)
        self.screen.blit(play_slots, play_slots_rect)
        self.screen.blit(flip, flip_rect)
        self.screen.blit(welcome, weclome_rect)
        self.screen.blit(self.coin_head, self.coin_head_rect)
        self.screen.blit(self.wheel, self.wheel_rect)
        self.screen.blit(f_bux, f_bux_rect)

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

                    if play_slots_rect.collidepoint(mouse_pos):
                        self.slots()

                    if flip_rect.collidepoint(mouse_pos):
                        self.coin_toss()

                    if self.wheel_rect.collidepoint(mouse_pos):
                        self.wheel_spin()

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

                # Check if the event type is a button press
                if event.type == pygame.KEYDOWN:
                    # If its an 's' Key then player
                    # wants to stand, run the stand code
                    if event.key == pygame.K_s:
                        if self.win == 0:
                            self.win = dealer.dealer_play(self.dealer_hand,
                                                          self.hand, self.deck)
                    # If its an 'h' Key then player
                    # wants to hit, run the hit code
                    if event.key == pygame.K_h:
                        if self.win == 0:
                            self.hand.add_card(self.deck)
                            self.total = self.hand.check_total()
                            if self.total > 21:
                                self.win = -1

            if self.win != 0:
                self.game_over()
            else:
                # If it is in a normal state run this code
                self.screen.fill("antiquewhite3")
            # Create the score text and blit to screen
            score_surface = self.font.render(f"Total: {self.total}",
                                             True, "white")
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
        won = self.font2.render("You Win!", True, "white")
        won_rect = won.get_rect()
        won_rect.center = (self.screen_width/2, self.screen_height/6)

        lost = self.font2.render("You Lose!", True, "white")
        lost_rect = lost.get_rect()
        lost_rect.center = (self.screen_width/2, self.screen_height/6)

        h = self.screen_height / 2
        self.play_again_rect.center = (self.screen_width/2, h)
        self.quit_rect.center = (self.screen_width * .75, h)

        self.back_to_main = self.font.render("Back to Menu", None, "white")
        self.back_to_main_rect = self.back_to_main.get_rect()
        self.back_to_main_rect.center = (self.screen_width/4, h)

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
                    if self.back_to_main_rect.collidepoint(mouse_pos):
                        self.main_menu()

    def coin_toss(self):
        self.screen.fill("antiquewhite3")

        self.win = 0
        self.game = "coin_toss"

        heads = self.font2.render("HEADS", True, "white")
        heads_rect = heads.get_rect()
        heads_rect.center = (self.screen_width/4, self.screen_height/2)

        o = self.font.render("or", True, "white")
        o_rect = o.get_rect()
        o_rect.center = (self.screen_width / 2, self.screen_height/2)

        tails = self.font2.render("TAILS", True, "white")
        tails_rect = tails.get_rect()
        tails_rect.center = (self.screen_width * .75, self.screen_height/2)

        self.back_to_main = self.font3.render("Back to Menu", None, "white")
        self.back_to_main_rect = self.back_to_main.get_rect()
        self.back_to_main_rect.center = (self.screen_width- 100, self.screen_height - 100)

        self.wheel = pygame.image.load("assets\wheel_spin2.png.png").convert_alpha()
        self.wheel_rect = self.wheel.get_rect()
        self.wheel_rect.center = (100, self.screen_height - 150)

        f_bux = self.font3.render(('Fiat Bux: ' + str(round(self.fiat_bux, 2)) + '0'), True, "white")
        f_bux_rect = f_bux.get_rect()
        f_bux_rect.center = (250, 100)

        self.coin_head_rect.center = (100, 100)

        if self.wheel_spins > 0:
            self.screen.blit(self.wheel, self.wheel_rect)

        pygame.draw.rect(self.screen, "gray54", heads_rect)
        pygame.draw.rect(self.screen, "gray54", tails_rect)
        pygame.draw.rect(self.screen, "gray54", self.back_to_main_rect)
        self.screen.blit(heads, heads_rect)
        self.screen.blit(o, o_rect)
        self.screen.blit(tails, tails_rect)
        self.screen.blit(self.back_to_main,self.back_to_main_rect)
        self.screen.blit(f_bux, f_bux_rect)
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

                    if self.wheel_spins > 0:
                        if self.wheel_rect.collidepoint(mouse_pos):
                            self.wheel_spin()


    def result(self):
        self.screen.fill("antiquewhite3")

        result = self.font2.render("It was", True, "white")
        result_rect = result.get_rect()
        result_rect.center = (self.screen_width/2.25, self.screen_height/3.5)

        h = self.screen_height *.8
        self.play_again_rect.center = (self.screen_width/2, h)

        f_bux = self.font3.render(('Fiat Bux: ' + str(round(self.fiat_bux, 2)) + '0'), True, "white")
        f_bux_rect = f_bux.get_rect()
        f_bux_rect.center = (250, 100)

        toss = random.randint(1, 2)
        if toss == self.choice:
            win = random.randint(0,1)
            if win == 0:
                self.fiat_bux += 100
                won = self.font.render("You won 100 coins!", True, "white")
            else:
                self.wheel_spins += 1
                won = self.font.render("You won a wheel spin!", True, "white")
            self.win = 1
            won_rect = won.get_rect()
            won_rect.center = (self.screen_width / 2, self.screen_height/2)
            self.screen.blit(won, won_rect)

        else:
            self.win = -1
            lost = self.font.render("You Lose, Try again.", True, "white")
            lost_rect = lost.get_rect()
            lost_rect.center = (self.screen_width/2, self.screen_height/2)
            self.screen.blit(lost, lost_rect)
        if toss == 1:
            coin = pygame.transform.scale(self.coin_head, (200, 200))
            coin_rect = coin.get_rect()
        else:
            coin = pygame.transform.scale(self.coin_tail, (200, 200))
            coin_rect = coin.get_rect()

        coin_rect.center = (self.screen_width * .55, self.screen_height/3.5)

        if self.wheel_spins > 0:
            self.screen.blit(self.wheel, self.wheel_rect)

        pygame.draw.rect(self.screen, "gray54", self.play_again_rect)
        pygame.draw.rect(self.screen, "gray54", self.back_to_main_rect)
        self.screen.blit(coin, coin_rect)
        self.screen.blit(f_bux, f_bux_rect)
        self.screen.blit(self.coin_head, self.coin_head_rect)
        self.screen.blit(result, result_rect)
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
                    if self.play_again_rect.collidepoint(mouse_pos):
                        self.coin_toss()

                    if self.back_to_main_rect.collidepoint(mouse_pos):
                        self.main_menu()

                    if self.wheel_spins > 0:
                        if self.wheel_rect.collidepoint(mouse_pos):
                            self.wheel_spin()


    def slots(self):
        self.screen.fill("antiquewhite3")

        self.game = 'slots'

        if self.bet == 0:
            pygame.draw.rect(self.screen, "gray54", self.choose_bet_rect)
            self.screen.blit(self.choose_bet, self.choose_bet_rect)
            
        else:
            choose_bet = self.font.render(f"${self.bet}0", True, ('white'))
            choose_bet_rect= choose_bet.get_rect()
            choose_bet_rect.center= (self.screen_width/2, self.screen_height * .8)
            pygame.draw.rect(self.screen, "gray54", choose_bet_rect)
            self.screen.blit(choose_bet, choose_bet_rect)

            spin= self.font.render('SPIN', True, ('white'))
            spin_rect = spin.get_rect(center = (self.screen_width/2, self.screen_height*.72))
            pygame.draw.rect(self.screen, "hotpink", spin_rect)
            self.screen.blit(spin, spin_rect)
            

        title= self.font.render("Welcome to Alfie's Treasure", True, ('white'))
        title_rect = title.get_rect(center = (self.screen_width/2, self.screen_height/7))
        self.screen.blit(title, title_rect)

        f_bux = self.font3.render(('Fiat Bux: ' + str(round(self.fiat_bux, 2)) + '0'), True, "white")
        f_bux_rect = f_bux.get_rect()
        f_bux_rect.center = (250, 100)

        self.coin_head_rect.center = (100, 100)

        self.wheel = pygame.image.load("assets\wheel_spin2.png.png").convert_alpha()
        self.wheel_rect = self.wheel.get_rect()
        self.wheel_rect.center = (100, self.screen_height - 150)

        self.back_to_main= self.font3.render("Back to menu", True, ('white'))
        self.back_to_main_rect = self.back_to_main.get_rect(center = (self.screen_width-100, self.screen_height-100))
        pygame.draw.rect(self.screen, "gray54", self.back_to_main_rect)
        self.screen.blit(self.back_to_main, self.back_to_main_rect)

        self.screen.blit(f_bux, f_bux_rect)
        self.screen.blit(self.coin_head, self.coin_head_rect)

        if self.wheel_spins > 0:
            self.screen.blit(self.wheel, self.wheel_rect)

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.choose_bet_rect.collidepoint(mouse_pos):
                        self.bet_select()

                    if self.back_to_main_rect.collidepoint(mouse_pos):
                        self.main_menu()

                    if self.wheel_spins > 0:
                        if self.wheel_rect.collidepoint(mouse_pos):
                            self.wheel_spin()

                    if spin_rect.collidepoint(mouse_pos):
                        sm = slots_machine(self.fiat_bux, self.bet)
                        self.screen.fill("antiquewhite3")
                        result= sm.gen()
                        display_nums= result[0]
                        self.fiat_bux= result[1]
                        if len(result) > 2:
                            bonus_game = result[2]

                            if bonus_game == 0:
                                self.wheel_spins += 1

                                won_wheel_spin = self.font2.render('You Won a Wheel Spin!', True, ('white'))
                                wws_rect = won_wheel_spin.get_rect(center = (self.screen_width/2, self.screen_height/6))
                                pygame.draw.rect(self.screen, "gray54", wws_rect)
                                self.screen.blit(won_wheel_spin, wws_rect)
                                

                        nums= self.font2.render(str(display_nums), True, ('white'))
                        nums_rect = nums.get_rect(center = (self.screen_width/2, self.screen_height/2))

                        f_bux = self.font3.render(('Fiat Bux: ' + str(round(self.fiat_bux, 2)) + '0'), True, "white")
                        f_bux_rect.center = (250, 100)

                        if self.wheel_spins > 0:
                            self.screen.blit(self.wheel, self.wheel_rect)

                        pygame.draw.rect(self.screen, "gray54", choose_bet_rect)
                        pygame.draw.rect(self.screen, "gray54", self.back_to_main_rect)
                        pygame.draw.rect(self.screen, "hotpink", spin_rect)
                        self.screen.blit(nums, nums_rect)
                        self.screen.blit(title,title_rect)
                        self.screen.blit(self.back_to_main, self.back_to_main_rect)
                        self.screen.blit(f_bux, f_bux_rect)
                        self.screen.blit(self.coin_head, self.coin_head_rect)
                        self.screen.blit(choose_bet, choose_bet_rect)
                        self.screen.blit(spin, spin_rect)
                        pygame.display.flip()

                        
            
                    

    def bet_select(self):
        self.screen.fill("antiquewhite3")
        title= self.font.render("Welcome to Alfie's Treasure", True, ('white'))
        title_rect = title.get_rect(center = (self.screen_width/2, self.screen_height/7))
        self.screen.blit(title, title_rect)

        pygame.draw.rect(self.screen, "gray54", self.back_to_main_rect)
        self.screen.blit(self.back_to_main, self.back_to_main_rect)

        f_bux = self.font3.render(('Fiat Bux: ' + str(round(self.fiat_bux, 2)) + '0'),True, "white")
        f_bux_rect = f_bux.get_rect()
        f_bux_rect.center = (250, 100)

        self.coin_head_rect.center = (100, 100)

        self.wheel = pygame.image.load("assets\wheel_spin2.png.png").convert_alpha()
        self.wheel_rect = self.wheel.get_rect()
        self.wheel_rect.center = (100, self.screen_height - 150)

        self.screen.blit(f_bux, f_bux_rect)
        self.screen.blit(self.coin_head, self.coin_head_rect)

        
        choose_bet1 = self.font.render('$0.80', True, 'white')
        cb1_rect = choose_bet1.get_rect(center = (self.screen_width/ 4 , self.screen_height * .8))
        choose_bet2 = self.font.render('$1.00', True, 'white')
        cb2_rect = choose_bet2.get_rect(center = (self.screen_width/ 2 , self.screen_height * .8))
        choose_bet3 = self.font.render('$2.50', True, 'white')
        cb3_rect = choose_bet3.get_rect(center = (self.screen_width * .75 , self.screen_height * .8))

        if self.wheel_spins > 0:
            self.screen.blit(self.wheel, self.wheel_rect)

        pygame.draw.rect(self.screen, "gray54", cb1_rect)
        pygame.draw.rect(self.screen, "gray54", cb2_rect)
        pygame.draw.rect(self.screen, "gray54", cb3_rect)
        self.screen.blit(title, title_rect)
        self.screen.blit(choose_bet1, cb1_rect)
        self.screen.blit(choose_bet2, cb2_rect)
        self.screen.blit(choose_bet3, cb3_rect)

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.back_to_main_rect.collidepoint(mouse_pos):
                        self.main_menu()

                    if self.wheel_spins > 0:
                        if self.wheel_rect.collidepoint(mouse_pos):
                            self.wheel_spin()


                    if cb1_rect.collidepoint(mouse_pos):
                        self.bet = .80
                        self.slots()
                        
                    if cb2_rect.collidepoint(mouse_pos):
                        self.bet = 1.0
                        self.slots()

                    if cb3_rect.collidepoint(mouse_pos):
                        self.bet = 2.5
                        self.slots()

    def wheel_spin(self):
        colors = {'r': [1,2], 'o' : [15,16], 'y':[13,14], 'g': [11,12], 'c': [9,10], 'b': [7,8], 'p': [5,6], 'pi': [3,4]}
        self.screen.fill("antiquewhite3")

        title= self.font2.render("Spin the Wheel!", True, ('white'))
        title_rect = title.get_rect(center = (self.screen_width/2, self.screen_height/7))
        self.screen.blit(title, title_rect)

        f_bux = self.font3.render(('Fiat Bux: ' + str(round(self.fiat_bux, 2)) + '0'),True, "white")
        f_bux_rect = f_bux.get_rect()
        f_bux_rect.center = (250, 100)
        
        self.back_to_main= self.font3.render("Back to menu", True, ('white'))
        self.back_to_main_rect = self.back_to_main.get_rect(center = (self.screen_width-100, self.screen_height-100))

        self.wheel = pygame.transform.scale(self.wheel, (500, 500))
        self.wheel_rect = self.wheel.get_rect(center = (self.screen_width/2, self.screen_height/2))

        spins = self.font.render(f"You Have {self.wheel_spins} spins.", True, ('white'))
        spins_rect = spins.get_rect(center = (self.screen_width/2, self.screen_height* .75))

        pygame.draw.rect(self.screen, "gray54", spins_rect)
        pygame.draw.rect(self.screen, "gray54", self.back_to_main_rect)
        self.screen.blit(title, title_rect)
        self.screen.blit(self.back_to_main, self.back_to_main_rect)
        self.screen.blit(self.wheel, self.wheel_rect)
        self.screen.blit(spins, spins_rect)
        self.screen.blit(f_bux, f_bux_rect)
        self.screen.blit(self.coin_head, self.coin_head_rect)

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.back_to_main_rect.collidepoint(mouse_pos):
                        self.main_menu()
                    
                    if spins_rect.collidepoint(mouse_pos) and self.wheel_spins > 0:
                        self.screen.fill("antiquewhite3")
                        self.wheel_spins -= 1
                        sm = slots_machine(self.fiat_bux, self.bet)
                        results = sm.wheel_spin()
                        spin = results[0]
                        self.fiat_bux = results[1]
                        self.free_games = results[2]

                        wheel = (f'assets\wheel_spin{colors[spin][1]}.png.png')
                        self.wheel = self.wheel = pygame.image.load(wheel).convert_alpha()
                        self.wheel = pygame.transform.scale(self.wheel, (500, 500))
                        
                        f_bux = self.font3.render(('Fiat Bux: ' + str(round(self.fiat_bux, 2)) + '0'), True, "white")
                        f_bux_rect.center = (250, 100)

                        spins = self.font.render(f"You Have {self.wheel_spins} spins.", True, ('white'))
                        spins_rect = spins.get_rect(center = (self.screen_width/2, self.screen_height* .75))

                        pygame.draw.rect(self.screen, "gray54", spins_rect)
                        pygame.draw.rect(self.screen, "gray54", self.back_to_main_rect)
                        self.screen.blit(title, title_rect)
                        self.screen.blit(self.back_to_main, self.back_to_main_rect)
                        self.screen.blit(self.wheel, self.wheel_rect)
                        self.screen.blit(spins, spins_rect)
                        self.screen.blit(f_bux, f_bux_rect)
                        self.screen.blit(self.coin_head, self.coin_head_rect)

                        pygame.display.flip()





casino()