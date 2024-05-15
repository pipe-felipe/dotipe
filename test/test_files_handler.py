from os.path import abspath

import pytest

from dotipe.core import IGNORABLE_DIRS
from dotipe.files_handler import (
    compare_files,
    get_all_files_from_directory,
    compare_files_from_folder,
    get_diff_between_files_metadata,
)


def test_compare_files_should_compare_two_files():
    file1 = f"{abspath("mock_home_folder")}/files_identical/file_test_1.txt"
    file2 = f"{abspath("mock_home_folder")}/files_identical/file_test_2.txt"
    # Act
    result = compare_files(file1, file2)
    for i in result:
        print(i)
    assert result == []


def test_compare_files_should_return_error_message_when_files_did_not_exist():
    file1 = "file1.txt"
    file2 = "file2.txt"
    # Act
    with pytest.raises(FileNotFoundError):
        compare_files(file1, file2)


def test_compare_files_should_return_the_diff_message_when_files_are_different():
    file1 = f"{abspath("mock_home_folder")}/files_different/file1.txt"
    file2 = f"{abspath("mock_home_folder")}/files_different/file2.txt"
    # Act
    result = compare_files(file1, file2)
    expected_diff = [
        "--- " "/home/pipe-ubuntu/Projects/dotipe/test/mock_home_folder/files_different/file1.txt\n",
        "+++ " "/home/pipe-ubuntu/Projects/dotipe/test/mock_home_folder/files_different/file2.txt\n",
        "@@ -1 +1 @@\n",
        "-other",
        "+one",
    ]
    assert result == expected_diff


def test_should_format_diff_between_files_string():
    diff_output = "@@ -1,5 +1,16 @@"
    # Act
    result = get_diff_between_files_metadata(diff_output)
    assert result["local_subtitle"] == "-1"
    assert result["raw_subtitle"] == "+1"
    assert result["local_diff"] == 5
    assert result["raw_diff"] == 16


def test_should_format_diff_between_files_if_local_did_not_have_any_diff():
    diff_output = "@@ -1 +1,16 @@"
    # Act
    result = get_diff_between_files_metadata(diff_output)
    assert result["local_subtitle"] == "-1"
    assert result["raw_subtitle"] == "+1"
    assert result["local_diff"] == 0
    assert result["raw_diff"] == 16


def test_should_format_diff_between_files_if_raw_did_not_have_any_diff():
    diff_output = "@@ -1,1 +1 @@"
    # Act
    result = get_diff_between_files_metadata(diff_output)
    assert result["local_subtitle"] == "-1"
    assert result["raw_subtitle"] == "+1"
    assert result["local_diff"] == 1
    assert result["raw_diff"] == 0


def test_should_format_diff_between_files_if_both_not_have_any_diff():
    diff_output = "@@ -1 +1 @@"
    # Act
    result = get_diff_between_files_metadata(diff_output)
    assert result["local_subtitle"] == "-1"
    assert result["raw_subtitle"] == "+1"
    assert result["local_diff"] == 0
    assert result["raw_diff"] == 0


def test_get_all_files_from_directory_should_return_all_files_from_a_directory():
    folder = f"{abspath("mock_home_folder")}/multiple"
    # Act
    result = get_all_files_from_directory(folder, "multiple", IGNORABLE_DIRS)
    assert result == [
        {
            "complete_path": f"{folder}/file_on_multiple_root",
            "file_name": "file_on_multiple_root",
            "relative_project_name_path": "multiple/file_on_multiple_root",
        },
        {
            "complete_path": f"{folder}/js/main.js",
            "file_name": "main.js",
            "relative_project_name_path": "multiple/js/main.js",
        },
        {
            "complete_path": f"{folder}/src/main.txt",
            "file_name": "main.txt",
            "relative_project_name_path": "multiple/src/main.txt",
        },
        {
            "complete_path": f"{folder}/ignore/ignored.json",
            "file_name": "ignored.json",
            "relative_project_name_path": "multiple/ignore/ignored.json",
        },
        {
            "complete_path": f"{folder}/tests/going_to_test.txt",
            "file_name": "going_to_test.txt",
            "relative_project_name_path": "multiple/tests/going_to_test.txt",
        },
    ]


def test_get_all_files_from_directory_should_return_empty_array_if_folder_dit_not_exists():
    folder = f"{abspath("mock_home_folder")}/multiples"
    # Act
    result = get_all_files_from_directory(folder, "multiples")
    assert result == []


def test_compare_files_from_folder_should_compare_two_folders():
    local_directory = f"{abspath("mock_home_folder")}/example_project"
    raw_remote_directory = f"{abspath("mock_home_folder")}/tmp/example_project"
    # Act
    result = compare_files_from_folder(local_directory, raw_remote_directory)
    assert result == {
        "example_project/src/x": {
            "compared_file": "example_project/src/x",
            "diff_numbers": {"local_diff": 2, "local_subtitle": "-1", "raw_diff": 0, "raw_subtitle": "+1"},
            "file_local_content": ["-felipe"],
            "file_remote_content": [],
        }
    }
