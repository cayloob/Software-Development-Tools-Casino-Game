import random
import pygame
class Card(pygame.sprite.Sprite):
    def __init__(self,value,suit):
        super().__init__()
        self.value = value
        self.suit = suit
        self.image = pygame.image.load("assets\AU_card_back.png.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (640,360) 
        self.image = pygame.transform.scale(self.image, (150, 150))
    def draw(self):
        if self.suit == 1:
            #Suit is spades
            pass
        if self.suit == 2:
            #Suit is hearts
            pass
        if self.suit == 3:
            #Suit is diamonds
            pass
        if self.suit == 4:
            #Suit is clubs
            pass

def makecards():
    # NOTE: Cards object going to be made, so this code is likely useless
    # Saving for later though

    # Quick function to create the cards for the game
    cardslist = []
    # adds card values (ace,jack,queen,king=1,11,12,13)
    k = "s"
    for i in range(1, 14):
        for j in range(1, 5):
            cardvalue = [i, j, k]
    # TODO: make cardslist one dimensional for convenience
    return cardslist


class Deck():
    # DECK FORMAT: [[1,(card)],[2,(card)]...]
    def __init__(self, deckamnt=1):
        self.cardslist = makecards()

    def draw(self):
        # random.randint()
        nextcard = self.cardslist.popleft()
        return nextcard[1]

    def shuffle(self):
        # randomizes the order of cards in the deck
        # METHOD: make second list of cards
        # move cards into 1 dimensional list in random order
        newcardset = []
        for i in range(1, len(self.cardslist)):
            # COMPLETE: try and see if theres a way to make it pick a random
            # order of numbers EXCLUSIVE
            # random.sample(range(r),i): makes a list of i numbers, randomly
            # selected from 1-r, without duplicates
            position = random.sample(range(52), 52)
            newcard = [position[i], self.cardslist[i]]
            newcardset.append(newcard)
        self.cardslist = newcardset
