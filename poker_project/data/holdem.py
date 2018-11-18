from collections import defaultdict
import pandas as pd

__actions_table__ = {
    "-": "na",
    "B": "blind bet",
    "f": "fold",
    "k": "check",
    "b": "bet",
    "c": "call",
    "r": "raise",
    "A": "all in",
    "Q": "quit",
    "K": "kicked"
}

# PHASES:
# 0 - preflop
# 1 - flop
# 2 - turn
# 3 - river
# 4 - showdown


class DataSet:

    def __init__(self, roster, hands, player):
        self.roster = roster
        self.hands = hands
        self.player = player

    def player_data(self, player_name, timestamp="all"):
        idxer = self.player.loc[player_name, :].loc
        if timestamp == "all":
            return idxer[:, :]
        else:
            return idxer[timestamp]

    def hand_info(self, timestamp):
        h = self.find_hand(timestamp)
        return {"timestamp": timestamp,
                "num_players": h.dealt_num,
                "end_phase": h['']}

    def find_hand(self, timestamp):
        return self.hands.query('timestamp == ' + timestamp)

    def hand_roster(self, timestamp):
        # return self.roster[timestamp]
        return self.roster.loc[timestamp, :].dropna().tolist()[1:]

    def find_hands_cards_shown(self):
        games_with_shown_hands = self.player.dropna(subset=['card_1', 'card_2'])
        # then look for timestamps in index of self.hands
        return games_with_shown_hands

    def game_history(self, timestamp):
        pass

    def action_series(self, player_name, timestamp):
        h = self.find_hand(timestamp)
        p_list = self.hand_roster(timestamp)
        # for player in p_list
        pass

    def player_details(self, timestamp):
        p_list = self.hand_roster(timestamp)[1:]
        p_actions = {player: self.player_data(player, timestamp) for player in p_list}
        return p_actions

    def turn_order(self, player_actions):
        p_seq = {p[1].player_position: p[0] for p in player_actions.items()}

    def phase_seq(self):
        return {"preflop": None, "flop": None, "turn": None, "river": None, "showdown": None}

    def align_actions(self, order):
        pass

    def winning_hands(self):
        chk = self.player.reset_index()
        chk = chk.dropna(subset=['amt', "delta", "card_1", "card_2"])
        chk['c1_val'] = chk['card_1'].apply(lambda x: x[0])
        chk['c1_suit'] = chk['card_1'].apply(lambda x: x[1])
        chk['c2_val'] = chk['card_2'].apply(lambda x: x[0])
        chk['c2_suit'] = chk['card_2'].apply(lambda x: x[1])
        chk = chk.drop('card_1', axis=1)
        chk = chk.drop('card_2', axis=1)
        return chk

    def parse_actions(self, action: str):
        ac = action.split()
        return ac
        # return [decode(act) for act in ac]

    def decode(self, action: str):
        pass
