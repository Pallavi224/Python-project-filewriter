def write_tofile(filename,content):
    """
    Write content to a file.
    
    :param filename: The name of the file to write to.
    :param content: The content to write to the file.
    """
    with open(filename, 'w') as f:
        f.write(content)

if __name__=="__main__":
    # Example usage
    write_tofile('example.txt', 'Hello, World!')
    print("Content written to example.txt")