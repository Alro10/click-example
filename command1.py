mport click

@click.group()
def feature_name():
    pass

@feature_name.command()
@click.option('--parameter_first', default='This is the default value',
              help='This is the help message for this parameter')
def command_feature(parameter_first):
    # Do something with the parameter
    click.echo(parameter_first)
