import streamlit as st
import pandas as pd
import joblib

# Load the trained model, imputer, feature columns, and location means
model = joblib.load('gb_real_estate_model.pkl')
imputer = joblib.load('imputer.pkl')
feature_columns = joblib.load('feature_columns.pkl')
location_means = joblib.load('location_means.pkl')

st.title("🇧🇬 Bulgaria Real Estate Price Predictor")
st.write("This application uses a **Gradient Boosting** machine learning model to predict property prices in Bulgaria.")

# Create user input interface in the sidebar
st.sidebar.header("Property Parameters")

area = st.sidebar.slider("Area (sq.m)", min_value=20, max_value=300, value=85, step=5)
year_built = st.sidebar.slider("Year Built", min_value=1950, max_value=2026, value=2020, step=1)

# Location selection from available ones in the dataset
available_locations = list(location_means.keys()) if isinstance(location_means, dict) else ['Sofia, Center']
selected_location = st.sidebar.selectbox("Location / Region", available_locations)

if st.sidebar.button("Predict Price"):
    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        'area': [area],
        'yearBuilt': [year_built]
    })
    
    # Add location price tier
    if selected_location in location_means:
        input_data['location_price_tier'] = location_means[selected_location]
    else:
        input_data['location_price_tier'] = sum(location_means.values()) / len(location_means)
        
    # Align columns precisely with training features
    input_data = input_data.reindex(columns=feature_columns, fill_value=0)
    
    # Impute and predict
    input_imputed = imputer.transform(input_data)
    predicted_price = model.predict(input_imputed)[0]
    
    # Display result
    st.success(f"### Predicted Price: **{predicted_price:,.2f} EUR**")
    st.info(f"Property with an area of **{area} sq.m**, built in **{year_built}** in **{selected_location}**.")