import os
from filewriter import write_to_file

def test_file_writer():
    # create a temporary file
    test_filename = 'test_file_writer.txt'
    test_content = 'This is a test content.'

    write_to_file(test_filename, test_content)

    assert os.path.exists(test_filename), "File was not created."
    with open(test_filename, 'r') as f:
        content = f.read()
        assert content == test_content, "Content written to file does not match expected content."
        # Clean up the test file after the test runs
       # os.remove(test_filename)
        