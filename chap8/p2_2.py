text_file = open("write_and_read_it.txt","w")
print("Input your string...")
while 1 :
    put = input(">> ")
    if put == "Q" :
        break
    else :
        text_file.write(put+"\n")
text_file.close()
print("Write process has been finished\n\n\n\n")




print("Your inputs are below..")
text_file = open("write_and_read_it.txt","r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()
    

