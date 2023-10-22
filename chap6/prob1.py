import random as R

inventory = ["sword","armor","shield","healing potion"]

l = len(inventory)
print("Your items:")
for i in inventory :
    print(i)

print("\nPress the enter key to continue.")
print("You have",l,"items in your prossession.\n")

print("Press the enter key to continue.")

for i in inventory :
    if i == "healing potion" :
        print("You will live to fight another day.\n")
put = int(input("Enter the index number for an item in inventory: "))
print("At index",put,"is",inventory[put])

start = int(input("\nEnter the index number to begin a slice: "))
end = int(input("Enter the index number to end the slice: "))
print("inventory[",start,":",end,"]             ",inventory[start:end])

print("\nPress the enter key to continue.")
chest = ["gold","gems"]
print("You find a chest. It contains:\n",chest[:],sep = "")
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
inventory += chest
print(inventory[:])

print("\n\nPress the enter key to exit.")

print("You trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now: \n",inventory)

print("\nPress the enter key to continue.")
print("you use your gold and gems to buy an orb of future telling.")

inventory[4:6] = ["orb of future telling"]
print("Your inventory is now:\n",inventory)

print("\nPress the enter key to continue.")
print("In a great battle, your shield is destroyed.")
del inventory[2]
print("Your inventory is now: \n",inventory)

print("\nPress the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.")
del inventory[0:2]
print("Your inventory is now:\n",inventory)
print("\n\nPress the enter key to continue.")
