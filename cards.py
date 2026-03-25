def makecards():
    # Quick function to create the cards for the game
    cardslist=[]
    # adds card values (ace,jack,queen,king=1,11,12,13)
    for i in range(1,14):
        cardvalue=[[i],[i],[i],[i]]
        cardslist.append(cardvalue)
    # appends each card with a suit
    for i in cardslist:
        i[0].append('s') # Spade
        i[1].append('c') # Club
        i[2].append('h') # Heart
        i[3].append('d') # Diamond
    return cardslist