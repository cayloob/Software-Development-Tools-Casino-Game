import random
def makecards():
    # Quick function to create the cards for the game
    cardslist=[]
    # adds card values (ace,jack,queen,king=1,11,12,13)
    for i in range(1,14):
        cardvalue=[[i,'s'],[i,'c'],[i,'h'],[i,'d']]
        cardslist.append(cardvalue)
    return cardslist
class Deck():
    def __init__(self,deckamnt=1):
        pass
    def draw():
        #random.randint()
        pass
    def shuffle():
        pass


