from flask import jsonify, request
from app import app
from BackEnd.analysis.preprocessing import upload_file

"""Returns the uploaded file as json data to be displayable on the front end for review"""


@app.route('/datasetDisplay', methods=['GET'])
def displayDataSet():
    df = upload_file()
    json_data = df.to_json(orient='records')
    return json_data

"""returns the preliminal exploritory data: df.info, df.describe to the front end"""
@app.route('/dataExplore', methods= ['GET'])
def upLoadExploreData():
    df = upload_file()
    dfInfo = df.info()
    dfDescription = df.describe()

    explorerData = {
        'info': dfInfo,
        'description': dfDescription
    }

    return explorerData



@app.route('/dataVisualizations', methods=['GET'])
def upLoadFinalVisuals():
    return ""
