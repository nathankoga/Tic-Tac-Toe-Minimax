import unittest
import tictactoe
from player_types import HardBot, Player


# class T0_board_checks(unittest.TestCase):
#
#     def test_horizontal_one(self):
#         # "top row win condition"
#         board = tictactoe.Board()
#         board.board = ["X", "X", "X",
#                        "", "", "",
#                        "", "", ""]
#         self.assertEqual(board.win_check(board.board), "X")
#
#     def test_horizontal_two(self):
#         # "middle row win condition"
#         board = tictactoe.Board()
#         board.board = ["", "", "",
#                        "X", "X", "X",
#                        "", "", ""]
#         self.assertEqual(board.win_check(board.board), "X")
#
#     def test_horizontal_three(self):
#         # "bottom row win condition"
#         board = tictactoe.Board()
#         board.board = ["", "", "",
#                        "", "", "",
#                        "X", "X", "X"]
#         self.assertEqual(board.win_check(board.board), "X")
#
#     def test_vertical_one(self):
#         # "first column win condition"
#         board = tictactoe.Board()
#         board.board = ["O", "", "",
#                        "O", "", "",
#                        "O", "", ""]
#         self.assertEqual(board.win_check(board.board), "O")
#
#     def test_vertical_two(self):
#         # "second column win condition")
#         board = tictactoe.Board()
#         board.board = ["", "O", "",
#                        "", "O", "",
#                        "", "O", ""]
#         self.assertEqual(board.win_check(board.board), "O")
#
#     def test_vertical_three(self):
#         # "last column win condition")
#         board = tictactoe.Board()
#         board.board = ["", "", "O",
#                        "", "", "O",
#                        "", "", "O"]
#         self.assertEqual(board.win_check(board.board), "O")
#
#     def test_back_slash(self):
#         # "second column win condition")
#         board = tictactoe.Board()
#         board.board = ["O", "", "",
#                        "", "O", "",
#                        "", "", "O"]
#         self.assertEqual(board.win_check(board.board), "O")
#
#     def test_forward_slash(self):
#         # "last column win condition")
#         board = tictactoe.Board()
#         board.board = ["", "", "O",
#                        "", "O", "",
#                        "O", "", ""]
#         self.assertEqual(board.win_check(board.board), "O")
#
#     def test_fresh_board(self):
#         # "fresh board")
#         board = tictactoe.Board()
#
#         self.assertEqual(board.win_check(board.board), None)
#
#     def test_full_board(self):
#         # "full board")
#         board = tictactoe.Board()
#         board.board = ["X", "O", "O",
#                        "O", "X", "X",
#                        "O", "X", "O"]
#
#         self.assertEqual(board.win_check(board.board), None)


class T1_minimax_checks(unittest.TestCase):

    def test_horizontal_one(self):
        print("top row win condition")
        p1 = HardBot('X', 'O')
        board = ["X", "O", "O",
                 "O", "X", "X",
                 "", "", ""]
        # p1. get_move(board) == (8, "X")  (the next move should be to place an X in spot 8 (as it results in a win)
        # self.assertEqual(board.win_check(board.board), "X")

if __name__ == "__main__":
    unittest.main()
