import gspread
from google.oauth2.service_account import Credentials

def load_to_csv(df, filename="products.csv"):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def load_to_google_sheets(df, json_key_path, spreadsheet_url):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(json_key_path, scopes=scope)
        client = gspread.authorize(creds)
        
        sh = client.open_by_url(spreadsheet_url)
        worksheet = sh.get_worksheet(0)
        
        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("Data successfully loaded to Google Sheets.")
    except Exception as e:
        print(f"Failed to load to Google Sheets: {e}")