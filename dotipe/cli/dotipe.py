from importlib.metadata import version

from typer import Exit

from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.facade.dotipe import DotipeFacade


def get_version(value: bool):
    if value:
        print(f"Dotipe Version: {version("dotipe")}")
        raise Exit(code=0)


class DotipeCli(DotipeFacade):
    def __init__(self, dotipe_config: DotipeConfigHandler):
        super().__init__(dotipe_config)
