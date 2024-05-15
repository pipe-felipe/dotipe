from os.path import expanduser

import requests

from dotipe.config_handler import DotipeConfig


def get_git_raw_remote_file_data(url, file_name):
    """ "
    Download a file from a remote git repository raw url
    """
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_name, "wb") as f:
                f.write(response.content)
    except requests.RequestException as e:
        raise e


class Retriever:
    def __init__(
        self,
        dotipe_config: DotipeConfig,
        section: str,
        url_key: str,
        file_path_key: str,
        file_name_key: str,
    ):
        self.dotipe_config = dotipe_config
        self.home_user_folder = expanduser("~")
        self.section = section
        self.url_key = url_key
        self.file_path_key = file_path_key
        self.file_name_key = file_name_key

    def get_from_remote(self):
        user_data = self.dotipe_config.retrieve_data_from_toml()
        section = user_data[self.section]
        try:
            url = section[self.url_key]
            file = (
                f"{self.home_user_folder}{user_data[self.section][self.file_path_key]}"
                f"{user_data[self.section][self.file_name_key]}"
            )
            get_git_raw_remote_file_data(url, file)
        except KeyError:
            print(f"Error: key not found in {self.dotipe_config.config_file_path}")
            raise
