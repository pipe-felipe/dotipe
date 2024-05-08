from os.path import abspath

import dotipe.dotipe as dtp


mock_home_folder = f"{abspath("mock_home_folder")}/"


def test_should_read_the_file_even_if_not_exists_creating_it():
    user_dotfiles = dtp.Dotipe(mock_home_folder)
    assert user_dotfiles.read_configuration_file()
