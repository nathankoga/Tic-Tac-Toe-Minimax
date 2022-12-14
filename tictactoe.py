ROWS = 3
COLS = 3
MAX = 9  # Number of maximum moves


class Board:
    def __init__(self):
        self.turn = 0
        self.status = False
        #  self.board = [[0 for row in range(ROWS)] for col in range(COLS)] # small enough board for 1D array
        self.board = ["", "", "",
                      "", "", "",
                      "", "", ""]

    def print(self):
        """ prints the rows"""
        for i in range(3):
            print(self.board[i*3:i*3+3])  # print slices of list by 3's

    def move(self, player: int, spot: int):
        # place a marker for the specified player
        if not self.board[spot]:  # spot is empty string
            if player == 1:
                self.board[spot] = 'X'
            else:  # player 2
                self.board[spot] = 'O'
            self.turn += 1
            self.print()
        else:
            print('invalid move!')

    def win_check(self):
        for item in range(len(self.board)):
            if self.board[item]:  # if board index is not empty
                if item % 3 == 0:  # item is in left column, check for horizontal win
                    if self.board[item] == self.board[item+1] and self.board[item] == self.board[item+2]:
                        self.status = True
                        return

                if item < 3:  # item is in first column, check for horizontal win
                    if self.board[item] == self.board[item+3] and self.board[item] == self.board[item+6]:

                        return True

                if item == 0:  # item is top left corner, check for diagonal win
                    if self.board[item] == self.board[item+4] and self.board[item] == self.board[item+8]:
                        self.status = True
                        return

                if item == 2:  # item is top right corner, check for diagonal win
                    if self.board[item] == self.board[item+4] and self.board[item] == self.board[item+6]:
                        self.status = True
                        return
            else:  # if none of these found a win
                return False

    def score(self):  # returns an int representing the respective value a move has
        pass


def main():
    # test board logic
    board = Board()
    while not board.status:
        player = (board.turn % 2) + 1  # player 1 or player 2's turn
        spot = int(input(f"Player {player}, Make a move (Input a number 0~8): "))
        board.move(player, spot)
        board.win_check()

    # board.move(1, 0)

if __name__ == "__main__":
    main()
