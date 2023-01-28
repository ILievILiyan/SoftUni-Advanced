row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

max_sum = float("-inf")
max_matrix = []

for i in range(row-2):
    curr_sum = 0
    for j in range(col-2):
        first_row = matrix[i][j:j+3]
        second_row = matrix[i+1][j:j+3]
        third_row = matrix[i+2][j:j+3]

        curr_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if curr_sum >= max_sum:
            max_sum = curr_sum
            max_matrix = [first_row, second_row, third_row]

print(f'Sum = {max_sum}')
[print(*max_matrix[row]) for row in range(3)]