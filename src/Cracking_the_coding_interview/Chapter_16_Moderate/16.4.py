# Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe.
from functools import reduce


def tic_tac_win(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    for col in range(len(board[0])):
        if len(set([row[col] for row in board])) == 1:
            return board[0][col]

    # diagonals
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]

    if len(set([board[len(board) - i - 1][i] for i in range(len(board))])) == 1:
        return board[len(board) - 1][0]
    return None


ttt_board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
print(tic_tac_win(ttt_board))
