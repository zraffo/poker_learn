import pandas as pd
import glob
import os
from io import StringIO
import poker_project.data.holdem as holdem
import numpy as np

__f_sep__ = os.path.sep


def raw_data(path=''):
    """
    Open the raw data.
    :param: path: Path of the raw data.
    :return: File object with raw data.
    """
    pass


def prepare_data(raw_source='', target=''):
    """
    Prepare the dataset by creating a new cleaned dataset.
    :param raw_source: Path of the raw data.
    :param target: Target path to put the prepared data.
    :return:
    """
    pass


def prepare_holdem(type, numbers):
    """
    Prepare the hold'em dataset.
    :return: Dictionary of tables.
    """
    hf = os.path.join('data', 'IRCdata', type, 'holdem ' + str(numbers), '*', 'hdb')
    pf = os.path.join('data', 'IRCdata', type, 'holdem ' + str(numbers), '*', 'pdb', 'pdb.*')
    rf = os.path.join('data', 'IRCdata', type, 'holdem ' + str(numbers), '*', 'hroster')

    hands_f = glob.glob(hf)
    players_f = glob.glob(pf)
    roster_f = glob.glob(rf)

    roster_data = __roster_dict__(roster_f)
    hands_df = __hands_df__(hands_f)
    player_data = __player_df__(players_f)

    # dataset = {'hands': hands_df, 'players': player_data, 'roster': roster_data}
    return holdem.DataSet(roster_data, hands_df, player_data)


def __player_df__(player_dir):
    """
    Create a dictionary of players and dataframes of their hand history.

    :param player_dir: Directory (glob format)
    :return: dictionary
    """
    all_players = []
    for f in player_dir:
        with open(f, 'r') as f:
            lines = [x.split() for x in f.read().splitlines()]
            player_data = [p[0:13] + [None for lg in range(0, (13 - len(p)))] for p in lines]
            all_players.extend(player_data)

    all_players = np.array(all_players)
    pbt = pd.DataFrame(all_players, columns=['name', 'timestamp', 'dealt_num', 'pos', 'bet_preflop', 'bet_flop',
                                             'bet_turn', 'bet_river', 'bank_start', 'action', 'amt', 'card_1',
                                             'card_2'])
    pbt.loc[:, ['dealt_num', 'pos', 'bank_start', 'amt', 'action']] = \
        pbt.loc[:, ['dealt_num', 'pos', 'bank_start', 'amt', 'action']].apply(pd.to_numeric, downcast='unsigned')
    pbt['delta_s'] = np.sign(pbt['amt'] - pbt['action'])
    pbt['delta'] = (pbt['amt'] - pbt['action'])
    pbt['total_delta'] = pbt['delta'].cumsum()
    pbt = pbt.set_index(['name', 'timestamp'])
    return pbt


def __roster_dict__(roster_dir):
    """
    Create a dictionary of games and list of the players in them, with the number of players as the first element of
    each list.
    :param roster_dir: directory of roster files (glob)
    :return: dictionary
    """
    all_roster = []
    for roster in roster_dir:
        with open(roster, 'r') as f:
            all_roster.extend([x.split() for x in f.read().splitlines()])

    rdf = pd.DataFrame(all_roster)
    rdf = rdf.rename(columns={0: 'timestamp'})
    rdf['timestamp'] = rdf['timestamp'].apply(pd.to_numeric)
    rdf = rdf.set_index('timestamp')
    return rdf


def __hands_df__(hands_dir):
    """
    Return a dataframe of all the hands.

    :param hands_dir: directory of the hands (glob)
    :return: dataframe
    """
    all_hands = []
    for hand in hands_dir:
        with open(hand, 'r') as f:
            all_hands.extend(f.readlines())

    hands_s = StringIO("".join(all_hands).replace('/', ' '))
    hands_df = pd.read_table(hands_s,
                             delimiter=r"\s+",
                             engine='python',
                             names=['timestamp', 'game_num', 'hand_num', 'dealt_num',
                                    'num_flop', 'flop_pot', 'num_turn', 'turn_pot',
                                    'num_river', 'river_pot', 'num_showdown', 'showdown_pot',
                                    'card_1', 'card_2', 'card_3', 'card_4', 'card_5'])
    hands_df = hands_df.set_index('timestamp')#.drop('game_num')
    return hands_df
