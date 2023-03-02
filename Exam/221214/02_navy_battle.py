def validate_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


def move(direct, hits, cruisers):
    row = submarine_position[0] + (directions[direct][0])
    col = submarine_position[1] + (directions[direct][1])

    if validate_index(row, col):
        matrix[submarine_position[0]][submarine_position[1]] = "-"
        if matrix[row][col] == "*":
            hits += 1
        elif matrix[row][col] == "C":
            cruisers -= 1
        matrix[row][col] = "-"

        return [row, col], hits, cruisers
    return submarine_position, hits, cruisers


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

size = int(input())

matrix = [[x for x in input()] for _ in range(size)]
submarine_position = []
bomb_hits = 0
cruisers_left = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            submarine_position = [row, col]
        elif matrix[row][col] == "C":
            cruisers_left += 1

while bomb_hits < 3 and cruisers_left:
    command = input()
    submarine_position, bomb_hits, cruisers_left = move(command, bomb_hits, cruisers_left)
    matrix[submarine_position[0]][submarine_position[1]] = "S"

    if bomb_hits == 3:
        print(f'Mission failed, U-9 disappeared! Last known coordinates {submarine_position}!')
        break
    elif cruisers_left == 0:
        print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
        break

for x in matrix:
    print(*x, sep="")