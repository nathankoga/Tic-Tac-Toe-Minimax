ROWS = 3
COLS = 3
MAX = 9  # Number of maximum moves
# https://www.neverstopbuilding.com/blog/minimax


class Board:
    def __init__(self):
        self.turn = 1
        self.player = 1
        self.status = False
        #  self.board = [[0 for row in range(ROWS)] for col in range(COLS)] # small enough board for 1D array
        self.board = ["", "", "",
                      "", "", "",
                      "", "", ""]

    def print(self):
        """ prints the rows"""
        for i in range(3):
            #TODO: fix printing 1 and 2 to X and O
            print(self.board[i*3:i*3+3])  # print slices of list by 3's

    def move(self, spot: int):
        # place a marker for the specified player
        if not self.board[spot] and self.turn <= MAX:  # spot is empty string, and we have not reached max move number
            if self.player == 1:
                self.board[spot] = 1
            else:  # player 2
                self.board[spot] = 2
            self.player = self.turn % 2 + 1  # set the board's next player to correct number
            self.turn += 1
            self.print()

        else:
            print('invalid move!')

    @staticmethod
    def possible_move(board: list, spot: int, player: int):
        # place a marker for the specified player
        if not board[spot]:  # spot is empty string, and we have not reached max move number
            if player == 1:
                board[spot] = 1
            else:  # player 2
                board[spot] = 2
            return board
        else:
            return None  # no moves left

    @staticmethod
    def win_check(board):  # has to be generalized, so that logic can be used for potential boards for minimax
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

        else:  # none of these found a win
            return None

    def score(self, board, player):  # returns an int representing the respective value a potential board has

        if self.win_check(board) == player:
            return 10  # 10 points for the current player, as there is a win
        elif self.win_check(board):
            return -10  # win_check resulted in a win that didn't match the player, therefore, other player wins
        else:
            return 0  # no win

    def minimax(self, board, depth, max_player):  # max_player is a bool to determine min or max

        if self.win_check(board) or depth == 0:
            return self.score(board, self.player)

        scores = []  # the scores of each move
        move_indices = []  # the index that relates to the score
        # player = self.turn % 2 + 1

        for move in range(len(self.board)):
            if not self.board[move]:
                move_indices.append(move)
                scores.append(self.score(self.board, self.player))


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
