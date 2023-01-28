num_of_commands = int(input())

cars = set()

map_functions = {
    "IN": lambda x: cars.add(x),
    "OUT": lambda x: cars.discard(x)
}

for _ in range(num_of_commands):
    operation, car_number = input().split(", ")
    map_functions[operation](car_number)

if cars:
    print(*cars, sep="\n")
else:
    print('Parking Lot is Empty')
