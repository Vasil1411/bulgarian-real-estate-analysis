Markdown
# 🏢 Bulgarian Real Estate Price Analysis & Prediction

A data science project focused on scraping, cleaning, exploring, and predicting apartment prices in Bulgaria using data from `imot.bg`.

## 📌 Project Overview
The goal of this project is to analyze the Bulgarian real estate market (focusing on apartment sales), clean and preprocess raw scraped data, handle missing values and outliers, and build a reliable machine learning model to predict property prices based on features like area, construction type, location, and year built.

## 🗂️ Project Structure
property-analyses/
│
├── raw/                  # Raw scraped CSV datasets from imot.bg
├── processed/            # Cleaned and filtered datasets ready for modeling
├── notebooks/            # Jupyter Notebooks for EDA and data cleaning
└── README.md             # Project documentation


## 🧹 Data Cleaning & Preprocessing Steps
1. **Column Selection:** Removed redundant English/Bulgarian duplicates, image URL columns (`imageUrls/*`), and empty metadata (`publishedDate`).
2. **Data Type Correction:** Converted floats to integers for features like `yearBuilt`, `floor`, and `totalFloors`.
3. **Outlier Removal:** Filtered out unrealistic real estate anomalies (e.g., extreme property areas above 400 sqm or below 15 sqm, and invalid prices per square meter).
4. **Missing Values Handling:** Handled missing values using median imputation and categorical placeholders where necessary.

## 🛠️ Built With
* **Python** 
* **Pandas & NumPy** – Data manipulation and cleaning
* **Jupyter Notebook** – Interactive development environment
* **Scikit-Learn** *(upcoming)* – Machine learning modeling

## 🚀 Future Steps
* Feature encoding (handling categorical variables like `constructionType` and `neighborhoodBg`).
* Training regression models (Linear Regression, Random Forest, XGBoost) to predict apartment prices.
* Evaluating model performance using MAE, RMSE, and $R^2$ scores.