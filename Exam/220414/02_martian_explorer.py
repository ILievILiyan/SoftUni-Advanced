directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

deposits_dictionary = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete"
}
available_deposits = set()
SIZE = 6
rover_coordinates = []

matrix = [[x for x in input().split()] for _ in range(SIZE)]
commands = [x for x in input().split(", ")]

for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == "E":
            rover_coordinates = [row, col]
            break

for command in commands:
    row = rover_coordinates[0] + directions[command][0]
    col = rover_coordinates[1] + directions[command][1]

    if row > SIZE - 1:
        row = 0
    if row < 0:
        row = SIZE - 1

    if col > SIZE - 1:
        col = 0
    if col < 0:
        col = SIZE - 1

    current_position = matrix[row][col]
    if current_position == "R":
        print(f"Rover got broken at ({row}, {col})")
        break
    elif current_position in deposits_dictionary.keys():
        available_deposits.add(deposits_dictionary[current_position])
        print(f"{deposits_dictionary[current_position]} deposit found at ({row}, {col})")
    rover_coordinates = [row, col]

if len(available_deposits) < 3:
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")