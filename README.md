# Court-data-dashboard
Here,you can access the indian court laws and cases
# Court-Data Fetcher & Mini-Dashboard

This Flask-based app takes user inputs (Case Type, Number, Filing Year), scrapes the Delhi High Court public site, and displays case metadata and latest order PDF.

## Features
- Input form for search
- Scrapes parties, filing & hearing dates, PDF link
- SQLite backend logging raw HTML & results
- Error handling for invalid input or page changes

## Setup
1. Clone repo  
2. `pip install -r requirements.txt`  
3. Install Playwright browsers: `playwright install firefox`  
4. `python app.py` and visit [http://localhost:5000](http://localhost:5000)

## Docker
```bash
docker build -t court-fetcher .
docker run -p 5000:5000 court-fetcher
