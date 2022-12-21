import unittest
import tictactoe


class T0_board_checks(unittest.TestCase):

    def test_horizontal_one(self):
        print("top row win condition")
        board = tictactoe.Board()
        board.board = [1, 1, 1,
                       "", "", "",
                       "", "", ""]
        self.assertEqual(board.win_check(board.board), 1)

    def test_horizontal_two(self):
        print("middle row win condition")
        board = tictactoe.Board()
        board.board = ["", "", "",
                       1, 1, 1,
                       "", "", ""]
        self.assertEqual(board.win_check(board.board), 1)

    def test_horizontal_three(self):
        print("bottom row win condition")
        board = tictactoe.Board()
        board.board = ["", "", "",
                       "", "", "",
                       1, 1, 1]
        self.assertEqual(board.win_check(board.board), 1)

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
        board.board = ["", 2, "",
                       "", 2, "",
                       "", 2, ""]
        self.assertEqual(board.win_check(board.board), 2)

    def test_vertical_three(self):
        print("last column win condition")
        board = tictactoe.Board()
        board.board = ["", "", 2,
                       "", "", 2,
                       "", "", 2]
        self.assertEqual(board.win_check(board.board), 2)

    def test_back_slash(self):
        print("second column win condition")
        board = tictactoe.Board()
        board.board = [2, "", "",
                       "", 2, "",
                       "", "", 2]
        self.assertEqual(board.win_check(board.board), 2)

    def test_forward_slash(self):
        print("last column win condition")
        board = tictactoe.Board()
        board.board = ["", "", 2,
                       "", 2, "",
                       2, "", ""]
        self.assertEqual(board.win_check(board.board), 2)

    def test_fresh_board(self):
        print("fresh board")
        board = tictactoe.Board()

        self.assertEqual(board.win_check(board.board), None)

    def test_full_board(self):
        print("full board")
        board = tictactoe.Board()
        board.board = [1, 2, 2,
                       2, 1, 1,
                       2, 1, 2]

        self.assertEqual(board.win_check(board.board), None)


class T1_minimax_checks(unittest.TestCase):

    def test_horizontal_one(self):
        print("top row win condition")
        board = tictactoe.Board()
        board.board = [1, 1, 1,
                       "", "", "",
                       "", "", ""]
        self.assertEqual(board.win_check(board.board), 1)

if __name__ == "__main__":
    unittest.main()
