from board import Ship,Board #important for the project

## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
import sys
def input( prompt=None ):
   if prompt != None:
       print( prompt, end="" )
   aaa_str = sys.stdin.readline()
   aaa_str = aaa_str.rstrip( "\n" )
   print( aaa_str )
   return aaa_str

class Player(object):
    """
        add your Class header here.
    """
    def __init__(self, name, board, ship_list):
        """
        Initializes the player's name, board, ship list, and list of guesses.
        """
        self.name = name    # Player 1 or Player 2
        self.board = board
        self.ship_list = ship_list
        self.guesses = []

    def validate_guess(self, guess):
        """
        Raises a RuntimeError if the guess is invalid or has already been made.
            Args:
                guess (tuple): the guess of the player
            Returns:
                None
        """
        if guess in self.guesses:
            raise RuntimeError("This guess has already been made!")
        # y coordinate within bounds
        elif guess[0] < 0 or guess[0] > self.board.size:
            raise RuntimeError("Guess is not valid location!")
        # x coordinate within bounds
        elif guess[1] < 0 or guess[1] > self.board.size:
            raise RuntimeError("Guess is not valid location!")

    def get_player_guess(self):
        """
        Gets the player's guess and validates it.
            Args:
                None
            Returns:
                tuple: the player's guess
        """
        while True:
            try:
                guess = input("Enter your guess: ")
                guess = guess.strip().split(",")
                guess = (int(guess[0]), int(guess[1]))
                self.validate_guess(guess)
                return guess
            except RuntimeError as error:
                print(error)
    def set_all_ships(self):
        """
        """
        for ship in self.ship_list:
            while True:
                ship_coords = input(f"Enter the coordinates of the ship \
of size {ship}: ").replace(' ', '').split(",")
                ship_orientation = input(f"Enter the orientation of the ship \
of size {ship}: ")
                for i in range(len(ship_coords)):
                    ship_coords[i] = int(ship_coords[i])
                ship_object = Ship(ship, ship_coords, ship_orientation)
                try:
                    self.board.validate_ship_coordinates(ship_object)
                    self.board.place_ship(ship_object)
                    break
                except RuntimeError as error:
                    print(error)


class BattleshipGame(object):
    """
        add your Class header here.
    """

    def __init__(self, player1, player2):
        """
            add your method header here.
        """

        pass  # TODO: implement this method

    def check_game_over(self):
        """
            add your function header here.
        """
        pass  # TODO: implement this method

    def display(self):
        """
            add your function header here.
        """
        pass  # TODO: implement this method

    def play(self):
        """
            add your function header here.
        """
        pass  # TODO: implement this method