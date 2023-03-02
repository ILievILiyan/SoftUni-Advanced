from collections import deque


white_directions = {
    "left_up_diagonal": (-1, -1),
    "right_up_diagonal": (-1, 1),
}

black_directions = {
    "left_down_diagonal": (1, -1),
    "right_down_diagonal": (1, 1),
}

positions = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h"
}

def move(player, position):
    winner = False

    if player == "white":
        for diagonal, pos in white_directions.items():
            row = position[0] + pos[0]
            col = position[1] + pos[1]
            if 0 <= row < SIZE and 0 <= col < SIZE:
                if matrix[row][col] == "b":
                    position = [row, col]
                    winner = True
                    break
        row = position[0] - 1
        col = position[1]
        if row - 1 == 0:
            position = [row, col]
            winner = True
        else:
            if matrix[row][col] == "-":
                matrix[row][col] = "w"

    elif player == "black":
        for diagonal, pos in black_directions.items():
            row = position[0] + pos[0]
            col = position[1] + pos[1]
            if 0 <= row < SIZE and 0 <= col < SIZE:
                position = [row, col]
                if matrix[row][col] == "b":
                    winner = True
                    break
        if position[0] + 1 == 7:
            winner = True
        else:
            if matrix[position[0] + 1][position[1]] == "-":
                position = [position[0] + 1][position[1]]
                matrix[position[0] + 1][position[1]] = "w"

    return position, winner




SIZE = 8
matrix = [[x for x in input().split()] for _ in range(SIZE)]

white_pos = []
black_pos = []
players = deque(["black", "white"])

for row in range(SIZE):
    if "w" in matrix[row]:
        white_pos = [row, matrix[row].index("w")]
    if "b" in matrix[row]:
        black_pos = [row, matrix[row].index("b")]


while True:
    player = players.pop()

    if player == "white":
        white_pos, status = move(player, white_pos)
        if status:
            print(f'Game over! White win, capture on {positions[white_pos[1]]}{white_pos[0]}.')
            break

    elif player == "black":
        black_pos, status = move(player, white_pos)
        if status:
            print(f'Game over! White win, capture on {positions[black_pos[1]+1]}{black_pos[0]}.')
            break
    players.appendleft(player)


