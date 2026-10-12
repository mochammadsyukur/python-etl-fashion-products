# Python ETL Pipeline — Fashion Product Data

A Python learning project that extracts public demo product listings, cleans and transforms their fields, and exports a structured CSV. Written as part of a data-processing course; **not a production ingestion service**.

## What is included
- `utils/extract.py` — request and parse product listings from the Dicoding demo website using `requests` and BeautifulSoup.
- `utils/transform.py` — remove invalid/duplicate rows and normalize price, ratings, sizes and other product attributes using pandas.
- `utils/load.py` — write a CSV; optional Google Sheets support is implemented but disabled in `main.py`.
- `tests/` — basic Python tests, including a mocked Sheets API test.

## Technology
Python · pandas · Requests · Beautiful Soup · pytest · optional gspread / Google APIs.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

The extraction step requires an internet connection and depends on the external demo site (`fashion-studio.dicoding.dev`), which may change or become unavailable. The generated `products.csv` is ignored by Git.

## Testing

```bash
pytest tests/test_transform.py tests/test_load.py -q
```

`tests/test_extract.py` makes a live website request; run it separately only when you have internet access.

## Technical caveats
- Currency normalization uses a **hard-coded teaching assumption** of IDR 16,000 per USD. It is not a live exchange-rate conversion.
- Google Sheets export requires your own service-account credentials and sheet URL. **Never commit secrets**; the placeholder configuration file from the learning archive is intentionally excluded.
- This repository is a course project showing an ETL workflow, rather than a claim of professional production deployment.

## Author / context
Mochammad Syukur Alhamdulillah — educational Python project.
