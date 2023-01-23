def check_validity_indexes(indexes):
    if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_cols):
        return True
    return False


def swap_indexes(command, indexes):
    if check_validity_indexes(indexes) and command == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*matrix[row]) for row in range(rows)]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    cmd, *info = [int(x) if x.isdigit() else x for x in input().split()]
    if cmd == "END":
        break
    swap_indexes(cmd, info)


