def move(cmd, collected_coal):
    is_position_on_edge = False

    r = miner_position[0] + directions[cmd][0]
    c = miner_position[1] + directions[cmd][1]

    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "c":
            collected_coal += 1
        elif matrix[r][c] == "e":
            is_position_on_edge = True

        matrix[r][c] = "s"
        matrix[miner_position[0]][miner_position[1]] = "*"
        return [r, c], collected_coal, is_position_on_edge

    return [miner_position[0], miner_position[1]], collected_coal, is_position_on_edge


size = int(input())
possible_commands = ["left", "right", "up", "down"]
commands = [x if x in possible_commands else None for x in input().split()]

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

miner_position = []
coals = 0
total_coal = 0
position_on_edge = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            miner_position = [row, col]
        elif matrix[row][col] == "c":
            total_coal += 1

for command in commands:
    miner_position, coals, position_on_edge = move(command, coals)

    if coals == total_coal:
        print(f'You collected all coal! ({miner_position[0]}, {miner_position[1]})')
        break

    if position_on_edge:
        print(f'Game over! ({miner_position[0]}, {miner_position[1]})')
        break
else:
    print(f'{abs(total_coal-coals)} pieces of coal left. ({miner_position[0]}, {miner_position[1]})')