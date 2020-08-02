"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    for matriz in board:
        for y in matriz:
            if y == X:
                x += 1
            elif y == O:
                o += 1
    if x == o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()

    for x in range(3):
        for y in range(3):
            if board[x][y] is None:
                action.add((x, y))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    x = action[0]
    y = action[1]

    new_board = copy.deepcopy(board)

    if new_board[x][y] is not None:
        raise NameError('Not Correct')
    else:
        new_board[x][y] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = [X, O]

    for x1 in range(2):
        player = players[x1]
        if (board[0][0] == player and board[0][1] == player and board[0][2] == player) or \
                (board[1][0] == player and board[1][1] == player and board[1][2] == player) or \
                (board[2][0] == player and board[2][1] == player and board[2][2] == player) or \
                (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
                (board[0][2] == player and board[1][1] == player and board[2][0] == player) or \
                (board[0][0] == player and board[1][0] == player and board[2][0] == player) or \
                (board[0][1] == player and board[1][1] == player and board[2][1] == player) or \
                (board[0][2] == player and board[1][2] == player and board[2][2] == player):
            return player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) is not None) or (None not in board[0] and None not in board[1] and None not in board[2]):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)

    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    player_now = player(board)

    possibilities = actions(board)
    highest_value = None
    move = None

    for possibilities in possibilities:
        board[possibilities[0]][possibilities[1]] = player_now
        value = best_move(board, player_now)
        board[possibilities[0]][possibilities[1]] = EMPTY

        if highest_value is None:
            highest_value = value
            move = possibilities
        elif player_now == X:
            if value > highest_value:
                highest_value = value
                move = possibilities
        elif player_now == O:
            if value < highest_value:
                highest_value = value
                move = possibilities
    return move


def best_move(board, player_now):
    won = winner(board)

    if terminal(board):
        if won == X:
            return 1
        elif won == O:
            return -1
        else:
            return 0

    if player_now == X:
        player_now = O
    else:
        player_now = X

    possibilities = actions(board)
    highest_value = None

    for possibilities in possibilities:
        board[possibilities[0]][possibilities[1]] = player_now
        value = best_move(board, player_now)
        board[possibilities[0]][possibilities[1]] = EMPTY
        if highest_value is None:
            highest_value = value
        elif player_now == X:
            if value > highest_value:
                highest_value = value
        elif player_now == O:
            if value < highest_value:
                highest_value = value

    return highest_value
