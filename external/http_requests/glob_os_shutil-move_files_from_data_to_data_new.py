import glob
import os
import shutil

file_paths = []

for file_name in glob.glob("data/*.txt"):
    file_paths.append(os.path.join("", file_name))

count = 1
new_path = "data_new"
file_count = []
for f in file_paths:
    with open(f) as file:
        file_count.append(f"file {count} ({f} [{file.read(17)} ...])")
        count += 1

moved_files  = []
for file in file_paths:
    shutil.move(file, new_path)
    moved_files.append(f"moved to {new_path}/")

for i in range(0, len(file_count)):
    print(f"{file_count[i]} {moved_files[i]}")
    if i != len(file_count)-1:
        print()
