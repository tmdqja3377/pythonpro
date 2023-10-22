geek = {"404" : "clueless.", "Uninstalled" : "being fired."}
geek["being fired."] = "Especially popular during the dot-bomb era."
add = ["being fired."]
while 1  :
    print("\n\tGeek Translator\n")
    print("\t0 - Quit")
    print("\t1 - Look Up a Geek Term")
    print("\t2 - Add a Geek Term")
    print("\t3 - Redefine a Geek Term")
    print("\t4 - Delete a Geek Term")

    put =  int(input("Choice: "))

    if put == 0 :
        break

    elif put == 1: 
        key = input("\nWhat term do you want me to translate?: ")
        if key in geek :
            value = geek[key]
            print(key,"means",geek[key],end = "")
            if value in geek:
                print("\t",geek[value])
            else :
                print("\n")
        else :
            print("I have no what",key,"is.")

    elif put == 2 :
        term = input("\nWhat term do you want me to add?: ")
        mean = input("How do you translate it?: ")
        geek[term] = mean

    elif put == 3 :
        redefine = input("\nWhat term do you want me to redefine?: ")
        content = input("Enter content:")
        geek[redefine] = content
    
    elif put == 4 :
        delete = input("\nWhat term do you want me to delete?: ")
        if delete in geek :
            del geek[redefine]
        else :
            print("I can't find the term")
    
    else :
        continue


    
        
