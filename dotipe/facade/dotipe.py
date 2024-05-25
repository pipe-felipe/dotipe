from textwrap import dedent

from rich.console import Console
from rich.table import Table

from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import Keys


class DotipeFacade:
    def __init__(self, dotipe_config: DotipeConfigHandler):
        self.console = Console()
        self.dotipe_config = dotipe_config
        self.table = Table("Sessions Available")

    def start_message(self):
        if not self.dotipe_config.file_exists():
            self.console.print("\nThe configuration file did not exists :cry:\n", style="bold white on red")
            self.console.print("I will create a new one for you 😌\n", style="bold green")
            self.dotipe_config.create_file_if_not_exists()
        else:
            self.console.print("\nThe file Exists and is on:", style="bold black on white")
            self.console.print(f"Path: {self.dotipe_config.config_file} 😌 \n", style="bold green")

            for key in Keys.SESSIONS:
                self.table.add_row(key)

            self.console.print(self.table)
            self.console.print("You can add more sessions :smile: following this structure:", style="bold green")

            config_example = dedent(
                """
            \\[wsl]
            raw_url = /mnt/c/Users/your_user
            file_path = some_path/your_user/your_file.txt
            """
            )
            self.console.print(config_example, style="bold magenta")
            self.console.print(
                "You can use the --help flag to see the available commands :smile:\n", style="bold black on white"
            )
