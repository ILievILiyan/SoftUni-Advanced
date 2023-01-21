from collections import deque

choco = deque(int(x) for x in input().split(", ") )
cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and cups and choco:
    current_choco = choco.pop()
    current_cup = cups.popleft()

    if current_cup <= 0 and current_choco <= 0:
        continue
    elif current_cup <= 0:
        choco.append(current_choco)
        continue
    elif current_choco <= 0:
        cups.appendleft(current_cup)
        continue

    if current_cup == current_choco:
        milkshakes += 1
    else:
        cups.append(current_cup)
        current_choco -= 5
        choco.append(current_choco)

if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print("Not enough milkshakes.")

print(f'Chocolate: {", ".join(map(str, choco)) or "empty"}')
print(f'Milk: {", ".join(map(str, cups)) or "empty"}')

