size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]

start_alice_position = []
alice_tea = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "A":
            start_alice_position = [row, col]
            matrix[row][col] = "*"
            continue

row, col = start_alice_position
while alice_tea < 10:
    command = input()

    row_step, col_step = directions[command]
    row += row_step
    col += col_step

    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "R":
            matrix[row][col] = "*"
            break
        elif matrix[row][col].isdigit():
            alice_tea += int(matrix[row][col])
        matrix[row][col] = "*"
    else:
        break

if alice_tea >= 10:
    print(f'She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')

for x in matrix:
    print(*x)