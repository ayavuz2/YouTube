import requests
from bs4 import BeautifulSoup
import  _sqlite3

"""
def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS TopChannelsByCountry(Title TEXT, Category TEXT, Subscribe TEXT, View TEXT, Video TEXT)")

def addValue(title,category,subs,view,video):
    cursor.execute("INSERT INTO TopChannelsByCountry(Title, Category, Subscribe, View, Video) VALUES(?,?,?,?,?)", (title,category,subs,view,video))
    con.commit()

def delete():
    cursor.execute("DELETE FROM TopChannelsByCountry")
    con.commit()

con = _sqlite3.connect("youtube.db")
cursor = con.cursor()
"""

main_url = "https://watchin.today"

r = requests.get("https://watchin.today/charts/channel/country")
soup = BeautifulSoup(r.content, "html.parser")

var = soup.find_all("a", {"class":"nps-item"})
var = var[: len(var) - 14]

link_list = []
for link in var:
    link_list.append(link.get("href"))

"""
current_url = main_url + link_list[0]
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
"""

"""
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
"""

#delete()
#con.close()