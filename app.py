import flask
import os
import pandas as pd
import numpy as np



app = flask.Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'for dev')
@app.route("/", methods = ['GET','POST'])
def homepage():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    
    elif flask.request.method == 'POST':
        streams_file = flask.request.files['streams']
        streams_df = pd.read_csv(streams_file,skiprows=[0],index_col='Stream Name')
        streams_df = streams_df.transpose()

        equipment_columns = ['From','To']
        array_of_from_and_to = streams_df[equipment_columns].values.ravel('K')
        equipment = pd.unique(array_of_from_and_to)

        flask.session['equipment'] = equipment.tolist()
        
        return flask.redirect("equipment_selection")

@app.route("/equipment_selection", methods = ['GET','POST'])
def select_equipment():
    equipment_list = flask.session.get('equipment')
    if flask.request.method=='POST':
        data= flask.request.form.getlist('HXunits')
        return data
    else:
        return flask.render_template('equipment_selection',equipment_list = equipment_list)



if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)