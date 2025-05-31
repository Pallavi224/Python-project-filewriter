from filewriter import write_to_file

# test-file-writer.py


def test_file_writer(tmp_path):
    test_filename = tmp_path / "test_file_writer.txt"
    test_content = "This is a test content."

    write_to_file(str(test_filename), test_content)

    assert test_filename.exists(), "File was not created."
    with open(test_filename, "r") as f:
        content = f.read()
        assert content == test_content, "Content written to file does not match expected content."