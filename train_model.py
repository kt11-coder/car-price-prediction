# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:07:56 2025

@author: kartik
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import xgboost as xgb
import pickle
import os

# Load the dataset
file_path = os.path.join(os.path.dirname(__file__), "car_price.csv")
df = pd.read_csv(file_path)

# Rename the column for convenience
df = df.rename(columns={'max_power (in bph)': 'max_power'})

# Define features and target
X = df.drop(columns=['selling_price', 'Unnamed: 0','name','Mileage Unit'])
y = df['selling_price']
# print(X)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocess the data
numeric_features = ['year', 'km_driven', 'seats', 'max_power', 'Mileage', 'Engine (CC)']
categorical_features = ['fuel', 'transmission', 'owner', 'seller_type']
# print(X.columns)
# 
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median'))
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Create a pipeline that preprocesses the data and then fits a model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(n_estimators=100, random_state=42))
])

# Train the model
model.fit(X_train, y_train)
model.score(X_test,y_test)

#Save the trained model to a file
with open('model_car.pkl', 'wb') as file:
     pickle.dump(model, file)

print("Model saved as model.pkl")