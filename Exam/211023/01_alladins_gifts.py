from collections import deque


def gifts_points(material, magic):
    points = material + magic

    if 0 < points < 100:
        if points % 2 == 0:
            points = material * 2 + magic * 3
        else:
            points *= 2
    elif points >= 500:
        points /= 2

    if 100 <= points < 200:
        gift = "Gemstone"

    elif 200 <= points < 300:
        gift = "Porcelain Sculpture"

    elif 300 <= points < 400:
        gift = "Gold"

    elif 400 <= points < 500:
        gift = "Diamond Jewellery"
    else:
        gift = None

    if gift:
        gifts[gift] += 1


materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

gifts = {'Diamond Jewellery': 0, 'Gemstone': 0, 'Gold': 0, 'Porcelain Sculpture': 0}

while materials and magic_levels:
    material = materials.pop()
    magic_lvl = magic_levels.popleft()
    gifts_points(material, magic_lvl)

if (gifts["Gemstone"] and gifts["Porcelain Sculpture"]) or (gifts["Gold"]  and gifts["Diamond Jewellery"]):
    print('The wedding presents are made!')
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials)}')
if magic_levels:
    print(f'Magic left: {", ".join(str(x) for x in magic_levels)}')

for k, v in gifts.items():
    if v:
        print(f"{k}: {v}")
