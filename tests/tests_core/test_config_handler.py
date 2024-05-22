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
    toml_content = """
    [user]
    info = "Do not edit this [user] session"
    os = "Linux"
    """
    with open(config.config_file, "w") as f:
        f.write(toml_content)
    expected = True
    actual = config.file_exists()
    assert expected == actual
    remove(config.config_file)


def test_should_create_a_file_if_it_does_not_exists():
    config = DotipeConfigHandler(f"{MOCKED_HOME_FOLDER}/tmp")
    expected = False
    actual = exists(config.config_file)
    assert expected == actual

    config.create_file_if_not_exists()
    expected = True
    actual = exists(config.config_file)
    assert expected == actual

    with open(config.config_file, "r") as f:
        expected = TOML_TEXT_BASE
        actual = f.read()
        assert actual == expected

    remove(config.config_file)


def test_retrieve_data_from_toml():
    config = DotipeConfigHandler(MOCKED_HOME_FOLDER)
    toml_content = """
    [user]
    info = "Do not edit this [user] session"
    os = "Linux"
    """
    with open(config.config_file, "w") as f:
        f.write(toml_content)

    expected = {"user": {"info": "Do not edit this [user] session", "os": "Linux"}}
    actual = config.retrieve_data_from_toml()
    assert actual == expected
    remove(config.config_file)

    config.config_file = "dont_exist.toml"
    expected = {}
    actual = config.retrieve_data_from_toml()
    assert actual == expected
