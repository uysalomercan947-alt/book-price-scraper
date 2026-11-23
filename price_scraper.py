import csv
import re
import time

import requests
from bs4 import BeautifulSoup

# A website made for practicing web scraping
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
PAGE_COUNT = 3  # how many pages to scrape


def scrape_page(page_number):
    """Return a list of all books found on one page."""
    url = BASE_URL.format(page_number)

    # 1) Download the page
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        print(f"Page {page_number} could not be opened (code: {response.status_code})")
        return []

    response.encoding = "utf-8"

    # 2) Turn the raw HTML text into an object we can search
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    # 3) Every book on the page sits inside an <article class="product_pod">
    for card in soup.select("article.product_pod"):
        title = card.h3.a["title"]
        price_text = card.select_one("p.price_color").text   # e.g. "£51.77"
        price = float(re.sub(r"[^0-9.]", "", price_text))     # keep only digits and dot
        stock = card.select_one("p.instock").text.strip()
        books.append({"title": title, "price": price, "stock": stock})

    return books


def main():
    all_books = []

    # Visit pages 1, 2, 3 one by one
    for number in range(1, PAGE_COUNT + 1):
        print(f"Scraping page {number}...")
        all_books.extend(scrape_page(number))
        time.sleep(1)  # wait 1 second so we do not overload the website

    # Write everything to a CSV file that Excel can open
    # utf-8-sig makes sure special characters look right in Excel
    with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price", "stock"])
        writer.writeheader()
        writer.writerows(all_books)

    print(f"Done! {len(all_books)} books were saved to books.csv")


if __name__ == "__main__":
    main()