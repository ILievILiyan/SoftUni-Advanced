def new_position_validation(current_position, direct):
    row = current_position[0] + directions[direct][0]
    col = current_position[1] + directions[direct][1]
    if 0 <= row < SIZE and 0 <= col < SIZE:
        return [row, col]

    return current_position


def create(current_position, direct, new_value):
    row, col = new_position_validation(current_position, direct)
    if matrix[row][col] == ".":
        matrix[row][col] = new_value

    return [row, col]



def update(current_position, direct, new_value):
    row, col = new_position_validation(current_position, direct)
    if matrix[row][col].isalpha() or matrix[row][col].isdigit():
        matrix[row][col] = new_value
    return [row, col]


def delete(current_position, direct):
    row, col = new_position_validation(current_position, direct)
    if matrix[row][col].isalpha() or matrix[row][col].isdigit():
        matrix[row][col] = "."
    return [row, col]


def read(current_position, direct):
    row, col = new_position_validation(current_position, direct)
    if matrix[row][col].isalpha() or matrix[row][col].isdigit():
        print(matrix[row][col])
    return [row, col]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

SIZE = 6
matrix = [[x for x in input().split()] for _ in range(SIZE)]

position = []
for x in input():
    if x.isdigit():
        position.append(int(x))

while True:
    command = input()
    if command == "Stop":
        for x in matrix:
            print(*x)
        break

    operation, direction, *value = command.split(", ")

    if operation == "Create":
        position = create(position, direction, *value)
    elif operation == "Update":
        position = update(position, direction, *value)
    elif operation == "Delete":
        position = delete(position, direction)
    elif operation == "Read":
        position = read(position, direction)

# operations = {
#     "Create": lambda i: create(current_position, direct, new_value)
# }
