import os

files_dict = {}

absolute_path_directory = os.path.dirname(os.path.abspath(__file__))
files_path = os.path.join(absolute_path_directory, "example_files")
files_directory = os.listdir(files_path)

for current_file in files_directory:
    file_name, extension = current_file.split(".")

    if extension not in files_dict.keys():
        files_dict[extension] = []
    files_dict[extension].append(file_name)

sorted_files_dict = sorted(files_dict.items(), key=lambda x: (x[0], x[1]))

with open("report.txt", "w") as file:
    for extension, filenames in sorted_files_dict:
        file.write(f'.{extension}\n')
        for filename in filenames:
            file.write(f'---{filename}.{extension}\n')

