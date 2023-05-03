# -*- coding: utf-8 -*-

"""Utilities for `mapp_metadata_checker`."""

import pandas as pd


def table_loader(table_path):
    """
    Load a table from a path and return it as a pandas DataFrame.

    :param table_path: The path to the table file.
    :type table_path: str
    :return: The loaded table as a pandas DataFrame.
    :rtype: pandas.DataFrame
    """
    df = pd.read_csv(table_path, sep=",", comment="#", dtype=str)
    return df


def headers_reader(table_path):
    """
    Load a table from a path and returns headers as a list.

    :param table_path: The path to the table file.
    :type table_path: str
    :return: The headers of the dataframe.
    :rtype: list
    """
    df = pd.read_csv(table_path, sep=",", comment="#", dtype=str)
    headers = df.columns.tolist()
    return headers
