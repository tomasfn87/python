import glob
import os
import shutil

file_paths = []

for file_name in glob.glob("data/*.txt"):
    file_paths.append(os.path.join("", file_name))

for i in file_paths:
    with open(i) as file:
        print(f"{i}: {file.read()}")