from os.path import exists
from tomllib import load

from dotipe.core.consts import TOML_TEXT_BASE, CONFIG_FILE_NAME


class DotipeConfigHandler:
    def __init__(self, configuration_file_path):
        self.config_file_path = configuration_file_path
        self.config_file_name = CONFIG_FILE_NAME
        self.config_file = f"{self.config_file_path}/{self.config_file_name}"

    def retrieve_data_from_toml(self):
        if self.file_exists():
            with open(self.config_file, "rb") as toml_file:
                configuration = load(toml_file)
            return configuration
        else:
            return {}

    def get_sections(self):
        return self.retrieve_data_from_toml().keys()

    def file_exists(self):
        return exists(self.config_file)

    def create_file_if_not_exists(self):
        if not self.file_exists():
            with open(self.config_file, "w") as config_file:
                config_file.write(TOML_TEXT_BASE)
