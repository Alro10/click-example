import click

from command1 import feature_name

commands = click.CommandCollection(sources=[feature_name])


def cli():
    commands()
