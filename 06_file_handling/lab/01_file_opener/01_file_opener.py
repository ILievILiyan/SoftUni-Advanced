import os

""" V1:  """
# try:
#     file = open("text.txt")
#     print("File found")
# except FileNotFoundError:
#     print("File not found")

""" V2 """
if os.path.exists("text.txt"):
    print("File found")
else:
    print("File not found")
