import random


class Player:
    def __init__(self, player_num):
        self.player = player_num  # i.e. player 1 if player_num = 1, else, 2

    def get_move(self, board: list):
        pass

    @staticmethod
    def possible_moves(board: list):
        move_list = []
        for spot in range(len(board)):  # iterate over indices to find each empty slot
            if not board[spot]:
                move_list.append(spot)
        return move_list


class HumanPlayer(Player):
    def __init__(self, player_num):
        super().__init__(player_num)

    def get_move(self, board: list):
        move = int(input(f"Player {self.player}, Make a move (Input a number 0~8): "))
        if not board[move]:
            return move, self.player  # return a tuple of where to place the symbol
        else:
            print("invalid move!")
            return


class EasyBot(Player):
    def __init__(self, player_num):
        super().__init__(player_num)

    def get_move(self, board: list):
        move_list = self.possible_moves(board)
        return random.choice(move_list)




