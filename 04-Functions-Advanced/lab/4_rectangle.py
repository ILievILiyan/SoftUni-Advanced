def rectangle(length, width):
    if type(length) == int and type(width) == int:
        rectangle_area = length * width
        rectangle_perimeter = 2*(width + length)
        return f"Rectangle area: {rectangle_area}\nRectangle perimeter: {rectangle_perimeter}"
    else:
        return "Enter valid values!"


print(rectangle('2', 10))