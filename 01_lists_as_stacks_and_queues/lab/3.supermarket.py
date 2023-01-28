from collections import deque

current = input()
queue_list = deque()

while True:
    if current == "End":
        print(f'{len(queue_list)} people remaining.')
        break
    elif current == "Paid":
        while queue_list:
            print(queue_list.popleft())
    else:
        queue_list.append(current)
    current = input()
