# blackjack
# 2 players
# Nathan Broadbent, kaleb beck, tyson vorwaller, andrew kellmer,dominic santistevan
# 2/19

#########################################
# imports
import cards, games

class WarHand(cards.Hand):
    def __init__(self, name, place):
        super(WarHand, self).__init__()
        self.name = name
        self.place = place

    def __str__(self):
        rep = self.name + ":\t" + len(self.cards)
        return rep


class WarPlayer(WarHand):

    def win_battle(self):
        print(self.name, "Won the battle")
        return self.place


class WarDeck(cards.deck):
    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.cards.append(WarCard(rank, suit))


class WarCard(cards.Card):
    ACE_VALUE = 1
    @property
    def value(self):
        if self.face_up:
            v = WarCard.RANKS.index(self.rank) + 1
        else:
            v = None
        return v

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Field(cards.Hand):
    @property
    def winner(self):
        if self.cards[0]>self.cards[1]

class Pot(cards.Hand):
    def __init__(self, winner):
        super(WarHand, self).__init__()
        self.winner = winner

    def give_winner(self):
        for card in self.cards:
            self.give(card, self.winner)



class WarGame(object):
    def __init__(self,names):
        self.deck = WarDeck()
        self.deck.shuffle()
        self.player1 = WarPlayer(names[0],0)
        self.player2 = WarPlayer(names[1],1)
        self.players = [self.player1, self.player2]
        self.pot = Pot()
        self.field = Field()

    def battle(self):
        self.player1.give(self.player1.cards[0],self.field.cards)
        self.player2.give(self.player2.cards[0],self.field.cards)
        #print(card1, "\n", card2)
        #if card1.value() == 1 and card2.value() == 13:
        #    place = self.player1.win_Battle()
        #elif card2.value() == 1 and card1.value() == 13:
        #    place = self.player2.win_Battle()

        #if card1.value() == card2.value():
         #   cards, token = self.tie(cards)

        #elif card1.value() > card2.value():
        #    place = self.player1.win_battle()

        #else:
        #    place = self.player1.win_battle()

        #for i in cards:
        #    self.players[place].add(i)

    def tie(self,cards):
        for i in range(3):
            card1 = self.player1[0]
            card2 = self.player2[0]
            cards.append(card1)
            cards.append(card2)
        card1 = self.player1[0]
        card2 = self.player2[0]
        return cards,


