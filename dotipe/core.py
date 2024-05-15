import platform

TOML_TEXT_BASE = "[user]\n" 'info = "Do not edit this [user] session"\n' f'os = "{platform.system()}"\n'

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
    SESSIONS = "wsl"
    URL_KEY = "raw_url"
    FILE_PATH_KEY = "file_path"
    FILE_NAME_KEY = "file_name"
