from math import floor
from collections import deque


class Robot:
    def __init__(self, current_name, robot_processing_time):
        self.name = current_name
        self.processing_time = robot_processing_time
        self.busy_until = 0


def get_seconds(time):
    hh, mm, sec = [int(x) for x in time.split(':')]
    return hh * 3600 + mm * 60 + sec


def get_time(seconds):
    seconds %= (24 * 60 * 60)
    hh = seconds // (60 * 60)
    mm = floor((seconds / 60) % 60)
    sec = seconds % 60
    return f'{hh:02d}:{mm:02d}:{sec:02d}'


robots = []
robots_data = input().split(';')

for robot in robots_data:
    name, processing_time = robot.split('-')
    robots.append(Robot(name, int(processing_time)))

time_in_secs = get_seconds(input())
items = deque()

while True:
    item = input()
    if item == 'End':
        break
    items.append(item)

while items:
    current_item = items.popleft()
    time_in_secs += 1
    found_robot = False

    for robot in robots:
        if time_in_secs >= robot.busy_until:
            found_robot = True
            robot.busy_until = time_in_secs + robot.processing_time
            print(f'{robot.name} - {current_item} [{get_time(time_in_secs)}]')
            break
    else:
        items.append(current_item)
