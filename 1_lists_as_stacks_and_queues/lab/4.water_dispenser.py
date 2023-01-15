from collections import deque

litters = int(input())
people = deque()

current_name = input()
while True:
    if current_name == "Start":
        break
    else:
        people.append(current_name)
    current_name = input()

water_needed = input()
while True:
    if water_needed.startswith("refill"):
        water_to_add = water_needed.split(" ")
        litters += int(water_to_add[1])
    elif water_needed == "End":
        print(f'{litters} liters left')
        break
    else:
        if litters >= int(water_needed):
            litters -= int(water_needed)
            print(f'{people.popleft()} got water')
        else:
            print(f'{people.popleft()} must wait')
    water_needed = input()
