from os.path import abspath
import dotipe.dotipe_config as dtp

MOCK_HOME_FOLDER = f"{abspath("mock_home_folder")}/"
DOTIPE_CONFIG_MOCK = dtp.DotipeConfig(MOCK_HOME_FOLDER)
