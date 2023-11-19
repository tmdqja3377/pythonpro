import _pickle as cPickle
import shelve

print("Pickling lists.\n")

print("Unpickling lists.")

variety = ['sweet', 'hot', 'dill']
shape = ["Whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

pickle_file = open("./pickles1.dat", 'wb')
cPickle.dump(variety, pickle_file)
cPickle.dump(shape, pickle_file)
cPickle.dump(brand, pickle_file)
pickle_file.close()

pickle_file = open("pickles1.dat", "rb")
variety = cPickle.load(pickle_file)
v2_1 = cPickle.load(pickle_file)
v3_1 = cPickle.load(pickle_file)
print (variety)
print (v2_1)
print (v3_1)
pickle_file.close()

print("\nShelving lists.\n")
print("Retrieving the lists form a shelved file:")
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["Whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]

pickles.sync()
for key in pickles.keys():
    print(key, "-", pickles[key])

pickles.close()

input("\n\nPress teh enter key to exit.")