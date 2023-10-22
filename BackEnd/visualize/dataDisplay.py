from flask import jsonify, request
from app import app
from BackEnd.analysis.preprocessing import upload_file

"""Returns the uploaded file as json data to be displayable on the front end for review"""


@app.route('/datasetDisplay', methods=['GET'])
def preprocess_data():
    df = upload_file()
    json_data = df.to_json(orient='records')
    return json_data


@app.route('/dataVisualizations', methods=['GET'])
def preprocess_data():
    return ""
