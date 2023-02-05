#if we use "a" we add some text;
#if we use "w" we will delete old text and will be saved only the new one
with open("my_first_file.txt", "a") as file:
    file.write("I just created my first file!")




