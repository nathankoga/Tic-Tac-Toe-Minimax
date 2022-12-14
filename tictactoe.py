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

    def win_check(self, board):  # has to be generalized, so that logic can be used for potential boards for minimax
        for item in range(len(board)):
            if board[item]:  # if board index is not empty
                if item % 3 == 0:  # item is in left column, check for horizontal win
                    if board[item] == board[item+1] and board[item] == board[item+2]:
                        return board[item]  # we return board[item] so that we know which player wins

                if item < 3:  # item is in first column, check for horizontal win
                    if board[item] == board[item+3] and board[item] == board[item+6]:
                        return board[item]

                if item == 0:  # item is top left corner, check for diagonal win
                    if board[item] == board[item+4] and board[item] == board[item+8]:
                        return board[item]

                if item == 2:  # item is top right corner, check for diagonal win
                    if board[item] == board[item+2] and board[item] == board[item+4]:
                        return board[item]

        else:  # if none of these found a win
            return None

    def score(self, board, player):  # returns an int representing the respective value a potential board has
        if self.win_check(board) == player:
            return 10  # 10 points for the current player, as there is a win
        elif self.win_check(board):
            return -10  # win_check resulted in a win that didn't match the player, therefore, other player wins
        else:
            return 0  # no win


def main():
    # test board logic
    board = Board()
    while not board.status:
        player = (board.turn % 2) + 1  # player 1 or player 2's turn
        spot = int(input(f"Player {player}, Make a move (Input a number 0~8): "))
        board.move(player, spot)

        if board.win_check(board.board):
            board.status = True

    # board.move(1, 0)

if __name__ == "__main__":
    main()
