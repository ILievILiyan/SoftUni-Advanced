def add_items_to_dictionary(number_of_items,dictionary):
    for _ in range(number_of_items):
        current_ticket = input()
        dictionary.add(current_ticket)
    return dictionary


number_of_guests = int(input())
tickets = set()

add_items_to_dictionary(number_of_guests, tickets)

while True:
    guest = input()
    if guest == "END":
        break
    else:
        tickets.discard(guest)

print(len(tickets))
print(*sorted(tickets), sep="\n")
