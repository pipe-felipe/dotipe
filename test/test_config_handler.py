from test.mocks import DOTIPE_CONFIG_MOCK


def test_should_read_the_file_even_if_not_exists_creating_it():
    assert DOTIPE_CONFIG_MOCK.retrieve_data_from_toml()


def test_file_exists_returns_false_for_non_existent_file():
    DOTIPE_CONFIG_MOCK.config_file = "dont_exist.toml"
    assert not DOTIPE_CONFIG_MOCK.file_exists()


def test_file_exists_returns_true_for_existent_file():
    assert DOTIPE_CONFIG_MOCK.file_exists()
