# Method 1:

# Advantages:
# Control Over File Handling: You have explicit control over when the file is opened and closed,
# which can be useful in certain scenarios.
# Compatibility: This method works across different versions of Python,
# making it more widely applicable.

# Disadvantages:
# Error Handling: Requires explicit error handling (try/except/finally)
# to ensure the file is properly closed in case of exceptions.
# Verbose: Code is more verbose due to the need to explicitly handle opening and closing operations.

# file = open('file.txt')
#
# contents = file.read()
#
# print(contents)
#
# file.close()

# Method 2: Using with Keyword

# Mode = what operation we want to operate like
# w=Write(rewrite whole document and if file is not present then it will create new file),
# r=read (By default),
# a=append(will append to the existing file)

# Advantages:
# Automatic Cleanup: The with statement ensures that the file is properly closed
# after its suite finishes, even if an exception occurs.
# Simplicity: Code is more concise and readable without the need for explicit closing of the file.

# Disadvantages:
# Limited Use Cases: In some complex scenarios (like handling multiple
# files simultaneously or nested file operations), using with might not be as straightforward.

# with open('file.txt', mode='r') as file:
#     contents = file.read()
#     print(contents)

with open('file1.txt', mode='w') as file:
    file.write('New File Dinkar')
    print(file)

