class Card :
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit) :
        self.rank = rank
        self.suit = suit

    def __str__(self) :
        reply = self.rank + self.suit
        return reply
    
class Unprintable_Card(Card) :          #이건 나중에 지우기
    def __str__(self) :
        return "<unprintable>"
    
class Positionable_Card(Card) :
    def __init__(self, rank, suit, face_up = True) :
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self) :
        if self.is_face_up:
            reply = super().__str__()
        else:
            reply = "XX"
        return reply
    
    def flip(self) :
        self.is_face_up = not self.is_face_up

class Hand:
    def __init__(self) :
        self.cards = []
    
    def __str__(self) :
        if self.cards :
            reply = ""
            for card in self.cards:
                reply += str (card) + "  "
        else:
            reply = "<empty>"
        return reply
    
    def clear(self) :
        self.cards = []
    
    def add(self, card) :
        self.cards.append(card)
    
    def give(self, card, other_hand) :
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand) :
    def populate(self) :
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self) :
        import random
        random.shuffle(self.cards)

    def deal(self, hand, per_hand = 2) :
        for rounds in range(per_hand) :
            if self.cards:
                top_card = self.cards[0]
                self.give(top_card, hand)
            else :
                print("OUT of cards!")

class Player(Hand) :
    def __init__(self,name) :
        self.name = name
        pcard = []

    def my_hand(self,deck) :
        self.deck = deck
        name = Hand()       #나중에 수정
        self.deck.deal(name,per_hand = 2)
        print(self.name,": ",name,sep = "")

    
    
class Dealer(Hand) :
    def __init__(self,deck) :
        self.deck = deck
        dealer = Hand()
        m = ["",]
        self.deck.deal(dealer,per_hand = 2)
        #fp = Positionable_Card()
        print("Dealer: ",dealer,sep = "")

    



print("Welcome to the worlds simplest game!\n")
n = []
deck = Deck()
deck.populate()
deck.shuffle()
print("deck = ",deck)


nplayer = int(input("How many players? <1 - 7>: "))

for i in range(nplayer) :
    name = input("Enter player name: ")
    n.append(Player(name))

for i in range(nplayer) :
    n[i].my_hand(deck)

dealer = Dealer(deck)