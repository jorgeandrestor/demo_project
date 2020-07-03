# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template,request
import model
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template("index.html",now=datetime.now())



#pick the spiciness routes here
@app.route('/jokes', methods=['GET','POST'])

def jokes():
    language = request.form["language"]
    savage_level = request.form["spiciness"]
    
    return render_template("jokes.html",language=language, savage_level=savage_level, now=datetime.now())
