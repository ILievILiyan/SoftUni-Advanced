num = int(input())
matrix = []

for _ in range(num):
    curr_nums = [int(x) for x in input().split(", ")]
    matrix.append(curr_nums)

primary_diagonal = []
secondary_diagonal = []

for i in range(num):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][num-1])
    num -= 1

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')
