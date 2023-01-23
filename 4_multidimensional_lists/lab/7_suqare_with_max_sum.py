rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    matrix.append(nums)

max_sum_sub_matrix = 0
max_sub_matrix = []
for i in range(rows-1):
    for j in range(cols-1):
        sub_matrix = [[matrix[i][j], matrix[i][j+1]], [matrix[i+1][j], matrix[i+1][j+1]]]
        curr_sum = sum(sub_matrix[0]) + sum(sub_matrix[1])

        if curr_sum > max_sum_sub_matrix:
            max_sum_sub_matrix = curr_sum
            max_sub_matrix = sub_matrix

for submatrix in max_sub_matrix:
    print(*submatrix)
print(max_sum_sub_matrix)
