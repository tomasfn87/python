file = open("./data/hello.txt", "w")

# before 'with', try...finally was the best option to avoid leaving a file open

try:
    file.write("Hello, world!")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    file.close()
