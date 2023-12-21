"""Modules to help build out the cli"""
from enum import Enum, unique
import os
import click


@unique
class TerminalColors(Enum):
    """Terminal color codes"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@click.group()
def cli():
    """A Python-based Git Clone"""


@cli.command()
@click.option("-n", "--name", type=str, help="Name to greet", default="World")
def hello(name):
    """Print out a greeting with an input name"""
    click.echo(f"Hello {name}")


@cli.command()
@click.argument("folder", required=True)
def init(folder):
    """Create a new repository FOLDER.
  
    FOLDER is name of the repository to create.
    """
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        click.echo(
            f"--warn-- Directory {folder} already exists. Cannot initialize repository."
        )

    git_path = "./" + folder + "/.git"
    os.mkdir(git_path)
    file_array = ["HEAD", "config", "description"]
    folder_array = ["hooks", "info", "objects", "refs"]

    for file_name in file_array:
        with open(os.path.join(git_path, file_name), "x", encoding="utf-8") as fp:
            if file_name == "HEAD":
                fp.write("ref: refs/heads/master")
            elif file_name == "description":
                fp.write("Unnamed repository; edit this file 'description' to name the repository.")
            else:
                fp.write("")
                fp.write("")

    for folder_name in folder_array:
        os.mkdir(git_path + "/" + folder_name)

    hint_message = [
        "Using 'master' as the name for the initial branch. This default branch name",
        "is subject to change. To configure the initial branch name to use in all",
        "of your new repositories, which will suppress this warning, call:", "",
        "  git config --global init.defaultBranch <name>", "",
        "Names commonly chosen instead of 'master' are 'main', 'trunk' and",
        "'development'. The just-created branch can be renamed via this command:", "",
        "  git branch -m <name>"]

    for line in hint_message:
        click.echo(f"{TerminalColors.WARNING.value}hint: {line} {TerminalColors.ENDC.value}")

    click.echo(f"Initialized empty Git repository in {folder}")
