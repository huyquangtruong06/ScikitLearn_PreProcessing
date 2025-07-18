# 🥣 Cereal Data Preprocessing with Scikit-Learn

📂 This project demonstrates how to perform essential preprocessing steps on a **cereal dataset** using Python and Scikit-Learn.

## 📊 Dataset Description

- Source file: `cereal.csv`
- Contains information about 77 types of cereals and their nutritional values.
- Key columns:
  - `name`, `mfr`, `type`: cereal name and manufacturer/type
  - `calories`, `protein`, `fat`, `sodium`, ...: nutritional attributes
  - `rating`: popularity rating (float)

---

## 🧠 What This Project Covers

### 🔹 Step 1: Import Libraries & Dataset
- import pandas as pd
- import numpy as np
- import seaborn as sns
- import matplotlib.pyplot as plt

### 🔹 Step 2: Handle Missing Values
Print percentage of missing values in each column.

Visualize missing data with a heatmap.

Replace missing numerical values using mean imputation.

📌 Used: SimpleImputer(strategy='mean')

### 🔹 Step 3: Encode Categorical Data
OneHotEncoder for independent variable (x)

LabelEncoder for dependent variable (y)

📌 Used:
- from sklearn.compose import ColumnTransformer
- from sklearn.preprocessing import OneHotEncoder, LabelEncoder

### 🔹 Step 4: Split Data
80% training, 20% testing
📌 Used:
- from sklearn.model_selection import train_test_split

### 🔹 Step 5: Feature Scaling
Apply StandardScaler only to numerical columns (excluding encoded ones).
📌 Used:
- from sklearn.preprocessing import StandardScaler

📈 Output Example
x_test after preprocessing is printed at the end.

📎 Files Included
ScikitLearn_PreProcessing.py – Main Python script

cereal.csv – Raw cereal dataset

README.md – You’re reading it 😄

🚀 How to Run
- python ScikitLearn_PreProcessing.py

📌 Notes
Handles missing values robustly.

Demonstrates full preprocessing pipeline, suitable for feeding into ML models.

You can extend this to build classifiers/regressors for predicting cereal ratings or categories.

✨ Credits
Developed with ❤️ using Python and Scikit-Learn.
Dataset originally sourced from Cereal Dataset - UCI Repository.

