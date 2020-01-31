import requests
from bs4 import BeautifulSoup
import _sqlite3
import time


def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS TopChannelsByCountries(Title TEXT, Country TEXT, Category TEXT, Subscriber_Count_Million REAL, Total_Views_Billion REAL, Video_Count INT)")


def addvalue(title, country, category, subs, view, video):
    cursor.execute("INSERT INTO TopChannelsByCountries(Title, Country, Category, Subscriber_Count_Million, Total_Views_Billion, Video_Count) VALUES(?,?,?,?,?,?)", (title, country, category, subs, view, video))
    con.commit()


def delete():
    cursor.execute("DELETE FROM TopChannelsByCountry")
    con.commit()


con = _sqlite3.connect("youtube.db")
cursor = con.cursor()

process = int(input("Create: 1\nDelete: 2\n"))

t0 = time.time()

if process == 1:
    main_url = "https://watchin.today"

    r = requests.get("https://watchin.today/charts/channel/country")
    soup = BeautifulSoup(r.content, "html.parser")

    var = soup.find_all("a", {"class": "nps-item"})
    var = var[: len(var) - 15]

    var2 = soup.find_all("div", {"class": "nps-item-text"})
    var2 = var2[: len(var2) - 15]

    link_list = []
    for link in var:
        link_list.append(link.get("href"))
    country_names = []
    for names in var2:
        country_names.append(names.text)

    createtable()

    i = 0
    for links in link_list:
        current_url = main_url + links
        r = requests.get(current_url)
        soup = BeautifulSoup(r.content, "html.parser")

        var = soup.find("div", {"class": "chart-item-data"})
        var = var.contents

        title = var[0].text

        var = var[1].contents

        category = var[0].text
        subs = (var[1].text.split())[0]
        subs = float(subs[:-1])
        view = (var[2].text.split())[0]
        view = float(view[:-1]) if "B" in view else float(view[:-1])/1000
        video = (var[3].text.split())[0]
        video = int(video) if not "K" in video else int(float(video[:-1])*1000)
        country = country_names[i]
        i += 1
        addvalue(title, country, category, subs, view, video)

elif process == 2:
    delete()

con.close()

t1 = time.time()
print("Process time:", (str(t1-t0))[:6])
