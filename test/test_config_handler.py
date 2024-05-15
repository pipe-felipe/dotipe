from test.mocks import DOTIPE_CONFIG_MOCK


def test_should_read_the_file_even_if_not_exists_creating_it():
    assert DOTIPE_CONFIG_MOCK.retrieve_data_from_toml()
