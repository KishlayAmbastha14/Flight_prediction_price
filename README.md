# ✈️ Flight Price Prediction

## 📌 Project Overview

This project predicts flight ticket prices for Indian domestic airlines based on multiple features such as airline, source city, departure time, stops, arrival time, destination city, travel class, flight duration, and days left until departure.
The model uses Random Forest Regression along with a preprocessing pipeline to handle categorical and numerical features.

### 🎯 Objective

The main goal is to accurately predict flight prices so that travelers can make informed decisions and plan their bookings effectively.

### 📂 Dataset

Source: Indian Flight Dataset from Kaggle

#### Features:

airline

source_city

departure_time

stops

arrival_time

destination_city

class

duration

days_left

Target Variable: price

Note: Column flight was dropped (non-informative identifiers like UK-82, AI-43).

## 🛠️ Tools & Technologies

Programming Language: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

Model: RandomForestRegressor

Preprocessing: ColumnTransformer (OneHotEncoder, OrdinalEncoder, StandardScaler)

Pipeline: Scikit-Learn Pipeline (preprocessing + model training)

## Data Preprocessing & EDA

1️⃣ Initial Cleaning

Checked dataset shape, nulls, and duplicates

Dropped unnamed columns

2️⃣ Exploratory Data Analysis (EDA)

Visualized distributions and outliers using Matplotlib & Seaborn

Plots used: kdeplot, histplot, boxplot

3️⃣ Feature Engineering & Selection

Dropped non-informative flight column

Identified categorical and numerical features for encoding

4️⃣ Encoding & Scaling

OneHotEncoder for nominal categorical features

OrdinalEncoder for ordinal features

StandardScaler for numerical features

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


## Pipeline
<img width="770" height="225" alt="flight_pipeline" src="https://github.com/user-attachments/assets/c0830032-1d3a-4d09-873f-2e345d1fe855" />



## 🤖 Modeling

Train-Test Split:

Features (X): all except price

Target (y): price

Pipeline Setup:

Preprocessing with ColumnTransformer

Model: RandomForestRegressor

Model Score:

R² ≈ 98%

## 📊 Model Evaluation

<details>

Sample Predictions

Actual  	Predicted

2098	  2097.24

7221	  7221.00

5955	  6473.07

2844	  3759.54

5954	  6204.12

9840	  10335.60

4020	  4020.00

2410	  2410.00

4496	  4542.20

3918	  3328.31

</details>

### Metrics
R² Score: 0.98

![Python](https://img.shields.io/badge/Python-3.10-blue) 
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange)
![RandomForest](https://img.shields.io/badge/Model-RandomForest-green)
