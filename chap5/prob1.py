import random as R

item = ("sword","armor","shield","healing potion")

l = len(item)
print("Your items:")
for i in item :
    print(i)

print("\nPress the enter key to continue.")
print("You have",l,"items in your prossession.\n")

print("Press the enter key to continue.")

for i in item :
    if i == "healing potion" :
        print("You will live to fight another day.\n")
put = int(input("Enter the index number for an item in inventory: "))
print("At index",put,"is",item[put])

start = int(input("\nEnter the index number to begin a slice: "))
end = int(input("Enter the index number to end the slice: "))
print("inventory[",start,":",end,"]             ",item[start:end])

print("\nPress the enter key to continue.")
chest = ("gold","gems")
print("You find a chest. It contains:\n",chest[:],sep = "")
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
item += chest
print(item[:])

print("\n\nPress the enter key to exit.")
