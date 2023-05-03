# -*- coding: utf-8 -*-

"""Trivial version test."""

import unittest

from mapp_metadata_checker.version import get_version


class TestVersion(unittest.TestCase):
    """Trivially test a version."""

    def test_version_type(self):
        """Test the version is a string.

        This is only meant to be an example test.
        """
        version = get_version()
        self.assertIsInstance(version, str)
