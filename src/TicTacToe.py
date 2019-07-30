import random

class TicTacToe:

    def __init__(self):
        self.board = [['-']*3, ['-']*3, ['-']*3]


    def add_token(self, token, location):
        row, col = location
        self.board[row][col] = token

    def print_board(self):
        for row in range(len(self.board)):
            slot1, slot2, slot3 = self.board[row]
            print(slot1 + "|" + slot2 + "|" + slot3)
        print('\n')

    def is_full(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == '-':
                    return False
        return True

    def legal_AI_move(self):
        if self.is_full():
            raise Exception("Board is full. No legal moves.")

        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == '-':
                    return row, col

    def game_loop(self):
        while True:
            self.add_token("X", self.get_user_input())
            self.add_token("O", self.legal_AI_move())
            self.print_board()

    def get_user_input(self):
        print("What is your move?\n")
        row = int(input("Row?"))
        col = int(input("Col?"))
        return row, col

game = TicTacToe()
game.game_loop()