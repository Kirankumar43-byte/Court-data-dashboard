from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def fetch_case(case_type, case_number, filing_year):
    with sync_playwright() as pw:
        browser = pw.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto("https://delhihighcourt.nic.in/")
        # Replace selectors with real site-specific ones:
        page.select_option("select#caseType", case_type)
        page.fill("input#caseNumber", case_number)
        page.fill("input#filingYear", filing_year)
        page.click("button#searchBtn")
        page.wait_for_selector("table.results")
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")
    # Actual parsing logic for Delhi High Court site
    parties = soup.select_one(".parties").get_text(strip=True)
    filing = soup.select_one(".filingDate").get_text(strip=True)
    hearing = soup.select_one(".nextHearing").get_text(strip=True)
    pdf = soup.select_one("a.pdfLink")["href"]
    return {
        "raw_html": html,
        "party_names": parties,
        "filing_date": filing,
        "next_hearing": hearing,
        "pdf_link": pdf
    }
