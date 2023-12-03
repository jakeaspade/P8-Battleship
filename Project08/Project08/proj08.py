###############################################################################
#   Computer Project #8
#   Initialize the game the board size and sizes of the ships
#   Create two players objects with the board and ships
#   Create a game object with the two players which will operate the game
#      Ask the players to place their ships and reprompt if the ship is invalid
#      While neither player has won or has quit
#         Ask the players to guess and reprompt if the guess is invalid
#         Apply the guess to the board and check if the player has won
#         If the player has won, print the winner and end the game
###############################################################################
'''
Import the board and game modules and initialize the game crucial objects to
allow the game to be played.
'''
import board
from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project





def main():
    board_size = 5
    ship_list = [5, 4, 3, 3, 2]
    player1 = Player("Player 1", board.Board(board_size), ship_list)
    player2 = Player("Player 2", board.Board(board_size), ship_list)
    # create a game object with 2 defined players objects
    game = BattleshipGame(player1, player2)
    game.play()  # play the game

if __name__ == "__main__":
    main()