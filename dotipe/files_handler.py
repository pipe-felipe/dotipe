import difflib
from os import walk
from os.path import exists

from dotipe.core import IGNORABLE_DIRS


def compare_files(local_file: str, remote_raw: str) -> list[str]:
    if exists(local_file) and exists(remote_raw):
        with open(local_file, "r") as file1, open(remote_raw, "r") as file2:
            diff = difflib.unified_diff(
                file1.readlines(),
                file2.readlines(),
                fromfile=local_file,
                tofile=remote_raw,
            )

            return list(diff)
    else:
        raise FileNotFoundError("File not found")


def get_all_files_from_directory(directory: str, to_ignore=None) -> list[str]:
    """
    Get all files from a directory, if to_ignore is a string, it will ignore all files that contain the string
    to_ignore is the folder that should be ignored
    """
    all_files = []
    for _, _, files in walk(directory):
        for file in files:
            if not isinstance(to_ignore, list) or not any(
                ignore in file for ignore in to_ignore
            ):
                all_files.append(file)
    return sorted(all_files)


def __get_the_folder_items_difference(
    folder_items_local: list[str], folder_items_raw: list[str]
):
    local_set = set(folder_items_local)
    remote_set = set(folder_items_raw)
    return (
        set.difference(local_set, remote_set),
        set.difference(remote_set, local_set),
    )


def compare_files_from_folder(local_directory: str, remote_directory: str):
    """
    Compare all files from two directories
    """
    local_files = get_all_files_from_directory(local_directory, IGNORABLE_DIRS)
    remote_files = get_all_files_from_directory(remote_directory, IGNORABLE_DIRS)
    x = __get_the_folder_items_difference(local_files, remote_files)
    print(x)
