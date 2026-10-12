import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import load_to_csv, load_to_google_sheets

@patch("pandas.DataFrame.to_csv")
def test_load_to_csv(mock_to_csv):
    df = pd.DataFrame({'col1': [1, 2]})
    load_to_csv(df, "test.csv")
    mock_to_csv.assert_called_once()

@patch("gspread.authorize")
@patch("google.oauth2.service_account.Credentials.from_service_account_file")
def test_load_to_google_sheets(mock_creds, mock_authorize):
    df = pd.DataFrame({'Title': ['A']})
    mock_client = MagicMock()
    mock_authorize.return_value = mock_client
    mock_client.open_by_url.return_value.get_worksheet.return_value = MagicMock()
    
    load_to_google_sheets(df, 'fake.json', 'http://fake.com')
    mock_authorize.assert_called_once()