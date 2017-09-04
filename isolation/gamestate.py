from copy import copy, deepcopy


class GameState:

    CLEAN = 0
    WIDTH = 3
    HEIGHT = 2
    # Block row 1, col 2, both starts at 0
    BLOCKED = [(2,1)]

    def print(self):
        print((self.state))
        print((self._player_locations))
        print((self._parity))

    def __init__(self):
        # init a clean board
        self.state = [GameState.CLEAN] * (GameState.WIDTH * GameState.HEIGHT)

        # block every box inside the blocked list
        for block in GameState.BLOCKED:
            self.state[block[0]+(GameState.WIDTH * block[1])] = 1

        self._parity = 0
        self._player_locations = [None, None]
        pass

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.)
        """
        loc = self._player_locations[self._parity]
        if not loc:
            return self._get_blank_spaces()
        moves = []

        # vectors base that I can multiply until reach to an end or to a block
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1),
                (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx, dy in directions:
            _x, _y = loc
            while 0 <= _x + dx < self.WIDTH and 0 <= _y + dy < self.HEIGHT:
                _x, _y = _x + dx, _y + dy
                if self.state[_x + _y*self.WIDTH]:
                    break
                moves.append((_x, _y))
        print(moves)
        return moves

    def _get_blank_spaces(self):
        """ Return a list of blank spaces on the board."""
        return [(x, y) for y in range(self.HEIGHT) for x in range(self.WIDTH)
                if self.state[x + self.WIDTH * y] == 0]

    def copy(self):
        """ Returns: a copy of the current game status """
        new_board = deepcopy(self)
        return new_board

    def move(self, move):
        """Move the active player to a specified location.

        Parameters
        ----------
        move : (int, int)
            A coordinate pair (row, column) indicating the next position for
            the active player on the board.
        """

        position = move[0] + move[1] * self.WIDTH
        self.state[position] = 1

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")
        new_gamestate = self.copy()
        new_gamestate.move(move)
        new_gamestate._player_locations[self._parity] = move
        new_gamestate._parity ^= 1
        return new_gamestate
