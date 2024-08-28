
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os

BASE_URL = "https://www.unisap.com"
OUTPUT_DIR = "output"

def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.text

def parse_product_page(soup):
    data = {}
    data["title"] = soup.find("h1", class_="product-title").text.strip()
    data["price"] = soup.find("span", class_="price").text.strip()
    data["description"] = soup.find("div", class_="product-description").text.strip()
    return data

def scrape_category(category_url):
    products = []
    page = 1
    while True:
        url = f"{category_url}?page={page}"
        html = get_page(url)
        soup = BeautifulSoup(html, "html.parser")
        
        product_links = soup.find_all("a", class_="product-link")
        if not product_links:
            break
        
        for link in product_links:
            product_url = BASE_URL + link["href"]
            product_html = get_page(product_url)
            product_soup = BeautifulSoup(product_html, "html.parser")
            product_data = parse_product_page(product_soup)
            products.append(product_data)
            
            # Be nice to the server
            time.sleep(random.uniform(1, 3))
        
        page += 1
    
    return products

def main():
    categories = [
        "/category/electronics",
        "/category/clothing",
        "/category/home-and-garden"
    ]
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    for category in categories:
        print(f"Scraping category: {category}")
        products = scrape_category(BASE_URL + category)
        
        df = pd.DataFrame(products)
        output_file = os.path.join(OUTPUT_DIR, f"{category.split('/')[-1]}.csv")
        df.to_csv(output_file, index=False)
        print(f"Saved {len(products)} products to {output_file}")

if __name__ == "__main__":
    main()
