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


def isFull(board):
    """
    Returns whether a board is full or not
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                return False
    return True


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]:
        return X
    else:
        x_count = 0
        o_count = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == X:
                    x_count += 1
                elif board[i][j] == O:
                    o_count += 1

        if x_count == 5 and o_count == 4:
            return

        if x_count > o_count:
            return O
        elif x_count == o_count:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if i > 2 or j > 2 or i < 0 or j < 0 or board[i][j] != EMPTY:
        raise Exception("Incorrect action fed")

    turn = player(board)

    b = copy.deepcopy(board)
    b[i][j] = turn

    return b


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == X and board[0][1] == X and board[0][2] == X:
        return X
    elif board[1][0] == X and board[1][1] == X and board[1][2] == X:
        return X
    elif board[2][0] == X and board[2][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    elif board[0][0] == O and board[0][1] == O and board[0][2] == O:
        return O
    elif board[1][0] == O and board[1][1] == O and board[1][2] == O:
        return O
    elif board[2][0] == O and board[2][1] == O and board[2][2] == O:
        return O
    elif board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return O
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O
    elif board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return O
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner_player = winner(board)

    if winner_player == X or winner_player == O:
        return True
    elif isFull(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def min_value(board):
    if terminal(board):
        return utility(board)

    v = 99999

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -99999

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        a = -99999
        max_move = ()
        for action in actions(board):
            tmp = max(a, min_value(result(board, action)))
            if tmp > a:
                a = tmp
                max_move = action
        return max_move

    elif player(board) == O:
        b = 99999
        min_move = ()
        for action in actions(board):
            tmp = min(b, max_value(result(board, action)))
            if tmp < b:
                b = tmp
                min_move = action
        return min_move
    else:
        return None
