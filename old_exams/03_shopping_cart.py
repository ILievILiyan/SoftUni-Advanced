def shopping_cart(*args):
    dict_foods = {
        "Pizza": [],
        "Dessert": [],
        "Soup": []
    }

    for current_arg in args:
        if current_arg == 'Stop':
            break
        type_meal, product = current_arg
        if len(dict_foods[type_meal]) < limit_products[type_meal] and product not in dict_foods[type_meal]:
            dict_foods[type_meal].append(product)

    sorted_dict = sorted(dict_foods.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    there_is_products = False

    for meal, products in sorted_dict:
        result += f"{meal}:\n"
        for product in sorted(products):
            if product:
                there_is_products = True
            result += f'- {product}\n'

    if there_is_products:
        return result
    else:
        return "No products in the cart!"


limit_products = {
    "Soup": 3,
    "Pizza": 4,
    "Dessert": 2
}


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

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
