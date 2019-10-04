import click

from command1 import test1_name
from command2 import test2_name

commands = click.CommandCollection(sources=[test1_name, test2_name])


def cli():
    commands()
