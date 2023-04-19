def rps_game_winner(moves):
    if len(moves) != 2:
        raise Exception('WrongNumberOfPlayersError')

    allowed_moves = ('R', 'P', 'S')

    p1_move = moves[0][1]
    p2_move = moves[1][1]

    if p1_move not in allowed_moves or p2_move not in allowed_moves:
        raise Exception('NoSuchStrategyError')

    if p1_move == p2_move:
        return ' '.join(moves[0])

    if (p1_move, p2_move) in (('R', 'S'), ('S', 'P'), ('P', 'R')):
        return ' '.join(moves[0])

    return ' '.join(moves[1])
