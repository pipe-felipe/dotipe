from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import TOML_LOCATION
from dotipe.facade.dotipe_facade import DotipeFacade


class DotipeCli:
    def __init__(self):
        self.dotipe_config = DotipeConfigHandler(TOML_LOCATION)
        self.facade = DotipeFacade(self.dotipe_config)

    def start(self):
        self.facade.start_message()
