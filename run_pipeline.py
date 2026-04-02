from scraper import scrape_prices
from cleaner import clean_data
from database import save_to_db

BASE_URL = "http://books.toscrape.com"

def main():
    raw = scrape_prices(BASE_URL, pages=3)
    if not raw:
        print("No data scraped. Check selectors or site availability.")
        return
    df = clean_data(raw)
    save_to_db(df)

if __name__ == "__main__":
    main()
