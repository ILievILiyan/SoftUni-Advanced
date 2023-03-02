def shopping_list(budget, **products):
    if budget < 100:
        return f'You do not have enough budget.'

    bought_products = {}

    for product, price_and_quantity in products.items():
        if len(bought_products.keys()) == 5 or not products:
            break

        price = price_and_quantity[0]
        quantity = price_and_quantity[1]
        total_price = price * quantity

        if budget >= total_price:
            if product not in bought_products.keys():
                bought_products[product] = [0, 0]

            bought_products[product][0] = total_price
            bought_products[product][1] = quantity
            budget -= total_price
    output_list = []
    for product, price_quantity in bought_products.items():
        output_list.append(f'You bought {product} for {price_quantity[0]:.2f} leva.')
    return "\n".join(output_list)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print("-----------------")
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print("-----------------")
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
