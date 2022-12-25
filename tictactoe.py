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
        self.winner = None
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
        result = self.p1.win_check(self.board)
        if result:  # Automatically check for a win
            self.status = True
            self.winner = result


def main():  # test board logic
    # initialize players
    # p1 = HumanPlayer('X')
    p1 = EasyBot('X', 'O')

    p2 = EasyBot('O', 'X')
    # p2 = HumanPlayer('O')

    # create board
    board = Board(p1, p2)

    while not board.status:
        if board.turn % 2 == 0:
            move = p1.get_move(board.board)
            board.official_move(move)
        else:
            move = p2.get_move(board.board)
            board.official_move(move)
    print(f"game over! {board.winner} wins!")


if __name__ == "__main__":
    main()
