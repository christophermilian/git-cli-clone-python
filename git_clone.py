"""Module to help build out the cli"""
import os
import click


@click.group()
def cli():
    """A Python Git Clone"""


@cli.command()
@click.option("-n", "--name", type=str, help="Name to greet", default="World")
def hello(name):
    """Print out a greeting with an input name"""
    click.echo(f"Hello {name}")


@cli.command()
@click.argument("folder", required=True)
def init(folder):
    """Create a new repository folder"""
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        click.echo(
            f"--warn-- Directory {folder} already exists. Cannot initialize local repo."
        )

    git_path = "./" + folder + "/.git"
    os.mkdir(git_path)
    file_array = ["HEAD", "config", "description"]
    folder_array = ["hooks", "info", "objects", "refs"]

    for filename in file_array:
        with open(os.path.join(git_path, filename), "x", encoding="utf-8") as fp:
            if filename == "HEAD":
                fp.write("ref: refs/heads/master")
            else:
                fp.write("")

    for foldername in folder_array:
        os.mkdir(git_path + "/" + foldername)

    click.echo(f"Initialized empty repository: {folder}")
