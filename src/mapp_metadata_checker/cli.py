# -*- coding: utf-8 -*-

"""Command line interface for :mod:`mapp_metadata_checker`.

Why does this file exist, and why not put this in ``__main__``? You might be tempted to import things from ``__main__``
later, but that will cause problems--the code will get executed twice:

- When you run ``python3 -m mapp_metadata_checker`` python will execute``__main__.py`` as a script.
  That means there won't be any ``mapp_metadata_checker.__main__`` in ``sys.modules``.
- When you import __main__ it will get executed again (as a module) because
  there's no ``mapp_metadata_checker.__main__`` in ``sys.modules``.

.. seealso:: https://click.palletsprojects.com/en/8.1.x/setuptools/#setuptools-integration
"""

import logging

import click

from .utils import table_tsver

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)


@click.group()
@click.version_option()
def main():
    """CLI for mapp_metadata_checker."""


@main.command(help=table_tsver.__doc__)
@click.argument("input_path")
@click.argument("output_path")
def tsver(input_path, output_path):
    table_tsver(input_path, output_path)


if __name__ == "__main__":
    main()
