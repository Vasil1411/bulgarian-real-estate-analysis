# 🏢 Bulgarian Real Estate Price Analysis & Prediction

An end-to-end data science project focused on scraping, cleaning, exploring, and predicting apartment prices in Bulgaria using data from imot.bg, wrapped in an interactive web application.

## 🚀 Live Demo
👉 [Test the Real Estate Price Predictor on Streamlit Cloud](https://your-app-url.streamlit.app)

## 📌 Project Overview
The goal of this project is to analyze the Bulgarian real estate market (focusing on apartment sales), clean and preprocess raw scraped data, handle missing values, and build a reliable machine learning model (`Gradient Boosting Regressor`) to predict property prices based on features like area, location, and year built.

## 🗂️ Project Structure
property-analyses/
│
├── raw/                  # Raw scraped CSV datasets from imot.bg
├── processed/            # Cleaned and filtered datasets ready for modeling
├── notebooks/            # Jupyter Notebooks for EDA, data cleaning & training
├── app.py                # Streamlit web application script
├── requirements.txt      # Python dependencies for deployment
├── *.pkl                 # Serialized model, imputer, and feature columns
└── README.md             # Project documentation

## 🧹 Data Cleaning & Preprocessing Steps
1. **Column Selection:** Removed redundant duplicates, image URL columns, and empty metadata.
2. **Data Type Correction:** Converted floats to integers for features like `yearBuilt`, `floor`, and `totalFloors`.
3. **Outlier Removal:** Filtered out unrealistic real estate anomalies (extreme property areas and invalid prices).
4. **Missing Values Handling:** Handled missing values using median imputation and target encoding for locations (`location_price_tier`).

## 🛠️ Built With & Tech Stack
- **Python**
- **Pandas & NumPy** – Data manipulation and feature engineering
- **Scikit-Learn** – Gradient Boosting Regressor machine learning pipeline
- **Streamlit** – Interactive web app development and cloud deployment
- **Joblib** – Model serialization
