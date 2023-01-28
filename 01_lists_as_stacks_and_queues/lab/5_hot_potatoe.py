from collections import  deque

people = deque(input().split())
n = int(input())

counter = 0
while len(people) > 1:
    counter += 1
    if counter == n:
        print(f'Removed {people.popleft()}')
        counter = 0
    else:
        people.append(people.popleft())

print(f'Last is {people.pop()}')



