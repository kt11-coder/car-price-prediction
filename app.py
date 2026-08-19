# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:04:38 2025

@author: kartik
"""

from flask import Flask, request, render_template, abort
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))

# Load the trained model
try:
    model_path = os.path.join(os.path.dirname(__file__), "model_car.pkl")
    model = pickle.load(open(model_path, "rb"))
except FileNotFoundError:
    print("Error: model_car.pkl not found. Make sure the file exists at the specified path.")
    exit(1)

# Define the feature names
FEATURES = [
    "year", "km_driven", "fuel", "seller_type", "transmission",
    "owner", "seats", "max_power", "Mileage", "Engine (CC)"
]

# Define categorical features that need encoding
CATEGORICAL_FEATURES = ["fuel", "seller_type", "transmission", "owner"]

def process_input(data):
    """
    Convert input data into a format suitable for prediction.
    Handles both numeric and categorical features.
    """
    try:
        # Convert numerical features to float
        numeric_data = {key: float(data[key]) for key in FEATURES if key not in CATEGORICAL_FEATURES}
        
        # Convert categorical features to strings (if they exist in the input)
        categorical_data = {key: data[key] for key in CATEGORICAL_FEATURES if key in data}

        # Combine numeric and categorical data
        processed_data = {**numeric_data, **categorical_data}

        # Convert to DataFrame (since the model expects a DataFrame)
        processed_data_df = pd.DataFrame([processed_data])

        return processed_data_df

    except KeyError as e:
        abort(400, f"Missing input field: {e}")
    except ValueError:
        abort(400, "Invalid input: Ensure numeric fields contain valid numbers.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the form data
    data = request.form.to_dict()

    # Process the input data
    processed_data_df = process_input(data)

    # Make a prediction
    prediction = float(model.predict(processed_data_df)[0])

    # Check if prediction.html exists
    prediction_template_path = os.path.join("templates", "prediction.html")
    if not os.path.exists(prediction_template_path):
        return "Error: prediction.html file not found!", 500

    return render_template("prediction.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
