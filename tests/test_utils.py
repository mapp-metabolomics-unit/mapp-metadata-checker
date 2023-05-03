# -*- coding: utf-8 -*-

"""Unit test for utilities of mapp_metadata_checker."""


import unittest

import pandas as pd

from mapp_metadata_checker.utils import headers_reader, table_loader, table_tsver
from tests.constants import CSV_TABLE_PATH, TSV_TABLE_PATH


class TestMappMetadataChecker(unittest.TestCase):
    """Unit test for utilities of mapp_metadata_checker."""

    def test_table_loader(self):
        """Test the table loader."""
        table = table_loader(CSV_TABLE_PATH)
        self.assertEqual(table.shape, (2, 2))

    def test_table_loader_headers(self):
        """Test that the headers are correctly read with the table."""
        table = table_loader(CSV_TABLE_PATH)
        self.assertEqual(table.columns.tolist(), ["header1", "header2"])

    def test_headers_reader(self):
        """Test that the headers are correctly read with headers reader."""
        headers = headers_reader(CSV_TABLE_PATH)
        self.assertEqual(headers, ["header1", "header2"])
        self.assertIn("header1", headers)

    def test_table_tsver(self):
        """Test that table_tsver reads and writes a file with tab separated headers."""
        # Call the function with the sample files
        table_tsver(CSV_TABLE_PATH, TSV_TABLE_PATH)
        # Check that the output file is a TSV file
        with open(TSV_TABLE_PATH, "r") as f:
            lines = f.readlines()
            self.assertTrue(lines[0].startswith("header1\theader2"))

    def test_table_tsver_dataframe(self):
        """Test that table_tsver reads and writes a TSV file with the expected values."""
        # Call the function with the sample files
        table_tsver(CSV_TABLE_PATH, TSV_TABLE_PATH)
        # Load the output file as a DataFrame
        df = pd.read_csv(TSV_TABLE_PATH, sep="\t", dtype=str)
        # Check that the DataFrame has the expected columns and values
        expected_df = pd.DataFrame({"header1": ["a", "b"], "header2": ["a_1", "b_1"]})
        pd.testing.assert_frame_equal(df, expected_df)
