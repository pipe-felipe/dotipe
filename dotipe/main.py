from typing import Annotated
from typing import Optional

from typer import Typer, Option, Context

from dotipe.cli.dotipe import DotipeCli, get_version
from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import TOML_LOCATION, Keys
from dotipe.core.retriever import Retriever

app = Typer()
config = DotipeConfigHandler(TOML_LOCATION)
retriever = Retriever(config, Keys.URL_KEY, Keys.FILE_PATH_KEY, Keys.NAME)
dotipe = DotipeCli(config, retriever)


@app.callback(invoke_without_command=True)
def callback(
    ctx: Context,
    version: Annotated[Optional[bool], Option("--version", "-v", callback=get_version)] = None,
):
    if ctx.invoked_subcommand:
        return
    dotipe.start_message()


@app.command(help="Compare the files form a session")
def file_compare(session: Annotated[Optional[str], Option("--session", "-s")]):
    dotipe.retrieve_to_tmp(session)
    dotipe.compare(session)


if __name__ == "__main__":
    app()
