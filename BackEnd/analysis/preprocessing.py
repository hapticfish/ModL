from flask import jsonify, request
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

from app import app
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from BackEnd.file_handling.filehandler import upload_file


@app.route('/preprocess', methods=['POST'])
def preprocess_data():
    data = request.json  # Receive the data and preprocessing options from the frontend

    # Extract data from the JSON request
    features = data['features']
    target_column = data['targetColumn']
    test_size = data['testSize']
    random_state = data['randomState']
    model_type = data['modelType']

    # Select the target column
    target = features[target_column]
    features = features.drop(columns=[target_column])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=test_size, random_state=random_state)

    # Train your machine learning model based on the model_type
    if model_type == 'LinearRegression':
        model = LinearRegression()
    else:
        # Add other model choices here
        pass

    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate MSE and R2
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Create a scatter plot
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs. Predicted Values')

    # Save the plot as an image
    plt.savefig('scatter_plot.png')

    # Convert the image to base64 for sending to React
    with open('scatter_plot.png', 'rb') as image_file:
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')

    # Prepare the data to send back to React
    response_data = {
        "message": "Data preprocessed and model trained successfully",
        "mse": mse,
        "r2": r2,
        "scatter_plot": image_base64
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
