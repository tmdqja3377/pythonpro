import random as R
word = ["difficult","banana","apple","python","daegu","catholic","university"]
check = []
hp = 6
chosen = R.choice(word)		#1
player = ""
leng = len(chosen)		#2
for i in range(leng) :
	check.append("_")
i = 0
word.clear()
while i < leng :
	word.append(chosen[i])
	i += 1

print(word)

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")
print("Length of the selected word:",leng)

index = 0

while 1 :
	count = 0
	print("Remaining attempts:",hp)			#output
	print("Current guessed word:",end = "")
	for i in check:
		print(i," ",end = "",sep ="")
	put = input("\nGuess a letter: ")
	
	for i in word :
		count += 1
		if put == i :
			check[count] = put
			player += i
		else :
			continue
	if chosen == player :
		print("Congratulations! You guessed the word:",chosen)
		break
	else :
		continue
		
