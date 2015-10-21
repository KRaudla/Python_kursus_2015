import re
#versioon2
while True:
    try:
        isikukood = int(input("Sisesta isikukood: "))
    except ValueError:
        print ("Ei ole Eesti isikukood")
        continue
    else:
        break
isikukood = str(isikukood)
if re.match("^[1-6]{1}[0-9]{10}$",isikukood):
    print ("On Eesti isikukood")
else:
    print ("Ei ole Eesti isikukood")