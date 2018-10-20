from collections import defaultdict

class DataSet:

    def __init__(self, roster, hands, player):
        self.roster = roster
        self.hands = hands
        self.player = player

    def player_data(self, player_name, timestamp=':,:'):
        idxer = self.player[player_name].loc
        if timestamp is str:
            return idxer[timestamp]
        else:
            return idxer[:, :]

    def find_hand(self, timestamp):
        return self.hands.query('timestamp == ' + timestamp)

    def hand_roster(self, timestamp):
        return self.roster[timestamp]

    def find_hands_cards_shown(self):
        games_with_shown_hands = defaultdict(lambda: 0)
        for p in self.player.items():
            chk = p[1][["card_1", "card_2"]].dropna()
            for ts in list(chk.index):
                games_with_shown_hands[ts] = games_with_shown_hands[ts] + 1
        return games_with_shown_hands



