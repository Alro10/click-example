import click

@click.group()
def test2_name():
    pass

@test2_name.command()
@click.option('--parameter-second', default='This is the default value',
              help='This is the help message for command 2.')
def test2(parameter_second):
    # Do something with the parameter
    click.echo(parameter_second)
