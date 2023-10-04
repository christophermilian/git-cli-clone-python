"""Module to help build out the cli"""
import click

@click.group()
def cli():
    """A Click group for multiple commands"""

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    """Print out a greeting with an input name"""
    click.echo(f'Hello {name}')
