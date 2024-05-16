from os.path import abspath

from dotipe.core.config_handler import DotipeConfigHandler

MOCK_HOME_FOLDER = f"{abspath("mock_home_folder")}/"
DOTIPE_CONFIG_MOCK = DotipeConfigHandler(MOCK_HOME_FOLDER)
