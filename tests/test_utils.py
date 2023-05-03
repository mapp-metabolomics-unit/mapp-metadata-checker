# -*- coding: utf-8 -*-

"""Unit test for utilities of mapp_metadata_checker."""


import unittest

from mapp_metadata_checker.utils import headers_reader, table_loader
from tests.constants import DATA_TABLE_PATH


class TestMappMetadataChecker(unittest.TestCase):
    """Unit test for utilities of mapp_metadata_checker."""

    def test_table_loader(self):
        """Test the table loader."""
        table = table_loader(DATA_TABLE_PATH)
        self.assertEqual(table.shape, (2, 2))

    def test_table_loader_headers(self):
        """Test that the headers are correctly read with the table."""
        table = table_loader(DATA_TABLE_PATH)
        self.assertEqual(table.columns.tolist(), ["header1", "header2"])

    def test_headers_reader(self):
        """Test that the headers are correctly read with headers reader."""
        headers = headers_reader(DATA_TABLE_PATH)
        self.assertEqual(headers, ["header1", "header2"])
        self.assertIn("header1", headers)
