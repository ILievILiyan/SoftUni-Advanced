from collections import deque


def made_toys(current_energy, current_box,used_energy, toys_made, count_moves, current_toys_to_make=1):
    if count_moves % 3 == 0:
        current_box *= 2
        current_toys_to_make = 2

    if current_energy >= current_box:
        if count_moves % 5 != 0:
            toys_made += current_toys_to_make

        used_energy += current_box
        current_energy -= current_box

        if current_energy > 0:
            elf_energy.append(current_energy + 1)

    else:
        if count_moves % 3 == 0:
            boxes.append(int(current_box/2))
        else:
            boxes.append(current_box)
        elf_energy.append(current_energy * 2)

    return used_energy, toys_made


elf_energy = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]

used_energy = 0
toys_made = 0
count_moves = 1

while elf_energy and boxes:
    current_energy = elf_energy.popleft()
    current_box = boxes.pop()

    if current_energy < 5:
        boxes.append(current_box)
        continue

    used_energy, toys_made = made_toys(current_energy, current_box, used_energy, toys_made, count_moves)
    count_moves += 1

print(f"Toys: {toys_made}")
print(f"Energy: {used_energy}")

if elf_energy:
    print(f'Elves left: {", ".join(str(x) for x in elf_energy)}')
if boxes:
    print(f'Boxes left: {", ".join(str(x) for x in boxes)}')

