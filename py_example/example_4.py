import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")



rows = soup.find("table", {"class":"table table-bordered downloads tablesorter"}).find("tbody").find_all("tr")[1:]

countries = []
for row in rows:
  columns = row.find_all("td")
  name = columns[0].get_text()
  code = columns[2].get_text()
  if columns[1] != "No universal currency":
    country = {
      "name" : name,
      "code" : code
    }
    countries.append(country)

def ask():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      print(f"You chose {country['name']}\nThe currency cod is {country['code']}")
  except ValueError:
    print("That wasn't a number.")
    ask()


print("Hello! Please choose select a country by number:")
for index, country in enumerate(countries):
  print(f"{index} {country['name']}")


ask()
