#William Murray
#017540586
"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = 0
    o_count = 0
    
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    # X goes first, so if counts are equal, it's X's turn
    # If X has more, it's O's turn
    if x_count <= o_count:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    # Check if action is valid
    if i not in [0, 1, 2] or j not in [0, 1, 2]:
        raise Exception("Invalid action: out of bounds")
    
    if board[i][j] != EMPTY:
        raise Exception("Invalid action: cell already occupied")
    
    # Create a deep copy of the board
    new_board = copy.deepcopy(board)
    
    # Determine whose turn it is and place their mark
    current_player = player(board)
    new_board[i][j] = current_player
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game is over if someone has won
    if winner(board) is not None:
        return True
    
    # Game is over if all cells are filled
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the board is terminal, return None
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X is maximizing player
        _, best_action = max_value(board)
        return best_action
    else:
        # O is minimizing player
        _, best_action = min_value(board)
        return best_action


def max_value(board):
    """
    Helper function for minimax: returns the maximum value and corresponding action.
    """
    if terminal(board):
        return utility(board), None
    
    alpha = -math.inf
    best_action = None
    
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > alpha:
            alpha = min_val
            best_action = action
    
    return v, best_action


def min_value(board):
    """
    Helper function for minimax: returns the alpha value and corresponding action.
    """
    if terminal(board):
        return utility(board), None
    
    beta = math.inf
    best_action = None
    
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < beta:
            beta = max_val
            best_action = action
    
    return beta, best_action