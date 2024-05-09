from os.path import abspath

import pytest
from dotipe.retriver import Retriever
from test.test_utils import DOTIPE_CONFIG_MOCK
from dotipe.utils import Keys
from dotipe.retriver import get_git_remote
from unittest import mock
from os import remove


def test_should_return_key_error_if_it_does_not_have_the_key_in_the_file():
    retriever = Retriever(
        DOTIPE_CONFIG_MOCK,
        "test_session_does_not_exist",
        Keys.URL_KEY,
        Keys.FILE_PATH_KEY,
        Keys.FILE_NAME_KEY,
    )
    with pytest.raises(KeyError):
        retriever.get_from_remote()


def test_git_remote_should_rise_error_when_url_not_found():
    with pytest.raises(Exception):
        get_git_remote("url_test", "")


def test_get_from_remote_should_download_file_correctly():
    test_file = f"{abspath("mock_home_folder")}/Downloads/test_file"

    retriever = Retriever(
        DOTIPE_CONFIG_MOCK,
        Keys.SESSIONS,
        Keys.URL_KEY,
        Keys.FILE_PATH_KEY,
        Keys.FILE_NAME_KEY,
    )

    with mock.patch("requests.get") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.content = b"file content"

        retriever.home_user_folder = f"{abspath("mock_home_folder")}"
        retriever.get_from_remote()

        with open(test_file, "rb") as f:
            file_content = f.read()

        assert file_content == b"file content"

    remove(test_file)
