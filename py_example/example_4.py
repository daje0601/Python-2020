import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

countries = []
nmuber_code = []
number_country = []
rows = soup.find("table", {"class":"table table-bordered downloads tablesorter"}).find("tbody").find_all("tr")
for row in rows:
  columns = row.find_all("td")
  if columns[1] != "No universal currency":
    country = columns[0].get_text()
    code = columns[2].get_text()
    number = columns[3].get_text()
    dict1 = {
      number : code 
    },
    dict2 = {
      number : country
    }
    nmuber_code.append(dict1)
    number_country.append(dict2)
    countries.append(country)

def printing_country():
  print("Hello! Please choose select a country by number:")
  x = 0
  for country in countries:
    x = x + 1
    print("#", x, country)

def ask():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    elif nmuber_code[choice] :
      print(nmuber_code.value)
  except ValueError:
    print("That wasn't a number.")
    ask()

printing_country()
ask()
