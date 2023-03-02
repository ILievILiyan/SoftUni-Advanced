def validate_index(row, col):
    if 0 <= row < size_matrix and 0 <= col < size_matrix:
        return True


def move(cmd, kilometers):
    car_is_finished = False

    row = car_coordinates[0] + directions[cmd][0]
    col = car_coordinates[1] + directions[cmd][1]

    if validate_index(row, col):
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
        if matrix[row][col] == ".":
            kilometers += 10
        elif matrix[row][col] == "T":
            matrix[row][col] = "."
            kilometers += 30

            current_tunnel = {(row, col)}
            second_tunnel = tunnels.difference(current_tunnel)
            row, col = second_tunnel.pop()

        elif matrix[row][col] == "F":
            kilometers += 10
            car_is_finished = True

        matrix[row][col] = "C"
        return [row, col], kilometers, car_is_finished

    return car_coordinates, kilometers, car_is_finished


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size_matrix = int(input())
car_num = input()
car_coordinates = [0, 0]
km_passed = 0

matrix = [[x for x in input().split()] for _ in range(size_matrix)]

tunnels = set()
for row in range(size_matrix):
    for col in range(size_matrix):
        if matrix[row][col] == "T":
            tunnels.add((row, col))

car_finished = False

while True:
    command = input()
    if command == "End":
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f'Racing car {car_num} DNF.')
        break

    car_coordinates, km_passed, car_finished = move(command, km_passed)

    if car_finished:
        print(f'Racing car {car_num} finished the stage!')
        break

print(f'Distance covered {km_passed} km.')
[print(*row, sep="") for row in matrix]