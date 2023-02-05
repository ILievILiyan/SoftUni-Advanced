import os

file_path = "file.txt"

# if os.path.exists(file_path):
#     os.remove(file_path)
#     print("file remove")
# else:
#     print("File already deleted!")

try:
    os.remove(file_path)
    print("file remove")
except FileNotFoundError:
    print("File already deleted!")
