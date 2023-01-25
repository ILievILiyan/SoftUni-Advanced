def happy_santa(gifts, nice_kids):
    for x, y in directions.values():
        r = santa_pos[0] + x
        c = santa_pos[1] + y

        if matrix[r][c].isalpha():
            if matrix[r][c] == "V":
                nice_kids += 1

            matrix[r][c] = "-"
            gifts -= 1

        if not gifts:
            break

    return gifts, nice_kids



directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

presents = int(input())
size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]

nice_kids = 0
santa_pos = []
nice_kids_with_present = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            santa_pos = [row, col]
            matrix[row][col] = "-"
        elif matrix[row][col] == "V":
            nice_kids += 1


command = input()
while command != "Christmas morning":

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
]
    house = matrix[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_with_present += 1
        presents -= 1

    elif house == "C":
        gifts, nice_kids_with_present = happy_santa(presents, nice_kids_with_present)

    matrix[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_with_present == nice_kids:
        break

    command = input()


if not presents:
    print("Santa ran out of presents!")


for x in matrix:
    print(*x)

if nice_kids == nice_kids_with_present:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {abs(nice_kids_with_present - nice_kids)} nice kid/s.')