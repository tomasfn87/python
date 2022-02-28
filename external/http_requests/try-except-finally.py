file = open("./data/hello.txt", "w")

try:
    file.write("Hello, world!")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    file.close()
