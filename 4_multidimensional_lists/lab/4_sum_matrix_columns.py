rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

for column_index in range(cols):
    curr_sum = 0
    for row_index in range(rows):
        curr_sum += matrix[row_index][column_index]

    print(curr_sum)
