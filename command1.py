import click

@click.group()
def test_name():
    pass

@test_name.command()
@click.option('--parameter-first', default='This is the default value',
              help='This is the help message for command 2)
def test(parameter_first):
    # Do something with the parameter
    click.echo(parameter_first)
