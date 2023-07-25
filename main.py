with open("my_file.txt", mode="r") as tam:
    contents = tam.read()
    print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("\nHookem Horns!")
