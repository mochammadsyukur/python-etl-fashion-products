import pandas as pd
import re

def transform_data(df):
    if df.empty:
        return df

    # 1. Hapus Duplikat & Null
    df = df.drop_duplicates().dropna()

    # 2. Filter data invalid
    invalid_pattern = r'.*\.(jpg|jpeg|png|gif|webp)$|Unknown Product'
    df = df[~df['Title'].str.contains(invalid_pattern, case=False, na=False)]
    df = df[~df['Price'].str.contains(invalid_pattern, case=False, na=False)]
    df = df[~df['Rating'].str.contains(invalid_pattern, case=False, na=False)]

    # 3. Transformasi Price (USD -> IDR 16.000)
    def clean_price(val):
        num = re.sub(r'[^\d.]', '', str(val))
        return float(num) * 16000 if num else 0.0
    
    df['Price'] = df['Price'].apply(clean_price)

    # 4. Transformasi Rating (Float)
    def clean_rating(val):
        match = re.search(r'(\d+\.?\d*)', str(val))
        return float(match.group(1)) if match else 0.0
    
    df['Rating'] = df['Rating'].apply(clean_rating)

    # 5. Transformasi Colors (Angka saja)
    df['Colors'] = df['Colors'].str.extract(r'(\d+)').fillna(0).astype(int)

    # 6. Transformasi Size & Gender (Hapus prefix)
    df['Size'] = df['Size'].str.replace(r'(?i)Size:\s*', '', regex=True).str.strip()
    df['Gender'] = df['Gender'].str.replace(r'(?i)Gender:\s*', '', regex=True).str.strip()

    return df