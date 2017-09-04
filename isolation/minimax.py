from isolation.gs import *
from isolation.utils import *

def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """
    moves = gameState.get_legal_moves()
    if not moves:
        return None
    return max(moves, key=lambda move: min_value(gameState.forecast_move(move)))
