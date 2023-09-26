import flask
import pandas as pd
import numpy as np

app = flask.Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def homepage():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    
    elif flask.request.method == 'POST':
        pass

if __name__ == "__main__":
    app.run()