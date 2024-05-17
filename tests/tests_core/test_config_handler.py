from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import TOML_TEXT_BASE
from tests.tests_core.mocks import MOCKED_HOME_FOLDER

from os.path import exists
from os import remove


def test_file_exists_should_returns_false_if_it_does_not_exists():
    config = DotipeConfigHandler(MOCKED_HOME_FOLDER)
    config.config_file = "dont_exist.toml"
    expected = False
    actual = config.file_exists()
    assert expected == actual


def test_file_exists_should_returns_true_if_it_exists():
    config = DotipeConfigHandler(MOCKED_HOME_FOLDER)
    expected = True
    actual = config.file_exists()
    assert expected == actual


def test_should_create_a_file_if_it_does_not_exists():
    config = DotipeConfigHandler(f"{MOCKED_HOME_FOLDER}/tmp")
    assert not exists(config.config_file)

    config.create_file_if_not_exists()
    assert exists(config.config_file)

    with open(config.config_file, "r") as f:
        content = f.read()
        assert content == TOML_TEXT_BASE

    remove(config.config_file)


def test_retrieve_data_from_toml():
    config = DotipeConfigHandler(MOCKED_HOME_FOLDER)
    test_data = """
    [user]
    info = "Do not edit this [user] session"
    os = "Linux"
    """
    with open(config.config_file, "w") as f:
        f.write(test_data)

    result = config.retrieve_data_from_toml()
    assert result == {"user": {"info": "Do not edit this [user] session", "os": "Linux"}}

    config.config_file = "dont_exist.toml"
    result = config.retrieve_data_from_toml()
    assert result == {}
