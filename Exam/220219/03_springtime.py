def start_spring(**kwargs):
    types_dict = {}

    for name, type in kwargs.items():
        if type not in types_dict.keys():
            types_dict[type] = []
        types_dict[type].append(name)

    sorted_types_dict = sorted(types_dict.items(), key=lambda x:(-len(x[1]), x[0]))

    output_list = []
    for type_spring, names in sorted_types_dict:
        output_list.append(f'{type_spring}:')
        for name in sorted(names):
            output_list.append(f'-{name}')
    return "\n".join(output_list)


example_objects = {
    "Water Lilly": "flower",
    "Swifts": "bird",
    "Callery Pear": "tree",
    "Swallows": "bird",
    "Dahlia": "flower",
    "Tulip": "flower"
}
print(start_spring(**example_objects))

print("-------------------------------------------")
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

print("-------------------------------------------")

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

