import random as R
import shelve

print("\t\tWelcome to Trivia Challenge!")
print("\n\t\tAn Episodo You Can't Refuze")

print("problum :")
num = R.randint(0,4)

prob = open("prob_zip.txt", "r")

for i in range(num):
    prob.readline()
print(prob.readline())

prob.close()

ok = shelve.open("check")
for i in range(5) :
    print(i+1,". ",ok[str(num+1)][i],"\n",sep="")
ok.close()

user = int(input("정답은 몇번인가요? "))
ans = shelve.open("answer")
if (ans[str(num+1)][0] == user) :
    print("\'",ans[str(num+1)][1],"\' ","정답입니다",sep="")
else :
    print("오답입니다")
ans.close()