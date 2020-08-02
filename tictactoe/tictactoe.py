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

    print(new_board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    print('TO AKI 3')

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    AI = player(board)

    best_move = set()

    #def teste(board):


    for x in range(3):
        for y in range(3):
            if board[x][y] == None:
                return (x, y)
