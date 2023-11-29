class Ship(object):
    """
        add your Class header here.
    """

    def __init__(self, length, position, orientation):
        """
        Initializes a ship object with the given
        length, position, and orientation.
            Args:
                length (int): the length of the ship
                position (list): the position of the ship
                orientation (str): the orientation of the ship
            Returns:
                None
        """
        self.length = length
        self.positions = []
        self.orientation = orientation

        if self.orientation == "h":
            for i in range(self.length):
                self.positions.append((position[0] + i, position[1]))
        else:
            for i in range(self.length):
                self.positions.append((position[0], position[1] + i))

        self.hit_count = 0
        self.is_sunk = False

    def get_positions(self):
        """
        Returns a list of positions that the ship occupies.
            Args:
                None
            Returns:
                list: a list of positions that the ship occupies
        """
        return self.positions

    def get_orientation(self):
        """
        Returns the orientation of the ship as a srting.
            Args:
                None
            Returns:
                str: the orientation of the ship
        """
        return self.orientation

    def apply_hit(self):
        """
        Applies a hit to the ship by incrementing the hit_count.
            Args:
                None
            Returns:
                None
        """
        self.hit_count += 1


class Board(object):
    """
        add your Class header here.
    """

    def __init__(self, size):
        """
        Initializes the board size, creates an empty board, and initializes
        an empty list of ships.
            Args:
                size (int): the size of the board
            Returns:
                None
        """
        self.size = size
        self.board = []
        for i in range(self.size):
            self.board.append([])
            for j in range(self.size):
                self.board[i].append(" ")
        self.ships = []

    def place_ship(self, ship):
        """
        Places a ship on the board.
        """

        for coords in ship.get_positions():
            self.board[coords[1]][coords[0]] = "S"

    def apply_guess(self, guess):
        """
        Determines if the guess is a hit or miss and updates the board.
            Args:
                guess (tuple): the guess of the player
            Returns:
                None
        """
        if self.board[guess[0]][guess[1]] == "S":
            self.board[guess[0]][guess[1]] = "H"
            print("Hit!")
        else:
            self.board[guess[0]][guess[1]] = "M"
            print("Miss!")

    def validate_ship_coordinates(self, ship):
        """
            Rasies a RuntimeError if the ship coordinates are invalid.
            Args:
                ship (Ship): a Ship object
            Returns:
                None
        """
        try:
            for position in ship.get_positions():
                if self.board[position[1]][position[0]] == "S":
                    raise RuntimeError("Ship coordinates are already taken!")
        except IndexError:
            raise RuntimeError("Ship coordinates are out of bounds!")


    def __str__(self):
        """
        prints the board as a string in a matrix format
            Args:
                None
            Returns:
                str: the board as a string
        """
        board_string = ""
        for i in range(self.size):
            for j in range(self.size):
                board_string += f'[{self.board[i][j]}]'
            board_string += "\n"
        return board_string

