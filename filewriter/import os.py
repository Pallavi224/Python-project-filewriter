import os
from filewriter import write_to_file

# test_file_writer.py


def test_write_to_file_creates_file_and_writes_content(tmp_path):
    test_filename = tmp_path / "test_file.txt"
    test_content = "Hello, world!"
    write_to_file(str(test_filename), test_content)
    assert test_filename.exists()
    with open(test_filename, "r") as f:
        assert f.read() == test_content

def test_write_to_file_empty_content(tmp_path):
    test_filename = tmp_path / "empty.txt"
    test_content = ""
    write_to_file(str(test_filename), test_content)
    assert test_filename.exists()
    with open(test_filename, "r") as f:
        assert f.read() == test_content

def test_write_to_file_overwrites_existing_file(tmp_path):
    test_filename = tmp_path / "overwrite.txt"
    initial_content = "Initial"
    new_content = "Overwritten"
    write_to_file(str(test_filename), initial_content)
    write_to_file(str(test_filename), new_content)
    with open(test_filename, "r") as f:
        assert f.read() == new_content