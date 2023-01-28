num = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(num)]

primary_diagonal = [matrix[i][i] for i in range(num)]
secondary_diagonal = [matrix[i][num-i-1] for i in range(num - 1, -1, -1)]

diagonal_difference = sum(primary_diagonal) - sum(secondary_diagonal)
print(abs(diagonal_difference))
