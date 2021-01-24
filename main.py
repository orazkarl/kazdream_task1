import random

class Player:
    """
    Class Player. The player has a name and a ticket with 5 random numbers (numbers from 1 to 99).
    """
    def __init__(self, name):
        """
        Constructor
        """
        self.name = name
        self.ticket = random.sample(range(1, 100), 5)

    def update(self, game):
        """
        Notifies the player of the current bingo number.
        """
        # If bingo number in player ticket
        if game.number in self.ticket:
            # remove it from ticket
            self.ticket.remove(game.number)
            # If player ticket is empty
            if self.ticket == []:
                # Print winner and finish game
                print(self.name + ' BINGO!!!')
                game.game_status = False


class Game:
    """
    Class Game. The player has a name and a ticket with 5 random numbers (numbers from 1 to 99).
    The program should randomly select a number from 1 to 99, display it on the console and notify
    the players about this number. The player who first collected his combination must call out his
    name and the program stops.
    """
    def __init__(self):
        """
        Constructor
        """
        self.players = []
        self.number = 0
        self.game_status = True


    def init_players(self, players):
        """
        Initializes bingo players
        """
        for player in players:
            self.players.append(Player(player))

    def start_game(self):
        """
        Starts the  bingo game
        """
        # Insert numbers from 0 to 99
        numbers = list(range(1,100))
        print('Welcome to the bingo game')
        # While loop until a winner is determined
        while self.game_status:
            # Choice a random number from numbers
            self.number = random.choice(numbers)
            # Remove random number from numbers
            numbers.remove(self.number)
            # Print bingo number and check players ticket
            print(f'We got number: {self.number}')
            for player in self.players:
                player.update(self)


if __name__ == '__main__':
    players = [
        'Karl',
        'Kuka',
        'Maks',
        'Baha',
        'Aza'
    ]

    game = Game()
    game.init_players(players)
    game.start_game()

