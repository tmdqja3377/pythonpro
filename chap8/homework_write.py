import shelve
prob = open("prob_zip.txt", "w")

prob.write("\'아까 네넴띤 맛있었지?\'에서 네넴띤은 무엇인가요?\n")
prob.write("소음 측정단위는 데시벨이라고 하는데 기호로는 어떻게 표시하나요?\n")
prob.write("국보 1호였던 문화재의 이름은?\n")
prob.write("오스트레일리아(호주)의 수도는?\n")
prob.write("초등학생이 가장 좋아하는 동네는?\n")

prob.close()

ok = shelve.open("check")
ok["1"] = ["비빔면", "짜장면", "냉면", "칼국수","잔치국수"]
ok["2"] = ["cm", "m", "dA", "dB", "mol"]
ok["3"] = ["광화문","숭례문","대문","소문","나생문"]
ok["4"] = ["서울","스톡홀름","베를린","베이징","캔버라"]
ok["5"] = ["놀이터","하양읍","방학동","pc방","동아리"]

ok.close()

ans = shelve.open("answer")
ans["1"] = [1,"비빔면"]
ans["2"] = [4,"dB"]
ans["3"] = [2,"숭례문"]
ans["4"] = [5,"캔버라"]
ans["5"] = [3,"방학동"]
ans.close()



