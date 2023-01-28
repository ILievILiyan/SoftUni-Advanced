row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

max_sum = float("-inf")
max_matrix = []

for i in range(row-2):
    curr_sum = 0
    for j in range(col-2):
        curr_matrix = [
            [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
            [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
            [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
        ]

        curr_sum = sum(sum(x) for x in curr_matrix)
        if curr_sum >= max_sum:
            max_sum = curr_sum
            max_matrix = curr_matrix

print(f'Sum = {max_sum}')
for row in max_matrix:
    print(*row)