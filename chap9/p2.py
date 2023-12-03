class Critter:
    def talk(self) :
        print("Hi, I'm an instance of class Critter.")
    def __init__(self) :
        print("A new critter has been born!")

crit1 = Critter()
crit2 = Critter()
print()
crit1.talk()
print()
crit2.talk()

input("\n\n\nPress the enter key to exit.")