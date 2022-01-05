ed={"sad":"難過","happy":"快樂","angry":"生氣"}
print(ed)

#chi = input("中文意思")
#eng = input("英文意思")

while True:
    print=int(input("function:1-6"))
    user=int(input())
    if user==1:
        print(1)
    elif user==2:
        print(2)
    elif user==3:
        print(3)
        voc=input("eng?")
        if voc in ed:
            print(ed[voc])
    elif user==4:
        got = False
        for k,v in ed.items():
            chi=input("chi?")
            if chi ==v:
                print("eng is",k)
                got=True
        if not got:
            print("nooooooooo")
    elif user==5:
       score=0
       print("總分",len(d),"分")
       for k ,v in ed,items():
           print (v)
           ans==input()
           if ans==k:
               scoore+1
               print("good")
          else:
             print("no")
        
          

#ed.keys()
#ed.values()
#ed.items()

#for k,val in ed.values():