text_file  = open("read_it.txt", "r")

print("Opening and closing the file.")
print("\nReading characters from the file.")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

text_file  = open("read_it.txt", "r")
print("\nReading the entire file at once.")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

text_file  = open("read_it.txt", "r")
print("\nReading charactors from a line.")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

text_file  = open("read_it.txt", "r")
print("\nReading one line at a time.")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

text_file  = open("read_it.txt", "r")
print("Reading the entire file inti a list.")
lines = text_file.readlines()
print(lines)
print(len(lines))
for i in lines :
    print(i)
text_file.close()


print("\nLooping through the file, line by line.")
text_file  = open("read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()

input("Press the enter key to exit.")