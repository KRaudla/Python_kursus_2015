import codecs
from bs4 import BeautifulSoup
import csv

with codecs.open("kasutajad.html", "r",encoding='utf8') as input,open("data.csv","w", encoding="utf-8") as output:
    writer = csv.writer(output, delimiter="\t",quotechar="'",quoting=csv.QUOTE_ALL)
    writer.writerow(["Nimi","E-mail"])
    soup = BeautifulSoup(input,"html.parser")
    for i in soup.find_all("td",attrs={"class":"content cell c1"}):
        lis =[]
        nimi = i.find("div",attrs={"class":"username"}).get_text()
        lis.append(nimi)
        try:
            email = i.find("a",href=True).get_text()
            lis.append(email)
        except:
            email = ""
            lis.append(email)
        writer.writerow(lis)


        #lis.append(i.get_text())
    #for i in soup.find_all("div",attrs={"class":"info"}):
     #   print (i.find("a",href=True).get_text())



