import pandas as pd

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


def won(df):
    return df[df > 0]


def lost(df):
    return df[df < 0]


def tie(df):
    return df[df == 0]


def stats(df):
    w = won(df['delta'])
    l = lost(df['delta'])
    t = tie(df['delta'])
    pm = df['delta'].mean()
    pc = df['delta'].count()
    pwc = w.count()
    pwm = w.mean()
    pwr = pwc / pc
    plc = l.count()
    plm = l.mean()
    plr = plc / pc
    ptm = t.mean()
    ptc = t.count()
    ptr = ptc / pc
    pev = (pwr * pwm) + (plr * plm)
    #st = df['stack_perc'].mean()
    ret = {'ev': [pm],
           'count': [pc],
           'won': [pwc],
           'avg win': [pwm],
           'winrate': [pwr],
           'lost': [plc],
           'avg lost': [plm],
           'lossrate': [plr],
           'tie': [plc],
           'avg tie': [plm],
           'tierate': [plr]}
    return pd.DataFrame(ret)
