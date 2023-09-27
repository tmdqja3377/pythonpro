import random

print("I sense your energy.  your true emotions are coming across my screen.")
print("you are...\n")
mood = random.randrange(0, 3)
if mood == 0 :
    print("     ------------")
    print("     |          |")
    print("     |  o    o  |")
    print("     |    <     |")
    print("     |          |")
    print("     |  \___/   |")
    print("     |          |")
    print("     ------------")
elif mood == 1 :
    print("     ------------")
    print("     |          |")
    print("     |  o    o  |")
    print("     |    <     |")
    print("     |          |")
    print("     |  _____   |")
    print("     |          |")
    print("     ------------")
elif mood == 2 :
   print("     ------------")
   print("     |          |")
   print("     |  o    o  |")
   print("     |    <     |")
   print("     |          |")
   print("     |   ____   |")
   print("     |  /    \  |")
   print("     ------------")
else:

   print("Illegal mood value!")
