from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split(" ")])
print(max(orders))

while True:   
    if orders:
        if food >= orders[0]:
            food -= orders.popleft()
        else:
            orders_str = ' '.join([str(elem) for elem in orders])
            print(f'Orders left: {orders_str}')
            break
    else:
        print('Orders complete')
        break