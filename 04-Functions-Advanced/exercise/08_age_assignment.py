def age_assignment(*args, **kwargs):
    names_ages_dict = {}
    for name in args:
        for letter, age in kwargs.items():
            if name[0] == letter:
                names_ages_dict[name] = age

    sorted_names_dict = dict(sorted(names_ages_dict.items(), key=lambda x:x[0]))

    result = ""
    for name, age in sorted_names_dict.items():
        result += f'{name} is {age} years old.\n'

    return result

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))