import difflib
from os import walk
from os.path import exists, join
from re import search

from dotipe.core import IGNORABLE_DIRS


def compare_files(local_file: str, remote_raw: str) -> list[str]:
    """ "
    This function compares two files and returns the difference between them
    If there is a difference, it will return a list with the difference
    This list has the length of 5, if the files are equal, the length will be 0
    """
    if exists(local_file) and exists(remote_raw):
        with open(local_file, "r") as local, open(remote_raw, "r") as raw:
            lines_local = local.readlines()
            lines_raw = raw.readlines()
            diff = difflib.unified_diff(
                lines_local,
                lines_raw,
                fromfile=local_file,
                tofile=remote_raw,
            )

            return list(diff)
    else:
        raise FileNotFoundError("File not found")


def get_all_files_from_directory(directory: str, project_name: str, to_ignore=None):
    """
    Get all files from a directory, if to_ignore is a string, it will ignore all files that contain the string
    to_ignore is the folder that should be ignored
    """
    all_files = []
    for root_folder, folder, files in walk(directory):
        for file in files:
            if not isinstance(to_ignore, list) or not any(
                ignore in file for ignore in to_ignore
            ):
                complete_path = join(root_folder, file)
                files_metadata = {
                    "complete_path": complete_path,
                    "file_name": file,
                    "relative_project_name_path": f"{project_name}{root_folder.split(project_name)[1]}/{file}",
                }
                all_files.append(files_metadata)
    return all_files


def __get_the_folder_items_difference(
    folder_items_local: list[str], folder_items_raw: list[str]
):
    local_set = set(folder_items_local)
    remote_set = set(folder_items_raw)
    return (
        set.difference(local_set, remote_set),
        set.difference(remote_set, local_set),
    )


def format_diff_between_files_string(diff_string):
    """ "
    This function formats the diff string to a more readable format
    output string example: (local:-1 raw:+1 diff_amount: 14)
    """
    pattern = r"^@@\s+-1(,\d+)?\s+\+1(,\d+)?\s+@@$"

    match = search(rf"{pattern}", diff_string)
    if match:
        diff_amounts = match.groups()
        local_diff = int(diff_amounts[0][1:]) if diff_amounts[0] else 0
        raw_diff = int(diff_amounts[1][1:]) if diff_amounts[1] else 0
        return {
            "local_subtitle": "-1",
            "raw_subtitle": "+1",
            "local_diff": local_diff,
            "raw_diff": raw_diff,
        }
    else:
        raise "No match found"


def compare_files_from_folder(local_directory: str, remote_directory: str):
    """
    Compare all files from two directories
    """
    local_files = get_all_files_from_directory(
        local_directory, "example_project", IGNORABLE_DIRS
    )
    remote_files = get_all_files_from_directory(
        remote_directory, "example_project", IGNORABLE_DIRS
    )

    diffs = {}

    for local_file in local_files:
        for remote_file in remote_files:
            if (
                remote_file["relative_project_name_path"]
                == local_file["relative_project_name_path"]
            ):
                print(
                    f"Comparing {local_file['complete_path']} with {remote_file['complete_path']}"
                )
                print(
                    f"Files: {local_file['file_name']} and {remote_file['file_name']}"
                )
                diff = compare_files(
                    local_file["complete_path"], remote_file["complete_path"]
                )
                if len(diff) > 0:
                    for i in range(len(diff)):
                        result = {
                            "file_local_content": diff[3],
                            "file_remote_content": diff[4],
                            "diff_numbers": format_diff_between_files_string(diff[2]),
                            "compared_file": local_file["relative_project_name_path"],
                        }
                        diffs[local_file["relative_project_name_path"]] = result
                else:
                    print("The file is equal")

    return diffs
