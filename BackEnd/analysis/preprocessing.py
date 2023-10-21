from flask import Flask, jsonify, request
from app import app
# from flask_uploads import UploadSet, configure_uploads, DATA
from flask_uploads import UploadSet, configure_uploads, DATA, UploadSet
import pandas as pd
import os
from BackEnd.fileHandling.fileHandler import upload_file



@app.route('/preprocess', methods=['POST'])
def preprocess_data():
    df = upload_file;

    # data = request.json['data'] # Receive the data to be preprocessed
    preprocessing_options = request.json['options'] # Receive the user's preprocessing options

    # More preprocessing steps based on user input


    # For example, encoding categorical data
    if 'encodingMethod' in preprocessing_options:
        if preprocessing_options['encodingMethod'] == 'one-hot':
            df = pd.get_dummies(df, columns=['categorical_column'])
        elif preprocessing_options['encodingMethod'] == 'label':
            df['categorical_column'] = df['categorical_column'].astype('category').cat.codes

    #selecting columns to drop and clean
    if 'selectedColumns' in preprocessing_options:
        df = df.drop(columns=preprocessing_options['selectedColumns'])

    if __name__ == '__main__':
        app.run(debug=True)