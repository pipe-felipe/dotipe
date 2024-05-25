import platform
from os.path import expanduser
from tempfile import gettempdir

TOML_TEXT_BASE = "[user]\n" 'info = "Do not edit this [user] session"\n' f'os = "{platform.system()}"\n'
TOML_LOCATION = expanduser("~")
CONFIG_FILE_NAME = "dotipe.toml"
TEMP_DIR = gettempdir()

IGNORABLE_DIRS = (
    ".git",
    ".gitattributes",
    ".gitmodules",
    ".gitkeep",
    ".vscode",
    ".idea",
    ".DS_Store",
    ".gitlab-ci.yml",
    ".gitlab-ci.yml.example",
    ".gitlab-ci.yml.sample",
)


class Keys:
    SESSIONS = ("user", "wsl")
    URL_KEY = "raw_url"
    FILE_PATH_KEY = "file_path"
    NAME = "name"
