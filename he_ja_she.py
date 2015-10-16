while True:
    try:
        isikukood = int(input("Sisesta isikukood"))
    except ValueError:
        print ("Isikukood on number!")
        continue
    else:
        break

if str(isikukood)[0] in ("1","3","5"):
    print ("he")
elif str(isikukood)[0] > "6":
    print ("See pole isikukood.")
else:
    print ("she")

