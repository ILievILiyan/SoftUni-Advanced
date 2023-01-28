from collections import deque

initial_green_line = int(input())
free_window = int(input())
cars = deque()
cars_passed = 0

crash = False
while not crash:
    green_line = initial_green_line
    command = input()

    if command == "END":
        print(f'Everyone is safe.\n{cars_passed} total cars passed the crossroads.')
        break
    elif command == "green":
        while not crash and green_line > 0 and cars:
            current_car = cars.popleft()

            if green_line > len(current_car):
                cars_passed += 1
                green_line -= len(current_car)
            elif green_line + free_window >= len(current_car):
                cars_passed += 1
                green_line = 0
            else:
                print(f'A crash happened!\n{current_car} was hit at {current_car[green_line+free_window]}.')
                crash = True
                break
    else:
        cars.append(command)
