import requests
from bs4 import BeautifulSoup
import  _sqlite3
import time

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS TopChannelsByCountry(Title TEXT, Country TEXT, Category TEXT, Subscribe TEXT, View TEXT, Video TEXT)")

def addValue(title,country,category,subs,view,video):
    cursor.execute("INSERT INTO TopChannelsByCountry(Title, Country, Category, Subscribe, View, Video) VALUES(?,?,?,?,?,?)", (title,country,category,subs,view,video))
    con.commit()

def delete():
    cursor.execute("DELETE FROM TopChannelsByCountry")
    con.commit()

con = _sqlite3.connect("youtube.db")
cursor = con.cursor()

inp = int(input("Create: 1\nDelete: 2\n"))

t0 = time.time()

if(inp==1):
    main_url = "https://watchin.today"

    r = requests.get("https://watchin.today/charts/channel/country")
    soup = BeautifulSoup(r.content, "html.parser")

    var = soup.find_all("a", {"class":"nps-item"})
    var = var[: len(var) - 15]

    var2 = soup.find_all("div", {"class":"nps-item-text"})
    var2 = var2[: len(var2) - 15]

    link_list = []
    for link in var:
        link_list.append(link.get("href"))
    country_names = []
    for names in var2:
        country_names.append(names.text)

    createTable()

    i = 0
    for links in link_list:
        current_url = main_url + links
        r = requests.get(current_url)
        soup = BeautifulSoup(r.content, "html.parser")

        var = soup.find("div", {"class":"chart-item-data"})
        var = var.contents

        title = var[0].text

        var = var[1].contents

        category = var[0].text
        subs = var[1].text
        view = var[2].text
        video = var[3].text
        country = country_names[i]
        i += 1
        addValue(title,country,category,subs,view,video)

elif(inp==2):
    delete()

con.close()

t1 = time.time()
print("Process time:", (str(t1-t0))[:6])