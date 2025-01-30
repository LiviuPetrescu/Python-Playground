# TEXT in the file: abc elephant cat dog
with open("write_file.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("write_file.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)
