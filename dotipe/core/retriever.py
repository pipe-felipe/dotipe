from typing import Tuple

import requests

from dotipe.core.config_handler import DotipeConfigHandler


def make_request(url: str) -> Tuple[int, bytes]:
    """
    Makes a GET request to the provided URL and returns the status code and content.

    :param url: The URL to make the request to.
    :return: A tuple containing the status code and content of the response.
    """
    try:
        response = requests.get(url, stream=True)
        return response.status_code, response.content
    except requests.RequestException as e:
        print(f"An error occurred while making the request: {str(e)}")
        raise


def write_to_file(file_name: str, content: bytes) -> None:
    """
    Writes the provided content to a file with the provided name.

    :param file_name: The name of the file to write to.
    :param content: The content to write to the file.
    :return: The file object.
    """
    with open(file_name, "wb") as f:
        f.write(content)


class Retriever:
    def __init__(
        self,
        dotipe_config: DotipeConfigHandler,
        url_key: str,
        file_path_key: str,
        name: str,
    ) -> None:
        """
        Initializes the Retriever with the provided configuration and keys.

        :param dotipe_config: The configuration handler.
        :param url_key: The key for the URL in the configuration.
        :param file_path_key: The key for the file path in the configuration.
        :param name: The key for the file name in the configuration.
        """
        self.dotipe_config = dotipe_config
        self.url_key = url_key
        self.file_path_key = file_path_key
        self.name = name

    def get_session_data(self, session) -> Tuple[str, str, str]:
        """
        :return: A tuple containing the URL and file path.
        """
        try:
            toml_data = self.dotipe_config.retrieve_data_from_toml()
            if session not in toml_data:
                print(f"Error: section {session} not found in {self.dotipe_config.config_file_path}")
                raise KeyError

            retrieved_section = toml_data[session]
            url = retrieved_section[self.url_key]
            name = retrieved_section[self.name]
            file_path_name = f"{retrieved_section[self.file_path_key]}/" f"{retrieved_section[self.name]}"

            return url, name, file_path_name
        except KeyError as e:
            print(f"Error: key {str(e)} not found in {self.dotipe_config.config_file_path}")
            raise

    def retrieve_data(self, session, path_to_download) -> None:
        url, name, _ = self.get_session_data(session)
        try:
            status_code, content = make_request(url)
            if status_code == 200:
                write_to_file(f"{path_to_download}/{name}", content)
            else:
                print(f"Error: status code {status_code} received from {url}")
        except Exception as e:
            raise e
