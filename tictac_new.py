from player_types import HumanPlayer, EasyBot

ROWS = 3
COLS = 3
MAX = 9  # Number of maximum moves
# https://www.neverstopbuilding.com/blog/minimax


class Board:
    def __init__(self, first_player, second_player):
        self.turn = 0
        self.p1 = first_player
        self.p2 = second_player
        self.status = False
        self.board = ["", "", "",
                      "", "", "",
                      "", "", ""]

    def print_board(self):
        """ prints the rows"""
        for i in range(3):
            print(self.board[i*3:i*3+3])  # print slices of list by 3's

    def official_move(self, move: tuple):
        # place a marker for the specified player
        spot = move[0]
        player = move[1]
        self.board[spot] = player
        self.turn += 1
        self.print_board()
        if self.win_check(self.board):  # Automatically check for a win
            self.status = True

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


def main():  # test board logic
    # initialize players
    p1 = HumanPlayer('X')
    # p2 = EasyBot(1)
    p2 = HumanPlayer('O')

    # create board
    board = Board(p1, p2)

    while not board.status:
        if board.turn % 2 == 0:
            move = p1.get_move(board.board)
            board.official_move(move)
        else:
            move = p2.get_move(board.board)
            board.official_move(move)
    print("game over!")


if __name__ == "__main__":
    main()
