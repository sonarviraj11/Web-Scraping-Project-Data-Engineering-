# 📊 Price Tracking Pipeline (B2B Data Engineering Project)

An end-to-end automated data pipeline designed to collect, transform, and deliver job market data for business use cases such as recruitment analytics, hiring trends, and talent intelligence.

## 🎯 Objective

Organizations rely heavily on job market insights to make strategic decisions — from hiring to competitor analysis. However, collecting such data manually is inefficient and unreliable.

This project solves that by building a **fully automated pipeline** that:
- Extracts job listings from a public web source
- Processes and standardizes raw data
- Stores it in a structured database
- Makes it accessible through a REST API

## 🏗️ System Design

The pipeline follows a modular architecture:
Data Source → Scraper → Data Processing → Database → API Layer

Each stage is independent, ensuring flexibility and scalability.

## 📁 Directory Layout

Web_Scrapper_project/

├── scraper.py # Data extraction logic
├── cleaner.py # Data transformation & cleaning
├── database.py # Database insertion script
├── run_pipeline.py # Pipeline orchestrator
├── app.py 
└── README.md

## 🛠️ Tools & Technologies

- **Python** – Core programming language  
- **BeautifulSoup + Requests** – Web scraping  
- **Pandas** – Data transformation  
- **MySQL** – Data storage  
- **FastAPI** – API development  
- **Uvicorn** – ASGI server  

## 🔄 Pipeline Workflow

### Step 1: Data Extraction
- Scrapes job listings from a public website
- Handles pagination and structured parsing
- Outputs raw data into CSV format

### Step 2: Data Transformation
- Removes duplicates and inconsistencies
- Normalizes text fields
- Extracts structured attributes (e.g., region)
- Produces a clean dataset

### Step 3: Data Storage
- Loads processed data into MySQL
- Ensures structured schema for querying

### Step 4: Data Serving
- Exposes data through REST API endpoints
- Enables integration with dashboards or applications
