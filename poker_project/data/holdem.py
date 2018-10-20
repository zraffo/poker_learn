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
