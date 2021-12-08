
a = int(input("全班人數"))
b = a
c = 0
d = 0


score = []
name = [] #我們新的需求


highest = 0
lowest = 100
highname = ""
lowestname=""
print("輸入",a,"個人的分數")
while a > 0:
    a = a-1 #while終止條件
    
    na = input("名字:") #名字變數
    name.append(na) #新增 一個名字的元素 進入到 name 的list裡
    
    
    d = int(input("成績:")) #成績變數
    score.append(d) #新增 一個數字的元素 進入到 score 的list裡
    
    c = c+d # 總和
print(name)
print(score)

for i in range(3):
    if score[i] > highest:
        highest = score[i]
        highname = name[i]
for i in range(3):
    if score[i]<lowest:
        lowest = score[i]
        lowestname= name[i]

print("平均值:",c/b)

print("最高分:",highest," 是",highname)
print("最低分:",lowest,"是",lowestname)
