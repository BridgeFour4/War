# blackjack
# 2 players
# Nathan Broadbent, kaleb beck, tyson vorwaller, andrew kellmer,dominic santistevan
# 2/19

#########################################
# imports
import cards, games


class WarHand(cards.Hand):
    """ allows for the name and the place to be added for each player"""
    def __init__(self, name, place):
        super(WarHand, self).__init__()
        self.name = name
        self.place = place

    def __str__(self):
        """changes the string to display how many cards you have"""
        rep = self.name + ":\t" + str(len(self.cards))
        return rep


class WarPlayer(WarHand):
    """win battle displays the winner
    lose_game return if they lost
    """
    def win_battle(self):
        print(self.name, "Won the battle")
        return self.place

    def lose_game(self):
        if len(self.cards) == 0:
            return 1
        return 0


class WarDeck(cards.Deck):
    """uses war card for value system"""
    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.cards.append(WarCard(rank, suit))


class WarCard(cards.Card):
    """value for each of the cards to see which is greater"""
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
        #returns who won the battle or if it was a tie
        winner = None
        #special for ace and king
        if self.cards[0].value == 1 and self.cards[1].value == 13:
            winner = 0
            return winner
        elif self.cards[1].value == 1 and self.cards[0].value == 13:
            winner = 1
            return winner
        # normal checks
        elif self.cards[0].value > self.cards[1].value:
            winner = 0
        elif self.cards[0].value < self.cards[1].value:
            winner = 1
        elif self.cards[0].value == self.cards[1].value:
            winner = "tie"
        return winner

    def give_to_pot(self, target):
        for i in range(len(self.cards)):
            self.give(self.cards[0], target)


class Pot(cards.Hand):
    def __init__(self, winner=None):
        super(Pot, self).__init__()
        self.winner = winner

    def give_winner(self):
        #didn't work had to change
        for card in range(len(self.cards)):
            self.give(self.cards[0], self.winner)



class WarGame(object):
    def __init__(self, names):
        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()
        self.player1 = WarPlayer(names[0], 0)
        self.player2 = WarPlayer(names[1], 1)
        self.players = [self.player1, self.player2]
        self.pot = Pot()
        self.field = Field()

    def battle(self):
        self.player1.give(self.player1.cards[0], self.field)
        self.player2.give(self.player2.cards[0], self.field)
        #Nathans work
        print(self.field)
        winner = self.field.winner
        self.field.give_to_pot(self.pot)
        if winner == "tie":
            for i in range(1):
                if len(self.player1.cards) == 0:
                    break
                for i in range(3):
                    # see issue with the index if they can't add three cards in
                    try:
                        self.player1.give(self.player1.cards[0], self.pot)
                    except:
                        print("player has no cards left for war will use last card")
                        self.pot.give(self.pot.cards[-1], self.player1)
                        break

            for i in range(1):
                if len(self.player2.cards) == 0:
                    break
                for i in range(3):
                    try:
                        self.player2.give(self.player2.cards[0], self.pot)
                    except:
                        print("player has no cards left for war will use last card")
                        self.pot.give(self.pot.cards[-1], self.player2)
                        break

            print("a war has started number of cards in pot is", len(self.pot.cards))
            if len(self.player2.cards) != 0 and len(self.player1.cards) != 0:
                self.battle()
        else:
            self.players[winner].win_battle()
            self.pot.winner = self.players[winner]
            self.pot.give_winner()

    #nathan worked on
    def play(self):
        self.deck.deal(self.players, 26)
        win=""
        while win == "":
            print(self.player1)
            print(self.player2)
            self.battle()
            lose1 = self.player1.lose_game()
            lose2 = self.player2.lose_game()
            if lose1 == 1 and lose2 == 1:
                win = "Tie, Nobody"
            elif lose1 == 1:
                win = self.player2.name
            elif lose2 == 1:
                 win = self.player1.name
            input("press enter to continue")
        print(win, "Won The Game")



#########################################################
# main
def main():
    name1 = games.name_check("enter player 1's name (no numbers)")
    name2 = games.name_check("enter player 2's name (no numbers)")
    names = [name1, name2]
    game = WarGame(names)
    game.play()


main()
