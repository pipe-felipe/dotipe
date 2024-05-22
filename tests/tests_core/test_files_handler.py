import pytest

from dotipe.core.files_handler import (
    compare_files,
    get_all_files_from_directory,
    extract_diff_metadata,
    compare_files_from_folder,
)
from tests.tests_core.mocks import MOCKED_HOME_FOLDER


def test_compare_files_should_return_empty_if_there_is_no_diff():
    home = MOCKED_HOME_FOLDER
    file_one = f"{home}/project_to_compare_one/identical"
    file_two = f"{home}/project_to_compare_two/identical"

    actual_diff_list = compare_files(file_one, file_two)
    expected_diff_list = []
    assert actual_diff_list == expected_diff_list


def test_compare_files_should_return_diff_if_there_is_diff():
    home = MOCKED_HOME_FOLDER
    file_one = f"{home}/project_to_compare_one/with_diff"
    file_two = f"{home}/project_to_compare_two/with_diff"

    actual_diff_list = compare_files(file_one, file_two)
    expected_diff_list = [
        "--- " f"{home}/project_to_compare_one/with_diff\n",
        "+++ " f"{home}/project_to_compare_two/with_diff\n",
        "@@ -1,3 +1,3 @@\n",
        " some\n",
        " data\n",
        "-two",
        "+with diff",
    ]
    assert actual_diff_list == expected_diff_list


def test_compare_files_should_rise_a_error_if_the_file_doest_exists():
    home = MOCKED_HOME_FOLDER
    file_one = f"{home}/project_to_compare_one/empty"
    file_two = f"{home}/project_to_compare_two/do_not_exits"

    with pytest.raises(FileNotFoundError):
        compare_files(file_one, file_two)


def test_get_all_files_from_directory():
    home = MOCKED_HOME_FOLDER
    project_dir = f"{home}/project_to_compare_one"
    project_name = "project_to_compare_one"

    expected = [
        {
            "complete_file_path": f"{home}/project_to_compare_one/with_diff",
            "file_name": "with_diff",
            "relative_path": "project_to_compare_one/with_diff",
        }
    ]

    actual_files_list = get_all_files_from_directory(project_dir, project_name, to_ignore=["identical"])
    assert actual_files_list == expected


def test_extract_diff_metadata():
    with pytest.raises(TypeError):
        extract_diff_metadata("x")

    string_tester = "@@ -1,3 +1,3 @@\n"

    expected = {"local_diff_amount": 3, "local_subtitle": "-1", "raw_diff_amount": 3, "raw_subtitle": "+1"}
    actual_metadata = extract_diff_metadata(string_tester)
    assert actual_metadata == expected


def test_compare_files_from_folder():
    project_one = f"{MOCKED_HOME_FOLDER}/complete_test_project"
    project_two = f"{MOCKED_HOME_FOLDER}/tmp/complete_test_project"

    actual_diffs = compare_files_from_folder(project_two, project_one, "complete_test_project")
    expected = {
        "complete_test_project/src/my_module/module.py": {
            "compared_file": "complete_test_project/src/my_module/module.py",
            "diff_numbers": {
                "local_diff_amount": 0,
                "local_subtitle": "-1",
                "raw_diff_amount": 2,
                "raw_subtitle": "+1",
            },
            "file_local_content_changed": [],
            "file_remote_content_changed": ['+print("I ' "just " "changed " "my " 'module")\n'],
        }
    }
    assert actual_diffs == expected
