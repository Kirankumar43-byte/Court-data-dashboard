from flask import Flask, render_template, request
from scraper import fetch_case
from models import init_db, save_raw_query, save_case
from datetime import datetime

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    if request.method == "POST":
        ct = request.form["case_type"]
        cn = request.form["case_number"]
        fy = request.form["filing_year"]
        try:
            data = fetch_case(ct, cn, fy)
        except Exception as e:
            error = f"Error fetching case: {e}"
            return render_template("form.html", error=error)

        timestamp = datetime.now().isoformat()
        rq_id = save_raw_query(ct, cn, fy, timestamp, data["raw_html"])
        save_case(rq_id, data["party_names"], data["filing_date"],
                  data["next_hearing"], data["pdf_link"])

        return render_template("result.html", metadata=data)
    return render_template("form.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
