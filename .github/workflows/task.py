with open("file1.txt", "r") as file:
    text = file.read()

with open("file2.txt", "w") as file:
    file.write(text)

print("done!")