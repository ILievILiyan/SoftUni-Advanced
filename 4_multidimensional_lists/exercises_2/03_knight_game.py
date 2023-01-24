def index_validity(row, col, size_matrix):
    return 0 <= row < size_matrix and 0 <= col < size_matrix


def is_knight(row, col, matrix):
    if matrix[row][col] == "K":
        return True


def get_attack_counter(row, col, matrix):
    result = 0
    if index_validity(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
        result += 1
    if index_validity(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result += 1
    if index_validity(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result += 1
    if index_validity(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    if index_validity(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    if index_validity(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1
    if index_validity(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result += 1
    if index_validity(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result += 1
    return result


size = int(input())
matrix = [[x for x in input()] for _ in range(size)]
removed_knight = 0

while True:
    knights_met = {}

    for row in range(size):
        for col in range(size):
            curr_position = matrix[row][col]
            if curr_position == "0":
                continue

            counter = get_attack_counter(row, col, matrix)
            if counter:
                knights_met[(row, col)] = counter

    if len(knights_met) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for coordinate, value in knights_met.items():
        if value > best_counter:
            best_counter = value
            knight_row = coordinate[0]
            knight_col = coordinate[1]

    matrix[knight_row][knight_col] = '0'
    removed_knight += 1

print(removed_knight)
