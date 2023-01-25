size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

bunny_pos = []
best_path = []
best_dir = None
max_egs = 0

for row in range(size):
    for col in range(size):
        curr_position = matrix[row][col]

        if curr_position == "B":
            bunny_pos = [row, col]

for direction in directions:
    path = []
    current_eggs = 0

    row = bunny_pos[0] + directions[direction][0]
    col = bunny_pos[1] + directions[direction][1]

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break
        current_eggs += int(matrix[row][col])
        path.append([row, col])

        row += directions[direction][0]
        col += directions[direction][1]

    if current_eggs >= max_egs:
        max_egs = current_eggs
        best_path = path
        best_dir = direction

print(best_dir)
print(*best_path,sep= "\n")
print(max_egs)

