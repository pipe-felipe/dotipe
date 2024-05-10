import os.path
from os.path import abspath

from dotipe.files_comparator import compare_files, get_all_files_from_directory


def test_compare_files_should_compare_two_files():
    file1 = f"{abspath("mock_home_folder")}/files_identical/file_test_1.txt"
    file2 = f"{abspath("mock_home_folder")}/files_identical/file_test_2.txt"
    # Act
    result = compare_files(file1, file2)
    assert result == ("", True)


def test_compare_files_should_return_error_message_when_files_did_not_exist():
    file1 = "file1.txt"
    file2 = "file2.txt"
    # Act
    result = compare_files(file1, file2)
    assert result == ("File not found file1.txt or file2.txt", False)


def test_compare_files_should_return_the_diff_message_when_files_are_different():
    file1 = f"{abspath("mock_home_folder")}/files_different/file1.txt"
    file2 = f"{abspath("mock_home_folder")}/files_different/file2.txt"
    # Act
    result = compare_files(file1, file2)
    expected_diff = (
        f"--- {abspath("mock_home_folder")}/files_different/file1.txt\n\n+++ "
        f"{abspath("mock_home_folder")}/files_different/file2.txt\n\n@@ -1 +1 "
        "@@\n\n-other\n+one"
    )
    assert result == (expected_diff, True)


# def test_compare_files_on_folder_should_return_error_message_when_folders_did_not_exist():
#     folder1 = "folder1"
#     folder2 = "folder2"
#     # Act
#     result = compare_files_on_folder(folder1, folder2)
#     assert result == "Folder not found folder1 or folder2"
#
#
# def test_compare_files_on_folder_should_return_the_diff_message_when_files_are_different():
#     folder1 = f"{abspath("mock_home_folder")}/files_identical"
#     folder2 = f"{abspath("mock_home_folder")}/files_different"
#     # Act
#     result = compare_files_on_folder(folder1, folder2)
#     assert result == "Folder is empty"


def test_get_all_files_from_directory_should_return_all_files_from_a_directory():
    folder = f"{abspath("mock_home_folder")}/multiple"
    # Act
    result = get_all_files_from_directory(folder)
    assert result == [
        f"{abspath("mock_home_folder")}/multiple/file_on_multiple_root",
        f"{abspath("mock_home_folder")}/multiple/ignore/ignored.json",
        f"{abspath("mock_home_folder")}/multiple/js/main.js",
        f"{abspath("mock_home_folder")}/multiple/src/main.txt",
        f"{abspath("mock_home_folder")}/multiple/tests/going_to_test.txt",
    ]


def test_get_all_files_from_directory_should_return_empty_array_if_folder_dit_not_exists():
    folder = f"{abspath("mock_home_folder")}/multiples"
    # Act
    result = get_all_files_from_directory(folder)
    assert result == []


def test_get_all_files_should_skip_selected_folder():
    folder = f"{abspath("mock_home_folder")}/multiple"
    folder_to_ignore = "ignore"
    # Act
    result = get_all_files_from_directory(folder, folder_to_ignore)
    assert result == [
        f"{abspath("mock_home_folder")}/multiple/file_on_multiple_root",
        f"{abspath("mock_home_folder")}/multiple/js/main.js",
        f"{abspath("mock_home_folder")}/multiple/src/main.txt",
        f"{abspath("mock_home_folder")}/multiple/tests/going_to_test.txt",
    ]
