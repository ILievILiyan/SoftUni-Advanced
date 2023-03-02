def shopping_cart(*args):
    limit_products = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }

    dict_foods = {
        "Soup": set(),
        "Pizza": set(),
        "Dessert": set()
    }

    for current_arg in args:
        if current_arg == 'Stop':
            break

        type_meal, product = current_arg

        if len(dict_foods[type_meal]) == limit_products[type_meal]:
            continue
        else:
            dict_foods[type_meal].add(product)

    sorted_meals = sorted(dict_foods.items(), key=lambda x: (-len(x[1]), x[0]))

    output_list = []
    there_is_products = False

    for meal, products in sorted_meals:
        output_list.append(f"{meal}:")
        if products:
            for value in sorted(products):
                there_is_products = True
                output_list.append(f" - {value}")

    if there_is_products:
        return "\n".join(output_list)
    else:
        return "No products in the cart!"






print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print("---------------------------------------------------")
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
print("---------------------------------------------------")
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
