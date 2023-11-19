print("Creating a text file with the write() method.")

print("\nReading the newly created file.")
text_file = open("write_it.txt","w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("And that would make this the third line.\n")
text_file.close()

text_file  = open("write_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nCreateing a text file with the writelines() method.")
print("\nReading the newly created file.")
text_file = open("write_it.txt","w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()

text_file  = open("write_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

input("\n\nPress the enter key to exit.")