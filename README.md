# Competitor Price Tracking Pipeline

## 📌 Problem
Businesses often need competitor pricing data but don’t have an easy way to collect it.  
This project builds a **data pipeline** that scrapes product prices from public websites, cleans the data, stores it in a database, and exposes an API endpoint for business use.


## ⚙️ Features
- Scraper with pagination & error handling
- Data cleaning (missing values, standardized formats)
- Automated pipeline storing data in SQLite
- Flask API endpoint (`/prices`) to serve results
- Bonus: Simple ML trend predictor

## Tech Stack
Python, BeautifulSoup, Pandas, SQLite, FastAPI, Scikit-learn

## How to Run
pip install -r requirements.txt  
python run_pipeline.py  
python run app.py 

## Future Improvements
- Real-time scraping
- Dashboard (React/Power BI)
- Advanced ML forecasting

