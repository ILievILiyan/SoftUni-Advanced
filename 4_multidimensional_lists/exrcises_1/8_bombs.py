def detonation(row, col, damage):
    matrix[row][col] = 0
    for step_r, step_c in directions:
        r = row + step_r
        c = col + step_c

        if r in range(size) and c in range(size):
            if matrix[r][c] > 0:
                matrix[r][c] -= damage
    return matrix


directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

size = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(size)]
indexes = [[int(y) for y in x.split(",")] for x in input().split()]

for row, col in indexes:
    bomb = matrix[row][col]
    if bomb > 0:
        matrix = detonation(row, col, bomb)

cells_count = 0
sum_cells = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            cells_count += 1
            sum_cells += matrix[r][c]


print(f'Alive cells: {cells_count}')
print(f'Sum: {sum_cells}')

for x in matrix:
    print(*x)

