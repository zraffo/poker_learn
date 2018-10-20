import pandas as pd
import glob
import os
from io import StringIO
from collections import defaultdict
import poker_project.data.holdem as holdem

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


def prepare_holdem():
    """
    Prepare the hold'em dataset.
    :return: Dictionary of tables.
    """
    hf = os.path.join('data', 'IRCdata', 'nolimit', '*', 'hdb')
    pf = os.path.join('data', 'IRCdata', 'nolimit', '*', 'pdb', 'pdb.*')
    rf = os.path.join('data', 'IRCdata', 'nolimit', '*', 'hroster')

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

    def __single_player__(player_dir):
        with open(player_dir, 'r') as f:
            lines = [x.split() for x in f.read().splitlines()]
            player_name = lines[0][0]
            player_data = [p[0:13] + [None for lg in range(0, (13 - len(p)))] for p in lines]
            player_data = {p[1]: p[2:] for p in player_data}

        pbt = pd.DataFrame.from_dict(player_data, orient='index')
        pbt.columns = ['players_dealt', 'player_position', 'bet_preflop', 'bet_flop',
                       'bet_turn', 'bet_river', 'bank_start', 'action', 'amount_won', 'card_1', 'card_2']
        return player_name, pbt

    pbt = pd.DataFrame(columns=['players_dealt', 'player_position', 'bet_preflop', 'bet_flop', 'bet_turn',
                                'bet_river', 'bank_start', 'action', 'amount_won', 'card_1', 'card_2'])
    all_players = defaultdict(lambda: pbt)
    for f in player_dir:
        p_data = __single_player__(f)
        all_players[p_data[0]] = all_players[p_data[0]].append(p_data[1])

    return all_players


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

    roster_data = {p[0]: p[1:] for p in all_roster}
    return roster_data


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
                             names=['timestamp', 'game_num', 'hand_num', 'num_players_dealt',
                                    'num_players_flop', 'flop_pot', 'num_players_turn', 'turn_pot',
                                    'num_players_river', 'river_pot', 'num_players_showdown', 'showdown_pot',
                                    'card_1', 'card_2', 'card_3', 'card_4', 'card_5'])
    return hands_df
