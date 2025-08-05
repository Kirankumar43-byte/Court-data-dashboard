import sqlite3

DB = "cases.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
      CREATE TABLE IF NOT EXISTS raw_queries (
        id INTEGER PRIMARY KEY,
        case_type TEXT, case_number TEXT, filing_year TEXT,
        timestamp TEXT, raw_html TEXT
      )""")
    cur.execute("""
      CREATE TABLE IF NOT EXISTS cases (
        id INTEGER PRIMARY KEY,
        query_id INTEGER, party_names TEXT,
        filing_date TEXT, next_hearing TEXT, pdf_link TEXT
      )""")
    conn.commit()
    conn.close()

def save_raw_query(case_type, case_number, filing_year, timestamp, raw_html):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO raw_queries
        (case_type, case_number, filing_year, timestamp, raw_html)
        VALUES (?, ?, ?, ?, ?)""",
        (case_type, case_number, filing_year, timestamp, raw_html))
    conn.commit()
    rowid = cur.lastrowid
    conn.close()
    return rowid

def save_case(query_id, party_names, filing_date, next_hearing, pdf_link):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO cases
        (query_id, party_names, filing_date, next_hearing, pdf_link)
        VALUES (?, ?, ?, ?, ?)""",
        (query_id, party_names, filing_date, next_hearing, pdf_link))
    conn.commit()
    conn.close()
