import flask
import pandas as pd
import numpy as np



app = flask.Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def homepage():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    
    elif flask.request.method == 'POST':
        streams_file = flask.request.files['streams']
        streams_df = pd.read_csv(streams_file,skiprows=[0])
        streams_df = streams_df.transpose()
        print(streams_df.head(50))
        return streams_df.to_html()

if __name__ == "__main__":
    app.run()