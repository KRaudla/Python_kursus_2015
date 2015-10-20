  # -*- coding: utf-8 -*-
import math
while True:
    try:
        sendid = int(input("Sisesta sentide arv: "))
    except ValueError:
        continue
    else:
        break
eurod = math.modf(sendid/100)
if(sendid/100%1 == 0) and sendid/100 >= 2:
    print (int(eurod[1]),"eurot") #2 jne eurot
elif sendid/100 == 1:
    print (int(eurod[1]),"euro")# 1 euro
elif sendid/100 == 0:
    print ("Sul pole raha!")
elif round(eurod[0],2) == 0.01 and eurod[1]==1.0:#2 eurot ja 1 sent
        print (int(eurod[1]),"euro ja",int(round(eurod[0],2)*100),"sent")
elif round(eurod[0],2) == 0.01 and eurod[1]>=2.0:#2 eurot ja 1 sent
        print (int(eurod[1]),"eurot ja",int(round(eurod[0],2)*100),"sent")
elif round(eurod[0],2) > 0.01 and eurod[1]>=2.0:#2 eurot ja 1 sent
        print (int(eurod[1]),"eurot ja",int(round(eurod[0],2)*100),"senti")
elif round(eurod[0],2) > 0.01 and eurod[1]==1.0:#2 eurot ja 1 sent
        print (int(eurod[1]),"euro ja",int(round(eurod[0],2)*100),"senti")
elif round(eurod[0],2) == 0.01 and eurod[1]<1.0:
    print (int(round(eurod[0],2)*100),"sent")
else:
    print (int(round(eurod[0],2)*100),"senti")

#kui kasutaja sisestab arvu 207, siis väljastatakse "2 eurot ja 7 senti"
#kui kasutaja sisestab arvu 101, siis väljastatakse "1 euro ja 1 sent" (NB! mitte "1 eurot ja 1 senti", ainsusel ja mitmusel tuleb vahet teha)
#kui kasutaja sisestab arvu 95, siis väljastatakse "95 senti" (st. ilma eurodeta)
#kui kasutaja sisestab arvu 100, siis väljastatakse "1 euro" (st. ilma sentideta)