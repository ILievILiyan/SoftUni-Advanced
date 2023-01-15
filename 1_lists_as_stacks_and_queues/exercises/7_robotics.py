from collections import deque


def time_to_sec(time):
    hh, mm, ss = map(int, time.split(':'))
    return hh * 3600 + mm * 60 + ss


def sec_to_time(ss):
    hh = ss // (60 * 60)
    ss %= (60 * 60)
    mm = ss // 60
    ss %= 60
    time = f"{hh:02d}:{mm:02d}:{ss:02d}"
    return time


def calculate_time(starting_hours):
    seconds_to_add = 1
    total_ss = time_to_sec(starting_hours)
    total_ss += seconds_to_add
    return sec_to_time(total_ss)


robots = {x.split("-")[0]:[int(x.split("-")[1]), 0] for x in input().split(";")}
# name: [time_per_1_product, time_for_current_task]
current_time = input()
products = deque()


while True:
    command = input()
    if command == "End":
        break
    else:
        products.append(command)

while products:
    current_time = calculate_time(current_time)
    product = products.popleft()

    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(product)
        continue
    robots[free_robots[0][0]][1] = free_robots[0][1][0]
    print(f'{free_robots[0][0]} - {product} [{current_time}]')

