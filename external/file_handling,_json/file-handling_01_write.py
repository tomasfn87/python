'''
# file handler
fh = open("sample_file.txt", "a")

#fh.write("Just looking for a test here.")

try:
    for i in range(1,11):
        fh.write("This is line #%d\n" % i)
finally:
    fh.close()
'''
# The with is the same thing as the code above:

#link = "https://www.youtube.com/watch?v=XxRtj-GU5_8"

with open("sample-file_01.txt", "a") as fh:
    for i in range(11, 21):
        fh.write("This is line #%d\n" % i)
    #fh.write(link)