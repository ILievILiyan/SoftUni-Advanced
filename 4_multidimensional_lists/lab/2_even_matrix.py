even_matrix = []

for _ in range(int(input())):
    even_matrix.append([int(el) for el in input().split(", ") if int(el) % 2 == 0])

# not recommended:
# even_matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(int(input()))]

print(even_matrix)