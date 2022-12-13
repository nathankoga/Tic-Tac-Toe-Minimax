ROWS = 3
COLS = 3
MAX = 9  # Number of maximum moves


class Board:
    def __init__(self):
        self.turn = 0
        self.round = 0
        #  self.board = [[0 for row in range(ROWS)] for col in range(COLS)] # small enough board for 1D array
        self.board = [0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]

    def print(self):
        """ prints the rows"""
        for i in range(3):
            print(self.board[i*3:i*3+3])  # print slices of list by 3's

    def move(self, player: int, spot: int):
        # place a marker for the specified player
        if self.board[spot] == 0:
            if player == 1:
                self.board[spot] = 'X'
            else:  # player 2
                self.board[spot] = 'O'
            self.print()
        else:
            print('invalid move!')

    def win_check(self):
        for item in range(len(self.board)):
            if item != 0:  # if board index is not empty
                if item % 3 == 0:  # item is in left column, check for horizontal win
                    if self.board[item] == self.board[item+1] and self.board[item] == self.board[item+2]:
                        return True

                if item < 3:  # item is in first column, check for horizontal win
                    if self.board[item] == self.board[item+3] and self.board[item] == self.board[item+6]:
                        return True

                if item == 0:  # item is top left corner, check for diagonal win
                    if self.board[item] == self.board[item+4] and self.board[item] == self.board[item+8]:
                        return True

                if item == 2:  # item is top right corner, check for diagonal win
                    if self.board[item] == self.board[item+4] and self.board[item] == self.board[item+6]:
                        return True
            else:  # if none of these found a win
                return False




def main():
    # test board logic
    board = Board()
    # print(board.board)
    board.move(1, 0)

if __name__ == "__main__":
    main()
