  # -*- coding: utf-8 -*-
while True:
    try:
        tunnid = int(input("Mitu tundi nädalas töötasid? "))
    except ValueError:
        print ("Sisesta number!")
        continue
    else:
        break
while True:
    try:
        tunnitasu = int(input("Kui suur on tunnitasu? "))
    except ValueError:
        print ("Sisesta number!")
        continue
    else:
        break
if tunnid <= 40:
    print (tunnid*tunnitasu)
elif tunnid > 40:
    ületunnipalk = 40*tunnitasu+(tunnid-40)*(tunnitasu*1.5)
    print (ületunnipalk)
elif tunnid == 0:
    print ("Käi tööl, siis saad alles pappi")
