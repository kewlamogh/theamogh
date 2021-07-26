from flask import Flask, render_template
from os import system as sys
app = Flask('app', template_folder = "pages", static_folder = 'static', debug = False)

@app.route('/')
def home():
  return render_template("not-article/home.html")
@app.route('/halo5tips')
def htips():
  return render_template("articles/halo5tips.html")
@app.route('/humpty')
def humpty():
  return render_template("articles/humptydumpty.html")
@app.route('/pytutorial')
def pytut():
  return render_template("articles/python-tutorial.html")


app.run(host='0.0.0.0', port=8080)
sys('clear')