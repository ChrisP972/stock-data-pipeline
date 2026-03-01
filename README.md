# Stock Data Pipeline & Visualisation
## Overview
This project is a containerised data pipeline designed to fetch financial data from Yahoo Finance, process it into a PostgreSQL database and visualise using Streamlit.

## Architecture
1. Data extracted from Yahoo Finance using yfinance
2. 

## Technologies Used
- Language: Python (yfinance for API calls)
- Database: PostgreSQL
- Dashboard: Streamlit
- Orchestration: Docker

## Quick Start
### Prerequisites
- Docker

### Installation
1. Clone the repository
```
git clone https://github.com/ChrisP972/stock-data-pipeline.git
cd stock-data-pipeline
```

2. Start all services
```
docker compose up --build
```

3. Access Dashboard

    Open: http://localhost:8501

4. Run pipeline for additional stocks
```
docker compose run --rm collect --ticker 
```

## Project Structure
```
stock-data-pipeline
├── app
│   ├── collect_stock_data.py       # Handles Yfinance API calls and ingestion into database
│   ├── db.py                       # Handles Postgres database
│   ├── display.py                  # Handles Streamlit dashboard
├── docker-compose.yaml             # Docker services configuration
├── Dockerfile                      # Docker container instructions
├── pyproject.toml                  # Python project configuration
├── uv.lock                         # UV dependency lock file
```

## Improvements
- Dashboard: Date range filter, advanced metrics, 
- CI/CD: 