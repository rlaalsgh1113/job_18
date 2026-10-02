from flask import Flask, render_template, request, redirect
from scrapper import search_all

app = Flask(__name__)

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword", "").strip()

    if keyword == "":
        return redirect("/")

    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = search_all(keyword, pages=1)
        db[keyword] = jobs

    incruit_count = len([job for job in jobs if job["site"] == "인크루트"])
    saramin_count = len([job for job in jobs if job["site"] == "사람인"])

    return render_template(
        "search.html",
        keyword=keyword,
        jobs=jobs,
        incruit_count=incruit_count,
        saramin_count=saramin_count
    )


if __name__ == "__main__":
    app.run(debug=True)
