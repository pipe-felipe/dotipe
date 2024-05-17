from rich.console import Console

from dotipe.core.config_handler import DotipeConfigHandler


class DotipeFacade:
    def __init__(self, dotipe_config: DotipeConfigHandler):
        self.console = Console()
        self.dotipe_config = dotipe_config

    def start_message(self):
        if not self.dotipe_config.file_exists():
            self.console.print("The configuration file did not exists :cry:\n", style="bold red")
            self.console.print("I will create a new one for you 😌", style="bold green")
