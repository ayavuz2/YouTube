import requests
from bs4 import BeautifulSoup
import  _sqlite3

main_url = "https://watchin.today/charts/channel/country"

r = requests.get(main_url)
soup = BeautifulSoup(r.content, "html.parser")

var = soup.find_all("a", {"class":"nps-item"})
var = var[: len(var) - 14]

link_list = []
for link in var:
    link_list.append(link.get("href"))

print(link_list)