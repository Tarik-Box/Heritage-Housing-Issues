import streamlit as st
import joblib
import numpy as np
import pandas as pd

@st.cache_resource
def load_model():
    """Loads the trained ML model from the .joblib file and caches it."""
    try:
        model = joblib.load('outputs/v1/heritage_housing_model.joblib')
        return model
    except FileNotFoundError:
        return None

@st.cache_data
def load_inherited_houses_data():
    """Loads the data for the 4 inherited houses."""
    try:
        df = pd.read_csv('src/four_houses_data.csv')
        return df
    except FileNotFoundError:
        return None

def page_3_price_prediction_body():
    """Displays the Price Prediction page content."""
    st.header("Price Prediction")
    st.write("---")

    # Load the trained model and data
    model = load_model()
    inherited_houses_df = load_inherited_houses_data()

    if model is None:
        st.error("Error: Model file not found. Please ensure 'heritage_housing_model.joblib' is in the 'outputs/v1/' directory.")
        return
    
    if inherited_houses_df is None:
        st.error("Error: Inherited houses data not found. Please ensure 'four_houses_data.csv' is in the 'src/' directory.")
        return

    # Section for the 4 inherited houses
    st.subheader("Predictions for Inherited Houses")
    st.write(
        "This section displays the predicted sale price for the client's four inherited properties "
        "based on their key attributes."
    )
    
    # Predict prices and add to dataframe
    predictions = model.predict(inherited_houses_df)
    inherited_houses_df['PredictedSalePrice'] = predictions

    st.dataframe(inherited_houses_df.style.format({
        "GrLivArea": "{:,.0f}",
        "PredictedSalePrice": "${:,.2f}"
    }))

    # Calculate and display the summed price
    summed_price = predictions.sum()
    st.success(
        f"**The summed predicted price for all 4 inherited houses is: ${summed_price:,.2f}**"
    )

    st.write("---")

    # Section for predicting any house (the existing functionality)
    st.subheader("Predict the Price of Any House")
    st.info(
        "Use the sliders below to predict the sale price for any house by providing its characteristics."
    )

    # Input widgets for features
    overall_qual = st.slider(
        'Overall Quality (Overall material and finish quality)',
        min_value=1, max_value=10, value=5, step=1,
        help="Rates the overall material and finish of the house (1-Very Poor, 10-Very Excellent)"
    )

    gr_liv_area = st.slider(
        'Above Ground Living Area (Square Feet)',
        min_value=334, max_value=5642, value=1500, step=10,
        help="Above grade (ground) living area square feet"
    )

    # Prediction button
    if st.button('Predict Sale Price'):
        input_data = pd.DataFrame([[overall_qual, gr_liv_area]], columns=['OverallQual', 'GrLivArea'])
        prediction = model.predict(input_data)[0]
        st.success(f"**Predicted Sale Price for the custom house: ${prediction:,.2f}**")
