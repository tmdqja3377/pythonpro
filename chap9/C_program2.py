import random as R
#ppt내용의 두 함수를 어떻게 구현하라는건지 이해가 잘 가지않습니다
#두개의 함수를 어떻게 써야할지 몰라서 하나만 사용했습니다
class Food:
    def __init__(self,name,level) :
        self.name = name
        self.level = level
        
    def getLevel(self) :
        if self.name == "meat" :
            self.level += 5
        elif self.name == "icecream" :
            self.level += 3
        elif self.name == "feed" :
            self.level += 1
        print(self.level)
        return self.level

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
        print("1 - meat")
        print("2 - feed")
        print("3 - icecream\n")
        food = ""
        num = int(input("What kind of snack are you going to give me? "))
        if num == 1 :
            food = "meat"
        elif num == 2 :
            food = "feed"
        elif num == 3 :
            food = "icecream"
        else :
            print("error")

        fd = Food(food,self.mood_level)
        self.mood_level = fd.getLevel()
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
    elif choice == 4 :
        print("mood_level =",cr.mood_level)
    else :
        continue
