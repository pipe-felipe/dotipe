from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.facade.dotipe_facade import DotipeFacade


class DotipeCli(DotipeFacade):
    def __init__(self, dotipe_config: DotipeConfigHandler):
        super().__init__(dotipe_config)
