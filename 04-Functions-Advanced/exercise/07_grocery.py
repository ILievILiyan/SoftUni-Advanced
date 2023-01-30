def grocery_store(**kwargs):
    sorted_products_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    result = ""
    for product, value in sorted_products_dict.items():
        result += f'{product}: {value}\n'
    return result


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
