import os

absolute_path_file = os.path.abspath(__file__)
absolute_path_directory = os.path.dirname(os.path.abspath(__file__))
""" 

"w" mode -> if file not found -> create new; if file is found -> delete text and add new text
"a" append mode -> just add text to the existing 
"""
file_path = os.path.join(absolute_path_directory, "custom_file", "test.txt")
file = open(file_path, "w")
# print(file.writelines("s\n"))
# print(file.writelines("d"))
# file.write("This is new text")

"""
"r" mode ->  only reading
"""
# file_path = os.path.join(absolute_path_directory, "custom_file", "inner.txt")
# try:
#     file = open(file_path, "r")
# except FileNotFoundError:
#     print("File not found or path is incorrect")
# else:
#     print(file.readlines())
# finally:
#     print("Exit")
