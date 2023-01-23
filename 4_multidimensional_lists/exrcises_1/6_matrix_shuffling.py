rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

while True:
    split_cmd = [int(x) if x.isdigit() else x for x in input().split()]
    if split_cmd[0] == "END":
        break
    elif split_cmd[0] == "swap" and len(split_cmd) == 5 and\
            0 <= split_cmd[1] < rows and\
            0 <= split_cmd[2] < cols and\
            0 <= split_cmd[3] < rows and\
            0 <= split_cmd[4] < cols:
        row1, col1, row2, col2  = split_cmd[1], split_cmd[2], split_cmd[3], split_cmd[4]

        matrix[row1][col1],matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*matrix[row]) for row in range(rows)]
    else:
        print("Invalid input!")
