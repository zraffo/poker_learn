import poker_project.data.holdem as hd
import pandas as pd
from matplotlib import pyplot as plt
import poker_project.data.analyze as az
import numpy as np


def plot_player_action(dset: hd.DataSet, player_name):
    """
    Plot the action probabilities of the player given the game dataset.

    :param dset:            Hold'em DataSet to investigate
    :param player_name:     Name of the player to plot the history of.
    :return:                matplotlib axis
    """
    player_history = dset.player_data(player_name)
    pd.DataFrame.plot(y='amount_won')


def plot_by(h: pd.DataFrame, feature):
    pairs = h.query('c1_val == c2_val')  # ['amt']
    not_pairs = h.query('c1_val != c2_val')  # ['amt']
    suited = h.query('c1_suit == c2_suit')  # ['amt']
    not_suited = h.query('c1_suit != c2_suit')  # ['amt']
    not_suited_not_pairs = h.query('(c1_suit != c2_suit) & (c1_val != c2_val)')  # ['amt']
    all_hands = h  # ['amt']

    p = az.stats(pairs)
    np = az.stats(not_pairs)
    s = az.stats(suited)
    ns = az.stats(not_suited)
    nsnp = az.stats(not_suited_not_pairs)
    a = az.stats(all_hands)

    st = [p, np, s, ns, nsnp, a]
    for df in st:
        print(df['count'])
    stdf = pd.concat(st)
    labels = ['Pair', 'No Pair', 'Suited', 'Offsuit', '*Offsuit', 'All Hands']
    stdf.index = pd.Index(labels)

    plt.clf()
    plt.style.use('ggplot')
    # ax.bar(height=winrate, x=labels)
    stdf.loc[:, [feature]].plot.bar()
    # stdf.loc[:, ["winrate", 'lossrate']].plot.bar()
    # hcs = hcg['delta'].apply(stats)
    # hcd = hcs.reset_index().rename(columns={'deal': 'Hand'}).drop('level_1', axis=1).sort_values('ev', ascending=False)
    # hcd.rename(columns={'ev': 'Expected Value'}, inplace=True)
    # hcd['count'] = (hcd['count'] - hcd['count'].min()) / (hcd['count'].max() - hcd['count'].min())
    # hcd['Expected Value'] = (hcd['Expected Value'] - hcd['Expected Value'].min()) / (hcd['Expected Value'].max() - hcd['Expected Value'].min())
    # hcd.plot.scatter(x='count', y='winrate')
    # ad.loc[:, ['c1_val', 'c1_suit', 'c2_val', 'c2_suit']] = ad[['c1_val', 'c1_suit', 'c2_val', 'c2_suit']].applymap(lambda x: ord(x))
    # hcd['count'].plot.normal()
    plt.show()
