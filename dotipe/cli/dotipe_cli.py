from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import TOML_LOCATION


class DotipeCli:
    def __init__(self):
        self.dotipe_config = DotipeConfigHandler(TOML_LOCATION)

    def start(self):
        pass
