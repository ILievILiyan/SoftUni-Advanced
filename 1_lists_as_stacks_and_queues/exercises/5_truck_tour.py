from collections import deque

num_of_petrol_pumps = int(input())
petrol_pumps = deque()
fuel = 0

for _ in range(num_of_petrol_pumps):
    current_petrol, distance = input().split()
    petrol_pumps.append((int(current_petrol), int(distance)))

count_pumps_met = 0
count_rotate = 0
while True:
    for i in range(len(petrol_pumps)):
        fuel += petrol_pumps[i][0]
        if fuel >= petrol_pumps[i][1]:
            fuel -= petrol_pumps[i][1]
            count_pumps_met += 1
            if count_pumps_met == num_of_petrol_pumps:
                print(count_rotate)
                exit()
            continue
        else:
            petrol_pumps.rotate(-1)
            count_pumps_met = 0
            count_rotate += 1
            fuel = 0
            break

print(petrol_pumps)
