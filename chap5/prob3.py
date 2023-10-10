import random as R
words = ["difficult","banana","apple","python","daegu","catholic","university"]
check = []
hp = 3
chosen = R.choice(words)         #1
player = ""
leng = len(chosen)
for i in range(leng) :
        check.append("_")
i = 0
words.clear()
while i < leng :
        words.append(chosen[i])
        i += 1

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")
print("Length of the selected word:",leng)		#2

wordcount = 0

while hp > 0 :						#4
        count = -1
        print("Remaining attempts:",hp)                 #output
        print("Current guessed word:",end = "")
        for i in check:
                print(i," ",end = "",sep ="")
        put = input("\nGuess a letter: ")		#3 input

        correct = 0
        for i in words :
                count += 1
                if put == i:
                        if check[count] == put :	#check
                                print("retry")
                                break
                        else :
                            check[count] = i            #correct!
                            wordcount += 1
                        correct = -1
                else :                                  #discorrect!
                        if count + 1 == leng and correct == 0 :
                                hp -= 1
                                print("Incorrect guess.")                                       


        if wordcount >= leng :
                for i in check :
                        player += i
    

        if chosen == player :
                print("Congratulations! You guessed the word:",chosen)
                break
        
        if hp  < 1 :
                print("You've used up all your attempts. The correct word was ",chosen,".",sep = "")
