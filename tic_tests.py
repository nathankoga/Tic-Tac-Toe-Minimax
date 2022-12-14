import unittest
import tictactoe


class T0_board_checks(unittest.TestCase):

    def test_horizontal_one(self):
        print("top row win condition")
        board = tictactoe.Board()
        board.board = ["X", "X", "X",
                       "", "", "",
                       "", "", ""]
        self.assertEqual(board.win_check(board.board), "X")

    def test_horizontal_two(self):
        print("middle row win condition")
        board = tictactoe.Board()
        board.board = ["", "", "",
                       "X", "X", "X",
                       "", "", ""]
        self.assertEqual(board.win_check(board.board), "X")

    def test_horizontal_three(self):
        print("bottom row win condition")
        board = tictactoe.Board()
        board.board = ["", "", "",
                       "", "", "",
                       "X", "X", "X"]
        self.assertEqual(board.win_check(board.board), "X")

    def test_vertical_one(self):
        print("first column win condition")
        board = tictactoe.Board()
        board.board = ["X", "", "",
                       "X", "", "",
                       "X", "", ""]
        self.assertEqual(board.win_check(board.board), "X")

    def test_vertical_two(self):
        print("second column win condition")
        board = tictactoe.Board()
        board.board = ["", "O", "",
                       "", "O", "",
                       "", "O", ""]
        self.assertEqual(board.win_check(board.board), "O")

    def test_vertical_three(self):
        print("last column win condition")
        board = tictactoe.Board()
        board.board = ["", "", "O",
                       "", "", "O",
                       "", "", "O"]
        self.assertEqual(board.win_check(board.board), "O")

    def test_back_slash(self):
        print("second column win condition")
        board = tictactoe.Board()
        board.board = ["O", "", "",
                       "", "O", "",
                       "", "", "O"]
        self.assertEqual(board.win_check(board.board), "O")

    def test_forward_slash(self):
        print("last column win condition")
        board = tictactoe.Board()
        board.board = ["", "", "O",
                       "", "O", "",
                       "O", "", ""]
        self.assertEqual(board.win_check(board.board), "O")

    def test_fresh_board(self):
        print("fresh board")
        board = tictactoe.Board()

        self.assertEqual(board.win_check(board.board), None)

    def test_full_board(self):
        print("full board")
        board = tictactoe.Board()
        board.board = ["X", "O", "O",
                       "O", "X", "X",
                       "O", "X", "O"]

        self.assertEqual(board.win_check(board.board), None)


if __name__ == "__main__":
    unittest.main()
