from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_google_sheets

def run_pipeline():
    print("Extracting data...")
    raw_df = extract_data(max_pages=50)
    
    print("Transforming data...")
    clean_df = transform_data(raw_df)
    
    SHEET_URL = ""
    
    load_to_csv(clean_df)
    # load_to_google_sheets(clean_df, 'google-sheets-api.json', SHEET_URL)
    
    print(f"Process completed. {len(clean_df)} records processed.")

if __name__ == "__main__":
    run_pipeline()