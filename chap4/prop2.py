import random as r
h = r.randrange(50,101)
m = r.randrange(50,101)
count = 0;
print("hero HP: ",h, " monster HP: ",m )
while(h > 0 and m > 0) :
    ha = r.randrange(-10,21)
    ma = r.randrange(-10,21)
    hs = ""
    ms = ""
    if ha < 1:
        hs = "fail"
    else :
        hs = "success"
        m = m - ha
    if ma < 1:
        ms = "fail"
    else :
        ms = "success"
        h = h - ma
    print("hero(HP: ",h, "attack: ",ha,")" ,hs, "<-> monster(HP:",m, "attack:",ma,")",ms)
    count = count + 1

print("\n--------------------------------------------------------\n")
print("Total phase: ",count)

if h > m :
    print("\nHero Win!!!!")
else :
   print("\nHero Loser")
