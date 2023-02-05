import os
import json

absolute_path_file = os.path.abspath(__file__)
absolute_path_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path_directory, "custom_file", "a.json")

#json to dictionary
file = open(file_path)
my_dict = json.load(file)
print(type(my_dict))
print(my_dict)
