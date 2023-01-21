from collections import deque

materials = deque(int(x) for x in input().split())
magic_lvl = deque(int(x) for x in input().split())

magic_levels_toys = {
    150: ["Doll", 0],
    250: ["Wooden train", 0],
    300: ["Teddy bear", 0],
    400: ["Bicycle", 0],
}

while materials and magic_lvl:
    last_material = materials.pop()
    first_magic = magic_lvl.popleft()
    result = last_material * first_magic

    if last_material == 0 and first_magic == 0:
        continue
    elif last_material == 0:
        magic_lvl.appendleft(first_magic)
        continue
    elif first_magic == 0:
        materials.append(last_material)
        continue

    if result < 0:
        materials.append(last_material + first_magic)
    else:
        if result not in magic_levels_toys.keys():
            materials.append(last_material + 15)
        else:
            magic_levels_toys[result][1] += 1

if (magic_levels_toys[150][1] > 0 and magic_levels_toys[250][1] > 0) or\
        (magic_levels_toys[300][1] > 0 and magic_levels_toys[400][1] > 0):
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')

if materials:
    materials.reverse()
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic_lvl:
    print(f'Magic left: {", ".join(map(str, magic_lvl))}')

sorted_magic_level_toys = sorted(magic_levels_toys.items(), key=lambda x: (x[1]))
for toys in sorted_magic_level_toys:
    print(f'{toys[1][0]}: {toys[1][1]}') if toys[1][1] > 0 else None


