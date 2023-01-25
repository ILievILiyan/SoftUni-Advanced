size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

bunny_pos = []
best_path = []
best_dir = None
max_eggs = 0

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

for direction in directions:
    path = []
    collected_eggs = 0

    r = bunny_pos[0] + directions[direction][0]
    c = bunny_pos[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == 'X':
            break
        collected_eggs += matrix[r][c]
        path.append([r, c])

        r += directions[direction][0]
        c += directions[direction][1]

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_path = path
        best_dir = direction

print(best_dir)
print(*best_path, sep="\n")
print(max_eggs)