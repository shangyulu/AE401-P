
while True:
    print("/n 1apple 價錢")
    print("2進貨apple")
    print("3賣apple")
    print("4銷售額")
    print(" 5apple庫存 ")
    print("結束")
    
    ui=int(input("功能"))
    if ui==1:
        an=int(input("幾顆apple"))
        an=int(input("apple價錢"))
    elif ui==2:
        ac==comepacket()
        an=an+ac
    elif ui==3:
        ao=int(input("賣了幾個apple"))
        an=an-ao
        gm=ao*ap
        sell.append([ao,gt])
    elif ui==4:
        sum=0
        money=0
        for i in sell:
            sum=sum+i[0]
            money=money+i[1]
        print("今天有"len(sell),"交易 分別賣",sum,"個蘋果共收",money)
    elif ui==5:
        print("剩下蘋果",an)
    elif ui==6:
        break
    