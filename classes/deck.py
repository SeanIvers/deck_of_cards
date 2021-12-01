from . import card
from random import randint

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

class BlackJackDeck(Deck):

    def __init__(self):
        super().__init__()
        
        # print(self.cards[0].string_val)

        for i in self.cards:
            if i.string_val == "Jack" or i.string_val == "Queen" or i.string_val == "King":
                i.point_val = 10
            if i.string_val == "Ace":
                i.point_val = 13

    def pick_random_card(self):
        self.cards[randint(0, len(self.cards) - 1)].card_info()
        return self.cards[randint(0, len(self.cards) - 1)]