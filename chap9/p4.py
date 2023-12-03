class Critter:
    total = 0

    def __init__(self, name) :
        print("A new critter has been born!")
        Critter.total += 1

    def status() :
        print("Total critters", Critter.total)

print("Accessing the class attribute Critter.total:",Critter.total)
print("\nCreating critters.")

crit1 = Critter("Critter 1")
crit2 = Critter("Critter 2")
crit3 = Critter("Critter 3")

print("\nThe total number of critters is",Critter.total)

print("\nAccessing the class attribute through an object:",crit1.total)

input("\n\nPress the enter key to exit.")