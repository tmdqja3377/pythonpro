import random as R

class Critter:
    def __init__(self,name, mood_level) :
        self.name = name
        self.mood_level = mood_level
        name = input("What do you want to name your critter?: ")
        # 0 mad
        # 1 frustrated
        # 2 soso
        # 3 happy

    def setmood(self, level) :
        self.mood_level = level

    def getmood(self) :
        print("mood level", self.mood_level)

    def talk(self) :
        mood = ""
        if self.mood_level == 0 :
            mood = "mad"
        elif self.mood_level == 1:
            mood = "frustrated"
        elif self.mood_level == 2:
            mood = "soso"
        else :
            mood = "happy"

        print("I'm ",self.name," and I feel ",mood," now",sep="")
        if self.mood_level > 0 :
            self.mood_level -= 1

    def Feed(self) :
        self.mood_level += 1
        print("It's good. But give me more")

    def Play(self) :
        self.mood_level += R.randint(1,4)
        print("It was fun")

cr = Critter(name = "", mood_level = 0)

while(1) :
    print("\n\tCritter Caretaker")
    print("\n\t0 - Quit")
    print("\t1 - Listen to your critter")
    print("\t2 - Feed your critter")
    print("\t3 - Play with your critter")

    choice = int(input("Choice: "))

    if choice == 0 :
        break
    elif choice == 1 :
        cr.talk()
    elif choice == 2 :
        cr.Feed()
    elif choice == 3 :
        cr.Play()
    else :
        continue
