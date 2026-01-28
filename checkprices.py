from bs4 import BeautifulSoup
import requests
import csv
import datetime

url = "https://books.toscrape.com/"

target_price = 49.99

def check_prices():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    price = float(soup.find("p", class_="price_color").text[2:])

    print(f"Current price: £{price}")

    if price < target_price:
        print("The competitor's price is lower than your target price.")


    with open("prices.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.date.today(), "A Light in the Attic", price])

if __name__ == "__main__":
    check_prices()













