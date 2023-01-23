# rows = int(input())
#
# matrix = []
# for _ in range(rows):
#     curr_matrix = [int(x) for x in input().split(", ")]
#     matrix.extend(curr_matrix)
#
# print(matrix)


rows = int(input())

matrix = []
for _ in range(rows):
    curr_matrix = [int(x) for x in input().split(", ")]
    matrix.append(curr_matrix)

result = []

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        result.append(matrix[row_index][col_index])
print(result)