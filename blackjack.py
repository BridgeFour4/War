# blackjack
# from 1-7 players compete against a dealer
# Nathan Broadbent
# 2/19
#########################################
# imports
import cards, games

##########################################
# classes


class BJCard(cards.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.face_up:
            v = BJCard.RANKS.index(self.rank)+1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJDeck(cards.Deck):
    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))


class BJHand(cards.Hand):

    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if a card in the hand has a value of None then Total is None
        for card in self.cards:
            if not card.value:
                return None
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        # determine if hand contains an ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJCard.ACE_VALUE:
                contains_ace = True
        # if hand contains ace and total is low enough treat ace as 11
        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21


class BJPlayer(BJHand):
    """A BlackJack Player."""
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want to hit(Y/N)")
        return response == "y"

    def bust(self):
        print(self.name,"busts")
        self.lose()

    def lose(self):
        print(self.name, "loses")

    def win(self):
        print(self.name, "wins")

    def push(self):
        print(self.name, "pushes")


class BJDealer(BJHand):
    """A BlackJack Dealer"""
    def is_hitting(self):
        soft = 0
        for i in self.cards:
            if i.value == 10:
                soft += 1
        if soft == 0:
            return self.total <= 17
        else:
            return self.total < 17

    def bust(self):
        print(self.name, "busts")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJGame(object):
    """A BlackJack Game"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJPlayer(name)
            self.players.append(player)
        self.dealer = BJDealer("Dealer: Bob")
        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # deal two initial cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()  # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()  # reveal dealer'sfirst
        if not self.still_playing:
            # since all players have busted, just show the dealers's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                # everyone playing still wins
                for player in self.still_playing:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total>self.dealer.total:
                        player.win()
                    elif player.total<self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()

##########################################
# main


def main():
    print("\t\tWelcome to Blackjack!\n")
    names = []
    number = games.ask_num("how many will be playing 1-7", 1, 7)
    for i in range(number):
        name = games.name_check("enter in a name (no numbers)")
        names.append(name)
    game = BJGame(names)
    again = None
    while again !='n':
        game.play()
        again = games.ask_yes_no("\nDo you want to play again(y,n)")


main()
