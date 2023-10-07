import random

word = ["difficult","banana","apple","python","daegu","catholic","university"]

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")

choice_word = random.choice(word)

word.clear()
leng = len(choice_word)
shuffle_word = ""
i = 0

while(i < leng) :
	word.append(choice_word[i])
	i += 1
	
random.shuffle(word)
i = 0

while i < leng :
	shuffle_word += word[i]
	i+= 1

print("Jumbled word:" ,shuffle_word)
put = input("Your guess: ")

if put == choice_word :
	print("Correct!")
else :
	print("Sorry, that's not correct. The word was:",choice_word)
