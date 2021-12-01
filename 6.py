n=0
n=int(input("有幾人?"))
score=[]
num=0
sum=0
i=n
highest=0
while n>0:
    num=int(input())
    score.appened(num)
    n=n-1
    sum=sum+num
for a in score:
    if a > highest:
        print(a)