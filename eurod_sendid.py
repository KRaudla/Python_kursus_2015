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
    print (int(eurod[1]),"eurot")
elif (sendid/100%1 == 0) and sendid/100 == 1:

elif:
    print (int(eurod[1]),"euro")

#if sendid/100 < 1 and sendid/100 > 0:
#    print (str(sendid),"senti")
#elif sendid/100 == 1:
#    print ("1 euro")
#elif sendid/100 >1 and sendid/100 <2:
#    eurod = math.modf(sendid/100)
#    if round(eurod[0],2) == 0.01:
#        print (int(eurod[1]),"euro ja",int(eurod[0]*100),"sent")
#    else:
#        print (int(eurod[1]),"euro ja",int(eurod[0]*100),"senti")
#else:
#    eurod = math.modf(sendid/100)
#    if round(eurod[0],2) == 0.01:
#        print (int(eurod[1]),"eurot ja",int(eurod[0]*100),"sent")
#    else:
#        print (int(eurod[1]),"eurot ja",int(eurod[0]*100),"senti")
