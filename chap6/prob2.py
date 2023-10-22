scores = [  (1000, "Moe"), (1500, "Larry") ]

while 1 :
    print("   High Scores Keeper\n")
    print("   0 - Quit")
    print("   1 - List Scores")
    print("   2 - Add a Score\n")
    
    put = int(input("Choice: "))

    if put == 0:
        break

    elif put == 1:
        print("\nHigh Scores\n")
        print("NAME\t SCORE")
        scores.sort()
        scores.reverse()
        for i in scores:
            score, name = i
            print(name, "\t", score)
        print("")
    elif put == 2:
        addname = input("What is the player's name?: ")
        addscore = int(input("What score did the player get?: "))
        temp = (addscore, addname)
        scores.append(temp)
        print("")
    else :
        continue
