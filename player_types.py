import random


class Player:
    def __init__(self, player_id=None, opponent_id=None):
        self.player_id = player_id  # i.e. player's marker is X or O
        self.opponent_id = opponent_id

    def get_move(self, board: list):
        pass

    @staticmethod
    def possible_moves(board: list):
        move_list = []
        for spot in range(len(board)):  # iterate over indices to find each empty slot
            if board[spot] == '':  # only find empty strings, as 0 also counts as Null
                move_list.append(spot)
        return move_list

    def score(self, board: list, current_player: str):
        if self.win_check(board) == current_player:
            return 10  # 10 points for the current player
        elif self.win_check(board) != 'No Win':
            return -10  # -10 points, because win_check implies the other player wins
        else:
            return 0  # no win

    @staticmethod
    def win_check(board: list):  # has to be generalized, so that logic can be used for potential boards for minimax
        for item in range(len(board)):
            if board[item]:  # if board index is not empty
                if item % 3 == 0:  # item is in left column, check for horizontal win
                    if board[item] == board[item + 1] and board[item] == board[item + 2]:
                        return board[item]  # we return board[item] so that we know which player wins

                if item < 3:  # item is in first column, check for horizontal win
                    if board[item] == board[item + 3] and board[item] == board[item + 6]:
                        return board[item]

                if item == 0:  # item is top left corner, check for diagonal win
                    if board[item] == board[item + 4] and board[item] == board[item + 8]:
                        return board[item]

                if item == 2:  # item is top right corner, check for diagonal win
                    if board[item] == board[item + 2] and board[item] == board[item + 4]:
                        return board[item]
        if "" not in board:  # board is full
            return "No Win"

        else:  # none of these found a win
            return None


class HumanPlayer(Player):
    def __init__(self, player_id, opponent_id):
        super().__init__(player_id, opponent_id)

    def get_move(self, board: list):
        move = int(input(f"Player {self.player_id}, Make a move (Input a number 0~8): "))
        if board[move] == '':
            return move, self.player_id  # return a tuple of where to place the symbol
        else:
            print("invalid move!")
            return


class EasyBot(Player):
    def __init__(self, player_id, opponent_id):
        super().__init__(player_id, opponent_id)

    def get_move(self, board: list):
        move_list = self.possible_moves(board)
        return random.choice(move_list), self.player_id


class HardBot(Player):
    def __init__(self, player_id, opponent_id):
        super().__init__(player_id, opponent_id)

    @staticmethod
    def potential_board(board: list, move: int, player: str):
        board[move] = player
        return board

    def get_move(self, board: list):
        if board == ['', '', '', '', '', '', '', '', '']:
            move = 4  # if board is empty, simply move to the center
        else:
            move = self.minimax(board)
        return move, self.player_id

    def minimax(self, board: list, max_player: bool = True) -> int:
        # if max_player:
        #     curr_player = self.player_id
        # else:
        #     curr_player = self.opponent_id  # might be redundant, we may only need to understand the final score
        #  in terms of the maximizing player

        if self.win_check(board):
            return self.score(board, self.player_id)

        move_list = self.possible_moves(board)  # may need to use recursion to populate the next depth boards?
        score_list = []
        for potential_move in move_list:
            if max_player:  # if it's the maximizing player's turn
                # pass the minimax of each potential board which returns the score?
                moved_board = self.potential_board(board, potential_move, self.player_id)
                score_list.append(self.score(moved_board, self.player_id))
            else:
                pass





