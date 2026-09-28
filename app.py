from flask import Flask, render_template, request
from scrapper import search_incruit

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")

@app.route("/python")
def python() :
  return render_template("python.html") # 템플릿 폴더 안의 자료가 있어야 실행 됨

@app.route("/search")
def search() :
  keyword = request.args.get("keyword")
  jobs = search_incruit(keyword)
  return render_template("search.html", keyword=keyword, jobs= enumerate(jobs))

if __name__ == "__main__":
  app.run(debug = True)
