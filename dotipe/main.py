from typing import Annotated
from typing import Optional

from typer import Typer, Option, Context

from dotipe.cli.dotipe import DotipeCli, get_version
from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import TOML_LOCATION

app = Typer()
config = DotipeConfigHandler(TOML_LOCATION)
dotipe = DotipeCli(config)


@app.callback(invoke_without_command=True)
def callback(
    ctx: Context,
    version: Annotated[Optional[bool], Option("--version", "-v", callback=get_version)] = None,
):
    if ctx.invoked_subcommand:
        return
    dotipe.start_message()


@app.command()
def ludo():
    print("branquinho")


@app.command()
def lud2o():
    print("branquinh2o")


if __name__ == "__main__":
    app()
