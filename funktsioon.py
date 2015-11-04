# -*- coding: utf-8 -*-
while True:
    try:
        pikkus = float(input("Sisesta jalalaba pikkus cm: "))
    except ValueError:
        print ("Ups, something wrong...")
        continue
    else:
        break
def jalanõude_suurus(pikkus):
    euroopanr = round((pikkus+1.5)*3/2,0)
    return  euroopanr
print (jalanõude_suurus(pikkus))



