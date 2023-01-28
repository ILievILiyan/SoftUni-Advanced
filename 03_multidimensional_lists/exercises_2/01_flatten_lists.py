matrix = [x.split() for x in input().split("|")]

new_list = []

for row_index in range(len(matrix)-1, -1, -1):
    for col_index in range(len(matrix[row_index])):
        new_list.append(matrix[row_index][col_index])
print(*new_list)

# print(*[new_list[row] for row in range(len(new_list))], sep = " ")
#
# line = input().split("|")
# sub_lists = []
#
# for sub_string in line[::-1]:
#     sub_lists.extend(sub_string.split())
#
# print(*sub_lists)