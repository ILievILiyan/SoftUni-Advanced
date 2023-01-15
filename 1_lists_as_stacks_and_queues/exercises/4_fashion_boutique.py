from collections import deque
from copy import copy

box_clothes = [int(x) for x in input().split(" ")]
clothes = deque(box_clothes)
capacity = int(input())
capacity_restart = copy(capacity)

boxes = 1
while clothes:
    if capacity >= clothes[0]:
        capacity -= clothes.popleft()
    else:
        boxes += 1
        capacity = capacity_restart

print(boxes)

