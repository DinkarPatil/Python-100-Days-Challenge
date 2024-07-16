
# Absolute File Path:
# An absolute file path specifies the exact location of a file or directory
# starting from the root directory of the file system. It includes all directories
# from the root to the specific file or directory. In most operating systems
# (like Windows, macOS, Linux), the root directory is denoted by a special symbol,
# such as / (forward slash) in Unix-like systems or \ (backslash) in Windows.

# Method 1:
with open('/Users/Dinkar/Desktop/Dinkar.txt') as data:
    contents = data.read()
    print(contents)

# Method 2:
with open('../../Desktop/Dinkar.txt') as data:
    contents = data.read()
    print(contents)

# Relative File Path:
# A relative file path specifies the location of a file or directory relative
# to the current working directory (where the script or application is currently executing).
# Relative paths do not start from the root directory; instead,
# they indicate the file's position relative to the current location.

with open('file1.txt') as data:
    contents = data.read()
    print(contents)
