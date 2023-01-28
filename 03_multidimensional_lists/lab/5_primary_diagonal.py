len_of_square_matrix = int(input())

matrix = []
for _ in range(len_of_square_matrix):
    curr_row = [int(x) for x in input().split()]
    matrix.append(curr_row)

diagonal_sum = 0
for row in range(len_of_square_matrix):
    diagonal_sum += matrix[row][row]
print(diagonal_sum)

