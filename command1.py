import click

@click.group()
def test1_name():
    pass

@test1_name.command()
@click.option('--parameter-first', default='This is the default value',
              help='This is the help message for command 2)
def test1(parameter_first):
    # Do something with the parameter
    click.echo(parameter_first)
