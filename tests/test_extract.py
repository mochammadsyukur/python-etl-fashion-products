from utils.extract import extract_data
import pandas as pd

def test_extract_returns_dataframe():
    df = extract_data(max_pages=1)
    assert isinstance(df, pd.DataFrame)