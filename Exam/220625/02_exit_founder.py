from collections import deque

players = deque(input().split(", "))
resting_players = []
SIZE = 6
matrix = [[x for x in input().split()] for _ in range(SIZE)]

while True:
    player = players[0]
    row, col = [int(ch) for ch in input() if ch.isdigit()]

    current_move = matrix[row][col]
    if player not in resting_players:
        if current_move == "E":
            print(f'{player} found the Exit and wins the game!')
            break
        elif current_move == "T":
            print(f'{player} is out of the game! The winner is {players[1]}.')
            break
        elif current_move == "W":
            print(f'{player} hits a wall and needs to rest.')
            resting_players.append(player)
            players.rotate(1)
        else:
            players.rotate(1)
    else:
        players.rotate(1)
        resting_players.remove(player)




