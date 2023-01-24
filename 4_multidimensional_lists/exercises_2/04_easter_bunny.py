size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

bunny_pos = []
best_path = []
best_dir = None
max_egs = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    for col in range(size):
        curr_position = matrix[row][col]

        if curr_position == "B":
            bunny_pos = [row, col]

for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]
    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break
        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

        if collected_eggs >= max_egs:
            max_egs = collected_eggs
            best_path = path
            best_dir = direction

print(best_dir)
print(*best_path,sep= "\n")
print(max_egs)

