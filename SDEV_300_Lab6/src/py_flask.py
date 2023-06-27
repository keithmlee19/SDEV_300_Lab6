'''Program that creates a simple website using Python Flask'''
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
now = datetime.now() # current date/time
dt_now = now.strftime("%m/%d/%Y, %H:%M:%S") # format for display

@app.route("/")
def index():
    '''Render index page'''
    return render_template("index.html", dt_now = dt_now)

@app.route("/zebra")
def zebra():
    '''Render Zebra page'''
    return render_template("zebra.html", dt_now = dt_now)

@app.route("/tater")
def tater():
    '''Render Tater page'''
    return render_template("tater.html", dt_now = dt_now)

if __name__ == "__main__":  
    app.run(debug=True) # launch and run with debugging
