import random
def makecards():
    # Quick function to create the cards for the game
    cardslist=[]
    # adds card values (ace,jack,queen,king=1,11,12,13)
    for i in range(1,14):
        cardvalue=[[i,'s'],[i,'c'],[i,'h'],[i,'d']]
        cardslist.append(cardvalue)
    # TODO: make cardslist one dimensional for convenience
    return cardslist
class Deck():
    def __init__(self,deckamnt=1):
        self._cardslist=makecards()
    def draw():
        #random.randint()
    def shuffle():
        # randomizes the order of cards in the deck
        # METHOD: make second list of cards
        # move cards into 1 dimensional list in random order
        newcardset=[]
        for card in self._cardslist:
            position=random.randint(1,52)
            newcard=[position,card[0],card[1]]
        newcardset.sort()
            


