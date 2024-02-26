from flask import Flask, redirect
import datetime
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
  page =""
  return page


@app.route('/book')
def bookrent():
  page = ""
  f = open("template/bookrent.html", "r")
  page = f.read()
  f.close()
  return page





app.run(host='0.0.0.0', port=81)