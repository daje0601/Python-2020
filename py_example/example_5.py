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


def change_currency_program(choice1, choice2):
  nation1_before = choice1
  nation2_after = choice2
  print(f"How many {nation1_before} do you want to convert to {nation2_after}?")
  amount_before = input()

  currency_page = f"https://transferwise.com/gb/currency-converter/{nation1_before}-to-{nation2_after}-rate?amount={amount_before}"

  currency = requests.get(currency_page)
  
  currency_data = BeautifulSoup(currency.text, 'html.parser')

  amount_after = currency_data.find('span', {'class':'text-success'}).text

  complete = float(amount_after) * float(amount_before)
  print(f"{nation1_before} {amount_before}is {complete}")


def ask():
  try:
    print("Where are you from? Choose a country by number.")
    choice1 = int(input("#: "))
    if choice1 > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice1]
      before_country = country['code']
    
    print("Now choose another country.")
    choice2 = int(input("#: "))
    if choice2 > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice2]
      after_country = country['code']
      return change_currency_program(before_country, after_country)
  except ValueError:
    print("That wasn't a number.")
    ask()


print("Hello! Please choose select a country by number:")
for index, country in enumerate(countries):
  print(f"{index} {country['name']}")

ask()


# print(format_currency(5000, "KRW", locale="ko_KR"))