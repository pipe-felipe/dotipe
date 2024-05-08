from tomllib import load
from os.path import exists

CONFIG_FILE_NAME = "dotipe.toml"


class Dotipe:
    def __init__(self, configuration_file_path):
        self.config_file_path = configuration_file_path
        self.config_file_name = CONFIG_FILE_NAME
        self.config_file = f"{self.config_file_path}{self.config_file_name}"

    def read_configuration_file(self):
        self.__create_file_if_not_exists()
        with open(self.config_file, "rb") as toml_file:
            configuration = load(toml_file)
        return configuration

    def __create_file_if_not_exists(self):
        if not exists(self.config_file):
            with open(self.config_file, "w") as config_file:
                config_file.write("[user]\n" 'test = "test"\n')
