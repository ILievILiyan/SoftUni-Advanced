from collections import deque
cups_capacity = deque(int(x) for x in input().split())
bottles_capacity = deque(int(x) for x in input().split())

wasted_water = 0

while cups_capacity and bottles_capacity:
    current_cups = cups_capacity.popleft()
    current_bottle = bottles_capacity.pop()
    current_water_diff = current_bottle - current_cups

    if current_water_diff >= 0:
        wasted_water += current_water_diff
    else:
        current_cups -= current_bottle
        while current_cups > 0:
            current_bottle = bottles_capacity.pop()
            current_cups -= current_bottle
        else:
            wasted_water += -current_cups

if cups_capacity:
    all_cups = ' '.join([str(c) for c in cups_capacity])
    print(f'Cups: {all_cups}')
    print(f'Wasted litters of water: {wasted_water}')
else:
    outstanding_bottles = ' '.join([str(b) for b in bottles_capacity])
    print(f'Bottles: {outstanding_bottles}')
    print(f'Wasted litters of water: {wasted_water}')
