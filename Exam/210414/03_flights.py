def flights(*args):
    destination_and_passangers = {}
    for current_destination in args(0, len(destination_and_passangers)):
        if current_destination == "Finish":
            break
        if current_destination not in destination_and_passangers.keys():
            destination_and_passangers[current_destination] = 0
        destination_and_passangers[current_destination] +=

    pass



print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print("------------------------------")
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print("------------------------------")
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))