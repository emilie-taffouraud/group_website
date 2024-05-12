from flask import Flask, render_template, request
import json

app = Flask(__name__)    

@app.route("/")
def index():
    return render_template("homepage.html")

"""
def home():
    with open('companies.json') as f:
        companies = json.load(f)
    return render_template('index.html', companies=companies)"""

if __name__ == '__main__':
    app.run(debug=True)