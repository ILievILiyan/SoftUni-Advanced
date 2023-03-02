from collections import deque

all_seats = [x for x in input().split(", ")]

used_seats = []


first_nums = deque(int(x) for x in input().split(", "))
second_nums = deque(int(x) for x in input().split(", "))

rotations = 0

while first_nums and second_nums and rotations < 10 and len(used_seats) < 3:
    first = first_nums.popleft()
    second = second_nums.pop()
    char = chr(first + second)

    words = [str(first) + char, str(second) + char]

    for word in words:
        if word in all_seats and word not in used_seats:
            used_seats.append(word)
            break
        elif word in all_seats and word in used_seats:
            break
        else:
            first_nums.append(first)
            second_nums.appendleft(second)
    rotations += 1

print(f'Seat matches: {", ".join(used_seats)}')
print(f'Rotations count: {rotations}')

