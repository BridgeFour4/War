# nathan broadbent
import random

class Card(object):
    """a playing card
    this class will build a single card
    to build a card call Card() and pass in a rank and suit
    card1 = Card(rank="A",spade="s")"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", 'K']
    SUITS = ["♣", "♢", "♡", "♠"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.face_up = face_up

    def __str__(self):
        if self.face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.face_up = not self.face_up


class Hand(object):
    """A hand of playing cards.
    this class will create a hand to hold cards in a list
    to build a hand call Hand() and don't pass anything in
    my_hand = Hand()
    to use clear call it with no parameters
    my_hand.clear()
    to add cards to hand use add pass in the card
    my_hand.add(card)
    to give a card to another hand use give pass in the card and the other_hand
    my_hand.give(my_hand.cards[0], other_hand)
    """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """A Deck of playing cards
    uses all of the hand functions from above
    use populate after creating the deck as deck.populate()
    this will fill out the deck with all 52 cards
    use deck.shuffle(to shuffle the deck randomly
    deck.deal(hands,per_hand)  will take a list of player hands,
    and how many cards for each hand
    if the deck runs out of cards it will print out of cards
    """
    def populate(self):
        for s in Card.SUITS:
            for r in Card.RANKS:
                self.add(Card(r, s, False))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for i in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. out of cards")


if __name__ =="__main__":
    print("your ran the module directly (and did not 'Import' it).")