import flask
import pandas as pd
import numpy as np

app = flask.Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def homepage():
    if flask.request.method == 'GET':
        return flask.render_template()
    
    elif flask.request.method == 'POST':
        pass