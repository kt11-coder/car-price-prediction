# 🚗 Car Price Prediction

A machine learning web application that predicts the price of a car based on user-provided car details.

The project uses a trained machine learning model and a Flask web application to provide predictions through a simple web interface. The application is deployed online using Render.

## 🌐 Live Demo

👉 **Live Application:**  
PASTE-YOUR-RENDER-URL-HERE

## 📌 Project Overview

Car prices depend on several factors such as the characteristics of the vehicle and its specifications.

This project uses machine learning to estimate the price of a car from the input provided by the user.

The trained model is integrated with a Flask backend, while HTML and CSS are used to create the user interface.

## ✨ Features

- 🚗 Car price prediction
- 🤖 Machine learning based prediction
- 🌐 Flask web application
- 📊 Trained prediction model
- 🖥️ Simple and user-friendly interface
- ⚡ Real-time prediction through the web interface
- ☁️ Deployed online using Render

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- XGBoost
- NumPy
- Pandas
- Joblib

### Web Development
- Flask
- HTML
- CSS

### Deployment
- Render
- Gunicorn

## 📂 Project Structure

```text
car-price-prediction/
│
├── app.py
├── train_model.py
├── car_price.csv
├── model_car.pkl
├── requirements.txt
├── Procfile
├── style.css
│
└── templates/
    ├── index.html
    └── prediction.html
