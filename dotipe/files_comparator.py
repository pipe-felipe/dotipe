import difflib
import os

from os import path


def compare_files(local_file: str, remote_raw: str) -> (str, bool):
    if path.exists(local_file) and path.exists(remote_raw):
        with open(local_file, "r") as file1, open(remote_raw, "r") as file2:
            diff = difflib.unified_diff(
                file1.readlines(),
                file2.readlines(),
                fromfile=local_file,
                tofile=remote_raw,
            )

            return "\n".join(diff), True
    else:
        return f"File not found {local_file} or {remote_raw}", False


def get_all_files(directory: str) -> list[str]:
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files
