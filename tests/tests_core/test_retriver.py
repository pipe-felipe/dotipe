from unittest.mock import patch

import pytest
import requests

from dotipe.core.config_handler import DotipeConfigHandler
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