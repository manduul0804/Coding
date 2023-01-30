import random

class Card:
    #Card object requirements 
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = ["Ace", "2", "3", "4", "5","6","7","8","9","10","Jack","Queen","King"]
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    # Create a deck using the Card object
    def __init__(self, shuffle = False):
        #We can shuffle the deck when we create our deck object
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        #First it loops through Card.suits, which has 4 variables. Then the inner loop iterate in Card.values which has 13 variables. In total the Deck object will have 52 Card objects. 
        if shuffle:
            #If shuffle is True, then shuffle the deck of cards
            random.shuffle(self.cards)

    def pickACard(self):
        #First pick a random integer number between 0 to 52
        random_card = random.randint(0,51)
        #We select a random card using the random number we found in random_card
        print(f"Your picked card is {self.cards[random_card]}")
    
    def deck_len(self):
        #Return the length of the Deck object
        return len(self.cards)

    def deal(self, count = 1):
        #Deal card based on the input number. Default deal count is 1. For example, if count = 7, then each players will have 7 cards. Note player number is not given
        cards = self.cards[:count]
        self.cards = self.cards[count:]
        return cards

    def print_deck(self):
        #Print out the Card names that exists in the Deck object list
        for card in self.cards:
            print(card)


deck = Deck(shuffle=True)
print("\n1st randomly picked card.")
deck.pickACard()

print("\n2nd randomly picked card.")
deck.pickACard()

print("\n3rd randomly picked card.")
deck.pickACard()
# deck.print_deck()
print("\nThe lenght of the deck is:")
print(deck.deck_len())

# cards = deck.deal(5)
# print(cards)



        
