s = input()

ls = ["",]
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ch = ["",]
num = 0

print(len)

for i in s :
    ls.append(i)

ls.sort()


for i in range(len(ls)) :
    for j in range(len(ls)) :
        if j+1 >= len(ls) :
            break
        else :
            if ls[i] == ls[j+1] :
                count[i] += 1


for i in range(len(ls)) :
    print(ls[i])   
    print(count[i])

