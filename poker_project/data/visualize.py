import poker_project.data.holdem as hd
import pandas as pd
from matplotlib import pyplot as plt


def plot_player_action(dset: hd.DataSet, player_name):
    """
    Plot the action probabilities of the player given the game dataset.

    :param dset:            Hold'em DataSet to investigate
    :param player_name:     Name of the player to plot the history of.
    :return:                matplotlib axis
    """
    player_history = dset.player_data(player_name)
    pd.DataFrame.plot(y='amount_won')
