import random
print("    Welcome to \'Guess My Numner\'1")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n\n")
N = random.randrange(1,101)
count = 0;
print(N)
while (1) : 
    number = int(input("Take a guess: "))
    count = count + 1
    if number > N :
        print("Lower...")
    elif number < N :
        print("Higher...")
    else:
        print("You guessed it! The number was %d" %N)
        print("And it only took you %d tries!" %count)
        break;
print("\n\n\nPress the enter key to quit")
