class WrongNumberOfPlayersError(Exception):
    """Raised when number of players is not two"""
    pass


class NoSuchStrategyError(Exception):
    """Raised when move is not correct"""
    pass


def rps_game_winner(moves):
    if len(moves) != 2:
        raise WrongNumberOfPlayersError('Number of players must be equal 2')

    allowed_moves = ('R', 'P', 'S')

    p1_move = moves[0][1]
    p2_move = moves[1][1]

    if p1_move not in allowed_moves or p2_move not in allowed_moves:
        raise NoSuchStrategyError('Moves must be "R", "S" or "P"')

    if p1_move == p2_move:
        return ' '.join(moves[0])

    if (p1_move, p2_move) in (('R', 'S'), ('S', 'P'), ('P', 'R')):
        return ' '.join(moves[0])

    return ' '.join(moves[1])
