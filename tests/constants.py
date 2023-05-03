# -*- coding: utf-8 -*-

"""Loading constants for the unit tests."""

import os

HERE = os.path.abspath(os.path.dirname(__file__))

DATA_DIR = os.path.join(HERE, "data")
CSV_TABLE_PATH = os.path.join(DATA_DIR, "test_table.csv")
TSV_TABLE_PATH = os.path.join(DATA_DIR, "test_table.tsv")
