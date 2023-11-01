from flask import jsonify, request
from app import app
from BackEnd.analysis.preprocessing import upload_file

"""Returns the uploaded file as json data to be displayable on the front end for review"""


@app.route('/datasetDisplay', methods=['GET'])
def displaydataset():
    df = upload_file()
    json_data = df.to_json(orient='records')
    return json_data

"""returns the preliminal exploritory data: df.info, df.describe to the front end"""
@app.route('/dataExplore', methods= ['GET'])
def uploadexploredata():
    df = upload_file()
    df_info = df.info()
    df_description = df.describe()

    explorer_data = {
        'info': df_info,
        'description': df_description
    }

    return explorer_data



@app.route('/dataVisualizations', methods=['GET'])
def upLoadFinalVisuals():
    return ""
