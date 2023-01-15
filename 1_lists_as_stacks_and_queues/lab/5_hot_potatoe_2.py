from collections import  deque

people = deque(input().split())
n = int(input())

counter = 0
while len(people) > 1:
    people.rotate(-n)
    print(f'Removed {people.pop()}')

print(f'Last is {people.pop()}')



