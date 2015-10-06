  # -*- coding: utf-8 -*-
import math
while True:
    try:
        laius = int(input("Kui lai on tort? "))
    except ValueError:
        print ("Sisesta number!")
        continue
    else:
        break
while True:
    try:
        pikkus = int(input("Kui pikk on tort? "))
    except ValueError:
        print ("Sisesta number!")
        continue
    else:
        break
while True:
    try:
        kõrgus = int(input("Kui kõrge on tort? "))
    except ValueError:
        print ("Sisesta number!")
        continue
    else:
        break
while True:
    try:
        küpsiste_arv_pakis = int(input("Kui palju on küpsiseid pakis? "))
    except ValueError:
        print ("Sisesta number!")
        continue
    else:
        break
palju_küpsiseid_on_vaja =laius*pikkus*kõrgus
pakke_on_vaja = palju_küpsiseid_on_vaja/küpsiste_arv_pakis
if pakke_on_vaja%1 == 0:
    print ("Tordi tegemiseks on sul vaja "+str(int(pakke_on_vaja))+" pakki küpsiseid.")
else:
    print ("Tordi tegemiseks on sul vaja "+str(math.ceil(pakke_on_vaja))+" pakki küpsiseid.")
