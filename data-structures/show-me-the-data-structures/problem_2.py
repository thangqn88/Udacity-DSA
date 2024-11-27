import os
import sys

def find_recursive(file_paths: list[str], suffix: str, path: str) -> list[str]:
    try:
        # Get list of files and directories in the current path
        files = os.listdir(path)
        # Iterate through each file/directory
        for file in files:
            # Get the full path of the file/directory
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path) and file.endswith(suffix):
                # Check if the path is a file and ends with the given suffix
                file_paths.append(full_path.replace("\\", "/"))
            elif os.path.isdir(full_path):
                # Check if the path is a directory
                # Recursively search the directory
                find_recursive(file_paths, suffix, full_path)
    except:
        print("Path does not exist")
        return


def find_files(suffix: str, path: str) -> list[str]:
    # Start the recursive search
    file_paths = []
    find_recursive(file_paths, suffix, path)
    return file_paths


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    assert result == ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2: Path does not exist
    print("Test Case 2: Path does not exist")
    result = find_files(".c", "./testdir/subdir0")
    assert result == []
    print(result)

    # Test Case 3: Path is a file ./testdir/t1.c
    print("Test Case 3: Path is a file")
    result = find_files(".c", "./testdir/t1.c")
    assert result == [] # Path is a file, not a directory
    print(result)
