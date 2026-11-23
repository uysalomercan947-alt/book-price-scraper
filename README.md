Book Price Scraper

A simple Python web scraper that collects book titles, prices and stock status from books.toscrape.com (a site built for practicing web scraping) and saves them to a CSV file that opens directly in Excel.

Features
Scrapes multiple pages automatically
Extracts title, price and stock status
Exports clean data to books.csv (Excel-friendly, UTF-8 with BOM)
Waits 1 second between requests to avoid overloading the website
Requirements
Python 3.8 or newer
Libraries: requests, beautifulsoup4
Installation
bash
# 1) Create a virtual environment
python -m venv venv

# 2) Install the libraries (Windows)
.\venv\Scripts\python.exe -m pip install -r requirements.txt

On macOS / Linux use venv/bin/python instead of .\venv\Scripts\python.exe.

Usage
bash
.\venv\Scripts\python.exe price_scraper.py

Output:

Scraping page 1...
Scraping page 2...
Scraping page 3...
Done! 60 books were saved to books.csv

Open books.csv in Excel to see the results.

Example output
title	price	stock
A Light in the Attic	51.77	In stock
Tipping the Velvet	53.74	In stock
Configuration

At the top of price_scraper.py:

Setting	Meaning
BASE_URL	Address of the pages to scrape ({} is replaced by the page number)
PAGE_COUNT	How many pages to scrape (default: 3)

To scrape a different website, change BASE_URL and update the CSS selectors (article.product_pod, p.price_color, p.instock) to match that site's HTML structure.

Responsible scraping

Before scraping a real website, check its robots.txt and terms of service, and keep your request rate low.