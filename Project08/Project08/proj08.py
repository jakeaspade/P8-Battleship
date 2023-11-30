'''Source Code Header'''
import board
from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project





def main():
    board_size = 5
    ship_list = [5, 4, 3, 3, 2]
    player1 = Player("Player 1", board.Board(board_size), ship_list)
    player2 = Player("Player 2", board.Board(board_size), ship_list)
    game = BattleshipGame(player1, player2)
    game.play()

if __name__ == "__main__":
    main()