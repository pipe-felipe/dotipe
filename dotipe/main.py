import typer

from dotipe.cli.dotipe_cli import DotipeCli
from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import TOML_LOCATION

config = DotipeConfigHandler(TOML_LOCATION)
dotipe_cli = DotipeCli(config)
typer_cli = typer.Typer()


@typer_cli.command()
def main():
    dotipe_cli.start_message()


if __name__ == "__main__":
    main()
