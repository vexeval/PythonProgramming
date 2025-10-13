with open("files/sample.txt", 'r') as file:
    content = file.readlines()

for line in content:
    print(line.rstrip())

with open("files/output.txt", 'w') as file:
    file.write('Hello, Christian.\n')
    file.writelines("['Line 1',\n 'Line 2']\n")

# Binary writing/reading
with open("files/example.bin", "wb") as fw:
    fw.write(b"This is binary data...")

with open("files/example.bin", "rb") as f:
    print(f.read()) # prints "b'This is binary data...'"


# with open(file_path, mode) as file_object:
#     content = file_object.read()

# read() reads entire file
# readline() reads one line
# readlines() reads all lines into a list
# `with` statement ensures proper file closing
# Modes:
# r: read;
# w: write;
# a: append;

# read/write binary files (e.g. images)
# Use binary modes for non-text files:
# rb
# wb
# ab