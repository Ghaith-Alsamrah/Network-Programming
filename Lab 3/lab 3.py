import random


class Card: 
    def __init__ (self, suit, value): 
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit 
        self._value = value
    def getValue(self):
        return self._value
    
    def getSuit(self): 
        match self._suit: 
            case 1: 
                return "spades"
            case 2: 
                return "hearts"
            case 3: 
                return "diamonds"
            case 4: 
                return "clubs"

                
    def __str__(self): 
        value = self.getValue()
        if value == 10:
            value = "Jack"
        elif value ==11:
            value = "Queen"
        elif value ==12:
            value = "King"
        suit = self.getSuit()
        return " {} of {}".format(value, suit)


class CardDeck: 
    def __init__(self):
        self.reset()

    def shuffle (self):
        random.shuffle(self._cards)
    def getCard(self):
        theCard = self._cards[-1]
        
        self._cards.pop() 
        return theCard 
    def size (self): 
        return len(self._cards)
    def reset (self):
        self._cards = []
        for sort in range(1,5): 
            for number in range(1,14): 
                self._cards.append(Card(sort,number)) 

deck = CardDeck()
deck.shuffle()
while deck.size()>0:
    card = deck.getCard()
    print("Card {} has value {}".format(card, card.getValue()))