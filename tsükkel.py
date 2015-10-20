  # -*- coding: utf-8 -*-
number = int(input('Sisesta täisarv '))
if number >= 0:
    summa = 0
    while number > 0:
        summa = summa + number
        number=number-1
    print (summa)
else:
    print (0)









