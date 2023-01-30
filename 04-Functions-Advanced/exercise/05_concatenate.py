def concatenate(*args, **kwargs):
    text = "".join(args)

    for key in kwargs.keys():
        text = text.replace(key, kwargs[key])

    return f'{"".join(text)}'


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
print(concatenate("I", " ", "Love", " ", "Cythons", Cy="Py", s=""))