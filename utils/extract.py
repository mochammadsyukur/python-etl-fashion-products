import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def extract_data(max_pages=50):
    base_url = "https://fashion-studio.dicoding.dev?page="
    all_products = []
    
    for page in range(1, max_pages + 1):
        try:
            response = requests.get(f"{base_url}{page}", timeout=10)
            if response.status_code != 200:
                continue
                
            soup = BeautifulSoup(response.content, 'html.parser')
            products = soup.find_all('div', class_='collection-card') 
            
            for p in products:
                data = {
                    'Title': p.find('h3', class_='product-title').get_text(strip=True) if p.find('h3', class_='product-title') else None,
                    'Price': p.find('span', class_='price').get_text(strip=True) if p.find('span', class_='price') else None,
                    'Rating': p.select_one('p:nth-of-type(1)').get_text(strip=True) if p.select_one('p:nth-of-type(1)') else None,
                    'Colors': p.select_one('p:nth-of-type(2)').get_text(strip=True) if p.select_one('p:nth-of-type(2)') else None,
                    'Size': p.select_one('p:nth-of-type(3)').get_text(strip=True) if p.select_one('p:nth-of-type(3)') else None,
                    'Gender': p.select_one('p:nth-of-type(4)').get_text(strip=True) if p.select_one('p:nth-of-type(4)') else None,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                all_products.append(data)
        except Exception as e:
            print(f"Error on page {page}: {e}")
            
    return pd.DataFrame(all_products)