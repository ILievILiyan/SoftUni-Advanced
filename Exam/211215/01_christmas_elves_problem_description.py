from collections import deque


def made_toys(energy, box, total_energy, toys_made, count_moves):
    if count_moves % 3 == 0:
        box *= 2
        current_toys_to_make = 2
    else:
        current_toys_to_make = 1

    if energy >= box:
        total_energy += box
        energy -= box

        if count_moves % 5 != 0:
            toys_made += current_toys_to_make
            elf_energy.append(energy + 1)

    else:
        if count_moves % 3 == 0:
            boxes.append(int(box / 2))
        else:
            boxes.append(box)
        elf_energy.append(energy * 2)

    return total_energy, toys_made


elf_energy = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]

used_energy = 0
toys_made = 0
count_moves = 0

while elf_energy and boxes:
    current_energy = elf_energy.popleft()

    if current_energy < 5:
        continue

    count_moves += 1
    current_box = boxes.pop()

    used_energy, toys_made = made_toys(current_energy, current_box, used_energy, toys_made, count_moves)

print(f"Toys: {toys_made}")
print(f"Energy: {used_energy}")

if elf_energy:
    print(f'Elves left: {", ".join(str(x) for x in elf_energy)}')
if boxes:
    print(f'Boxes left: {", ".join(str(x) for x in boxes)}')
