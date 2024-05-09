import platform

TOML_TEXT_BASE = (
    "[user]\n"
    'info = "Do not edit this [user] session"\n'
    f'os = "{platform.system()}"\n'
)


class Keys:
    SESSIONS = "wsl"
    URL_KEY = "raw_url"
    FILE_PATH_KEY = "file_path"
    FILE_NAME_KEY = "file_name"
