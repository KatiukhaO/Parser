import requests
from bs4 import BeautifulSoup
from config import URL, FILE_NAME
import csv


def get_html(url):
    page = requests.get(URL)
    return page


def get_content(html):
    soup = BeautifulSoup(html.content, "html.parser")
    items = soup.find_all("div", class_="_3DNsL _3yOEq")

    cards = []

    for item in items:
        cards.append(
            {
                "name": item.find("div", class_="_1bfj5").find("h3").get_text(strip=True).split(","),
                "price": item.find("div", class_="_24XLO").find("span", class_="_2-l9W").get_text(strip=True).replace(
                    ",", ".")
            }
        )

    return cards


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        item = get_content(html)
        save_doc(item, FILE_NAME)

    else:
        print("Error, we dont get html page")


def save_doc(list_items, path):
    with open(path, "w", encoding="utf-16") as file:
        writer = csv.writer(file)
        writer.writerow(["country", "region", "price"])
        for i in list_items:
            writer.writerow([i["name"][0], i["name"][-1], i["price"]])


if __name__ == '__main__':
    parser()