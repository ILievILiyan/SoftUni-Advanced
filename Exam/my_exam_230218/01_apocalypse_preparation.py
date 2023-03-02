from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque(int(x) for x in input().split())

items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}
while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    current_sum = medicament + textile

    if current_sum in items.values():
        for item, amount in items.items():
            if current_sum == amount:
                created_items[item] += 1

    elif current_sum > items["MedKit"]:
        available_sum = current_sum - items["MedKit"]
        created_items["MedKit"] += 1
        next_medicament = medicaments.pop() + available_sum
        medicaments.append(next_medicament)
        
    else:
        medicaments.append(medicament + 10)

sorted_created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))


if medicaments and not textiles:
    print("Textiles are empty.")
elif not medicaments and textiles:
    print("Medicaments are empty.")
else:
    print("Textiles and medicaments are both empty.")

for name, amount in sorted_created_items:
    if amount:
        print(f'{name} - {amount}')

if medicaments:
    medicaments.reverse()
    print(f'Medicaments left: {", ".join(str(x) for x in medicaments)}')

elif textiles:
    print(f'Textiles left: {", ".join(str(x) for x in textiles)}')
