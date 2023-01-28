def validate_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


def move(direct, steps):
    row = my_position[0] + (directions[direct][0] * steps)
    col = my_position[1] + (directions[direct][1] * steps)

    if validate_index(row, col) and (matrix[row][col] == "."):
        matrix[my_position[0]][my_position[1]] = "."
        matrix[row][col] = "A"
        return [row, col]
    return my_position


def shoot(direct):
    row, col = (my_position[0] + (directions[direct][0])), (my_position[1] + (directions[direct][1]))
    step_r, step_c = directions[direct]

    while validate_index(row, col):
        if matrix[row][col] == "x":
            matrix[row][col] = "."
            targets_list_met.append([row, col])
            break
        row += step_r
        col += step_c
    return targets_list_met


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

size = 5
matrix = [[x for x in input().split()] for _ in range(size)]

my_position = []
targets_list_met = []
count_of_all_targets = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            count_of_all_targets += 1

num_of_commands = int(input())

for _ in range(num_of_commands):
    command, *info = input().split()
    row, col = my_position

    if command == "move":
        direction, steps = info[0], int(info[1])
        my_position = move(direction, steps)

    elif command == "shoot":
        direction = info[0]
        shoot(direction)

    if len(targets_list_met) == count_of_all_targets:
        print(f'Training completed! All {count_of_all_targets} targets hit.')
        break
else:
    print(f'Training not completed! {abs(len(targets_list_met) - count_of_all_targets)} targets left.')

print(*targets_list_met, sep='\n')