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
            add your method header here.
        """
        pass  # TODO: implement this method

    def validate_guess(self, guess):
        """
            add your method header here.
        """
        pass  # TODO: implement this method

    def get_player_guess(self):
        """
            add your method header here.
        """
        pass  # TODO: implement this method

    def set_all_ships(self):
        pass  # TODO: implement this method


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