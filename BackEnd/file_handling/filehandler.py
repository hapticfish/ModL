from flask import jsonify, request
from app import app
# from flask_uploads import UploadSet, configure_uploads, DATA
from flask_uploads import UploadSet, configure_uploads, DATA, UploadSet
import pandas as pd
import os


#set up the file destination
app.config['UPLOADED_FILES_DEST'] = 'uploads'
files = UploadSet('files', DATA)
configure_uploads(app, files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Check the file format (Excel or CSV)
        file_extension = file.filename.split('.')[-1].lower()
        if file.extension not in ['csv', 'xlsx', 'txt', 'json', ]:
            return jsonify({'error': 'Invalid file format'})

        # Generate a unique filename and save the file
        filename = files.save(file)
        file_path = os.path.join(app.config['UPLOADED_FILES_DEST'], filename)

        # Depending on the file format, load the data using Pandas
        if file_extension == 'csv':
            df = pd.read_csv(os.path.join(app.config['UPLOADED_FILES_DEST'], filename))
            return df
        elif file_extension == 'xlsx':
            df = pd.read_excel(os.path.join(app.config['UPLOADED_FILES_DEST'], filename))
            return df
        elif file_extension == 'json':
            json_file_path = pd.read_json(os.path.join(app.config['UPLOADED_FILES_DEST'], filename))

            if 'orient' in request.form and request.form['orient'] == 'records':
                df = pd.read_json(json_file_path, orient='records')
                return df
            elif 'lines' in request.form and request.form['lines'] == 'true':
                df = pd.read_json(json_file_path, lines=True)
                return df
            else:
                # read normaly
                df = pd.read_json(json_file_path)
                return df

        elif file_extension == 'txt':
                # Detect whether it's tab-separated, pipe-separated, or fixed-width
            if 'delimiter' in request.form:
                    delimiter = request.form['delimiter']
                    if delimiter == 'tab':
                        df = pd.read_csv(file_path, sep='\t')
                        return df
                    elif delimiter == 'pipe':
                        df = pd.read_csv(file_path, sep='|')
                        return df
                    elif delimiter == 'fixed-width':
                        # Define column positions for fixed-width
                        colspecs = [(0,5), (6,12), (13,18)]
                        df = pd.read_fwf(file_path, colspecs=colspecs)
                        return df
            else:
                return jsonify({'error': 'Specify the delimiter for the text file (tab, pipe, or fixed-width)'})
