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
        Creates a player object with a name, board, ship list, and list of
        guesses. This is used to keep track of the player's information by
        keeping track of the instance of the player's board from the
        Board class.
    """
    def __init__(self, name, board, ship_list):
        """
        Initializes the player's name, board, ship list, and list of guesses.
            Args:
                name (str): the name of the player
                board (Board): the player's board
                ship_list (list): the list of ships
            Returns:
                None
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
            raise RuntimeError("Guess is not a valid location!")
        # x coordinate within bounds
        elif guess[1] < 0 or guess[1] > self.board.size:
            raise RuntimeError("Guess is not a valid location!")

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
            except RuntimeError as error:  # prints why the guess is invalid
                print(error)
            except ValueError:  # if the guess is not in the correct format
                print("Guess is not a valid location!")
    def set_all_ships(self):
        """
        Places all the ships on the board.
            Args:
                None
            Returns:
                None
        """
        for ship in self.ship_list:
            while True:  # reprompts if the ship is invalid
                ship_coords = input(f"Enter the coordinates of the ship \
of size {ship}: ").replace(' ', '').split(",")
                ship_orientation = input(f"Enter the orientation of the ship \
of size {ship}: ")
                for i in range(len(ship_coords)):  # converts to int
                    ship_coords[i] = int(ship_coords[i])
                ship_object = Ship(ship, ship_coords, ship_orientation)
                try:  # tries to place the ship on the board
                    self.board.validate_ship_coordinates(ship_object)
                    self.board.place_ship(ship_object)
                    break  # breaks out of the loop if the ship is valid
                except RuntimeError as error:  # prints why the ship is invalid
                    print(error)


class BattleshipGame(object):
    """
        Conducts the processes involved in playing the game between two
        players.
    """

    def __init__(self, player1, player2):
        """
            Initializes the players as objects within the game
            Args:
                player1 (Player instance): the first player
                player2 (Player instance): the second player
            Returns:
                None
        """
        self.player1 = player1
        self.player2 = player2


    def check_game_over(self):
        """
            Checks if the game is over by checking if all the ships of a player
            are sunk.
            Args:
                None
            Returns:
                str: the name of the player who won
        """
        sunk = 0
        for ship in self.player1.board.ships:
            if ship.is_sunk:
                sunk += 1
        if sunk == len(self.player1.board.ships):  # if all ships are sunk
            return "Player 2"  # player 2 wins
        sunk = 0
        for ship in self.player2.board.ships:
            if ship.is_sunk:
                sunk += 1
        if sunk == len(self.player2.board.ships):  # if all ships are sunk
            return "Player 1"  # player 1 wins
        return ""  # if no one has won


    def display(self):
        """
            Displays the boards of both players.
            Args:
                None
            Returns:
                None
        """
        print("Player 1's board:")
        print(self.player1.board)
        print("Player 2's board:")
        print(self.player2.board)


    def play(self):
        """
        Main game loop. After setting up the boards, the game will continue
        to prompt the players for guesses until one of them wins or they don't
        want to continue playing.
            Args:
                None
            Returns:
                None
        """
        command = 'c'
        self.player1.set_all_ships()  # sets all the ships for player 1
        self.player2.set_all_ships()  # sets all the ships for player 2
        while command == 'c':  # while the players want to continue playing
            self.display()
            # player 1's turn processes
            print("Player 1's turn.")
            guess = self.player1.get_player_guess()
            self.player2.board.apply_guess(guess)
            self.player1.guesses.append(guess)
            if self.check_game_over() == "Player 1":
                print("Player 1 wins!")
                break
            # player 2's turn processes
            print("Player 2's turn.")
            guess = self.player2.get_player_guess()
            self.player1.board.apply_guess(guess)
            self.player2.guesses.append(guess)
            if self.check_game_over() == "Player 2":
                print("Player 2 wins!")
                break
            # asks the players if they want to continue playing
            command = input("Continue playing?: ")