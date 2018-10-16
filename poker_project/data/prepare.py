import pandas as pd
import glob
import os


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
    f_sep = os.path.sep
    pdir = os.path.join('data', 'poker', 'nolimit', '*')
    hands_f = glob.glob(pdir + f_sep + 'hdb')
