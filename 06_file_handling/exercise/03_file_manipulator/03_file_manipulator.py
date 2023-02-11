import os


def create_file(name):
    with open(f'{name}', "w") as file:
        file.write("")


def add_file(name, content):
    with open(f'{name}', "a") as file:
        file.write(f'{content}\n')


def replace_file(name, old_text, new_text):
    try:
        with open(f'{name}', "r") as file:
            text = file.readlines()

        for i in range(len(text)):
            text[i] = text[i].replace(old_text, new_text)

        with open(f'{name}', "w") as file:
            file.write("".join(text))

    except FileNotFoundError:
        print("An error occurred")


def delete_file(name):
    try:
        os.remove(name)
    except FileNotFoundError:
        print("An error occurred")


operation_dict = {
    "Create": lambda x: create_file(x),
    "Add": lambda x, y: add_file(x, y),
    "Replace": lambda x, y, z: replace_file(x, y, z),
    "Delete": lambda x: delete_file(x)
}


while True:
    command = input()
    if command == "End":
        break

    operation, file_name, *args = command.split("-")
    operation_dict[operation](file_name, *args)
