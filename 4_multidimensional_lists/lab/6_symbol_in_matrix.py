len_of_square_matrix = int(input())

matrix = []
for _ in range(len_of_square_matrix):
    curr_row = [x for x in input()]
    matrix.append(curr_row)

symbol = input()

symbol_exist = False
for i in range(len_of_square_matrix):
    for j in range(len_of_square_matrix):
        if matrix[i][j] == symbol:
            print(f'({i}, {j})')
            symbol_exist = True
            break
    if symbol_exist:
        break

if not symbol_exist:
    print(f'{symbol} does not occur in the matrix')