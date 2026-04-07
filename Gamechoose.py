import pygame


name = "Please select a game: 1: Blackjack, 2: Poker, 3: Solitaire, 0: Quit"
gamechoice = int(input(name))
if gamechoice == 1:
    pygame.init()
    # run blackjack (in development)
elif gamechoice == 2:
    pygame.init()
    # need to implement poker
elif gamechoice == 3:
    pygame.init()
    # need to implement solitaire
else:
    print("Goodbye.")
    pygame.quit()
