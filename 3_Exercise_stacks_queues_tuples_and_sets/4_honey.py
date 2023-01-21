from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0
operations_func = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y if x != 0 and y != 0 else 0,
    '/': lambda x, y: x / y if x != 0 and y != 0 else 0
}

while bees and nectar:
    first_bee = bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar < first_bee:
        bees.appendleft(first_bee)
    else:
        operation = symbols.popleft()
        total_honey += abs(operations_func[operation](first_bee, last_nectar))

print(f'Total honey made: {total_honey}')

if bees:
    print(f'Bees left: {", ".join(map(str,bees))}')
if nectar:
    print(f'Nectar left: {", ".join(map(str,nectar))}')
