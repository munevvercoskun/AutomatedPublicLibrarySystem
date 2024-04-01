#test file - Anthony
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/search')
def search():
  return render_template("search.html")

@app.route('/searchResults', methods=['POST'])
def searchResults():
  return render_template("searchResults.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


