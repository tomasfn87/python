# python3 -m pip install pathlib
import pathlib

file_path = pathlib.Path("./data/hello.txt")

with file_path.open("r") as file:
    print(file.read())
