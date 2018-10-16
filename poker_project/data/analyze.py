def filter_games(num_players=0, player_name="", cards_shown=False, hole_cards=(), cards_dealt=None, game_stage='a',
                 pot_size=-1):
    """
    Filter the game dataset by the given parameters.

    :param num_players:     Number of players in the hand.
    :param player_name:     Name of the player to find games for.
    :param cards_shown:     If any cards were shown.
    :param hole_cards:      Filter by specific hole cards.
    :param cards_dealt:     Filter by specific cards that appeared in the hand.
    :param game_stage:      Filter by stage of the game.
    :param pot_size:        Size of the pot.
    :return: dictionary
    """
    pass


def filter_player(player_name='', won=True, lost=True, cards_shown=True, hole_cards=(), cards_dealt=None, pot_size=-1):
    """
    Filter games by player information.

    :param player_name:     Name of the player.
    :param won:             Only show won games.
    :param lost:            Only show lost games.
    :param cards_shown:     Only show games where player showed cards.
    :param hole_cards:      Filter by specific hole cards.
    :param cards_dealt:     Filter by specific cards that appeared.
    :param pot_size:        Filter by pot size.
    :return: dictionary
    """
    pass
