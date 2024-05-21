from os import remove

import pytest
import requests

from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import Keys
from dotipe.core.retriever import make_request, Retriever
from tests.tests_core.mocks import MOCKED_HOME_FOLDER


def test_make_request_success(requests_mock):
    url = "https://test.com"
    mock_content = b"mock content"
    requests_mock.get(url, text=mock_content.decode())
    actual_status_code, actual_content = make_request(url)
    expected_status_code = 200
    assert actual_status_code == expected_status_code
    assert actual_content == mock_content


def test_make_request_404(requests_mock):
    url = "https://test.com"
    requests_mock.get(url, status_code=404)
    expected_status_code = 404
    actual_status_code, _ = make_request(url)
    assert actual_status_code == expected_status_code


def test_make_request_timout(requests_mock):
    url = "https://test.com"
    requests_mock.get(url, exc=requests.exceptions.ConnectTimeout)
    with pytest.raises(requests.RequestException):
        make_request(url)


def test__get_url_and_file():
    config = DotipeConfigHandler(f"{MOCKED_HOME_FOLDER}/tmp")

    toml_content = """
    [user]
    info = "Do not edit this [user] session"
    os = "Linux"
    
    [wsl]
    raw_url = "https://test.com"
    file_path = "something/else"
    file_name = "test.html"
    """
    with open(config.config_file, "w") as f:
        f.write(toml_content)

    retriever = Retriever(config, Keys.URL_KEY, Keys.FILE_PATH_KEY, Keys.FILE_NAME_KEY, Keys.SESSIONS[0])

    expected_url = "https://test.com"
    expected_file = "something/else/test.html"

    actual_url, actual_file = retriever._get_url_and_file()
    assert actual_url == expected_url
    assert actual_file == expected_file
    remove(config.config_file)
