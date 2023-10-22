import random as R

def display(hp) :
    head = "o"
    arm = "-+-"
    waist = " | "
    leg = "/ \\"
    print(" ---------")
    print(" |      |")
    if hp < 1 :
        print(" |")
    else :  print(" |      o")
    if hp < 2 :
        print(" |")
    else :  print(" |     -+-")
    if hp < 3 :
        print(" |")
    else :  print(" |      | ")
    if hp < 4 :
        print(" |")
    else :  print(" |     / \\")
    print("--------------")

word = ["hangman", "coffee", "banana", "codebook", "daegu", "terminal"]
userinput = []
correct = []
hp = 4
cword = R.choice(word)
leng = len(cword)
word.clear()

for i in range(leng) :
    word.append(cword[i])
    correct.append("_")

display(hp)

while 1 :
    check = 0
    put = input("\nEnter your guess: ")
    userinput.append(put)

    for i in range(leng) :
        if word[i] == put :
            correct[i] = put
            check = 1
        else :
            if i == (leng - 1) and check == 0:
                hp -= 1

    if check == 1 :
        print("\nYes!",put,"is in the word!\n")
    else :
        print("\nNo!",put,"is not in the word!\n")
    
    display(hp)
    print()

    print("You've used the following letters:\n",userinput)

    print("so far, the word is:")
    for i in range(leng) :
        print(correct[i],end ="")
    print()

    if hp == 0 :
        print("\nYou LOSER!\n")
        break
    else :
            w = ""
            for i in range(leng) :
                w += correct[i]
            if w == cword :
                print("\nYou WIN!!\n")
                break
    

    

