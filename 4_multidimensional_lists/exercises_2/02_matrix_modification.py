def check_index_validity(data):
    row, col = int(data[0]), int(data[1])
    row_col_range = range(len(matrix))
    if {row, col}.issubset(row_col_range):
        return True
    print('Invalid coordinates')
    return False


def matrix_modification(command, data):
    if check_index_validity(data):
        row, col, value = [int(x) for x in data]
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value


num = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(num)]

while True:
    cmd, *info = input().split()
    if cmd == "END":
        break
    matrix_modification(cmd, info)

[print(*matrix[row]) for row in range(len(matrix))]
