from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user  = { 'nickname' : 'Splin' }
    posts = [
                {
                    'author':{'nickname':'John'},
                    'body':'Beautiful day in Portland!'
                }
            ]
    return render_template("index.html",
                           title = 'Home',
                           user  = user['nickname'],
                           posts = posts) 
