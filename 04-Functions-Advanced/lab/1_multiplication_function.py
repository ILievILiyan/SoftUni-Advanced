def multiply(*args):
    y = 1
    for x in args:
        y *= x
    return y

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
