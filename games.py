import cards


def ask_num(message, min, max):
    """ask for a number within a range
    when you call this up you will pass in a string message a minimum value
    and a maximum value
    ask_num("enter a number between 2-7",2,7)"""
    while True:
        try:
            number = int(input(message))
        except:
            print("that was not a number")
            continue
        if max >= number >= min:
            break
    return number


def ask_yes_no(question):
    """this is to be used for asking yes or no questions
    when you call it up you need a catching variable for the
    yes or no value as a y or n
    ask_yes_no("is 2+2 = 4")
    """
    response = None
    while response not in ("y", "n"):
        response = input(question+" y or n").lower()
    return response


def switch_turn(turn,num):
    """this will increase the turn by one every time it is called up
    you must have a turn already created
    and you must pass in the turn and then the number of players
    switch_turn(0,5)

    """
    turn += 1
    if turn == num:
        turn = 0
    return turn


def roll(name, number):
    """it will roll the amount of dice you pass in
    you must pass in the players name and the number of dice
    roll("nathan",5)
    """
    import random
    rolls = []
    total = 0
    for i in range(number):
        die = random.randint(1, 6)
        roll = die
        rolls.append(roll)

    for i in rolls:
        total += i

    print(name, "rolled a ", total)
    return total


def name_check(message):
    """this will mainly be used to check that a name is all alphabetical
    however this can be used whenever you need to check that it is a string
    you must pass in a message for the question
    name_check("what is your name")"""
    name = input(message)
    while True:
        if name.isalpha():
            return name
        else:
            name = input(message)


class Player(object):

    """A player for a game"""
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name
        rep = rep+" "+str(self.score)
        return rep


if __name__ == "__main__":
    print("You ran this module directly that won't do anything")
    input()
