import requests
from bs4 import BeautifulSoup

def scrape_prices(base_url, pages=3):
    data = []
    for page in range(1, pages+1):
        url = f"{base_url}/catalogue/page-{page}.html"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            products = soup.find_all('article', class_='product_pod')
            for p in products:
                name = p.h3.a['title'] if p.h3 and p.h3.a else None
                price = p.find('p', class_='price_color').text.strip() if p.find('p', class_='price_color') else None
                data.append({"name": name, "price": price})
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return data
