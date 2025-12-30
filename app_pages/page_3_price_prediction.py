import streamlit as st
import joblib
import numpy as np
import pandas as pd

def page_3_price_prediction_body():
    """Displays the Price Prediction page content."""
    st.header("Price Prediction")
    st.write("---")

    st.info(
        "Use this page to get an instant prediction of a house's sale price "
        "based on its characteristics. Adjust the sliders below to define "
        "the 'Overall Quality' and 'Above Ground Living Area' of the property."
    )

    # Load the trained model
    try:
        model = joblib.load('src/heritage_housing_model.joblib')
    except FileNotFoundError:
        st.error("Error: Model file not found. Please ensure 'heritage_housing_model.joblib' is in the 'src/' directory.")
        return

    # Define features for input (based on what the model was trained on)
    # Our model was trained on 'OverallQual' and 'GrLivArea'
    st.subheader("Input House Features")

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

    # Create a DataFrame for prediction
    # Ensure column names match the features used during training
    input_data = pd.DataFrame([[overall_qual, gr_liv_area]], columns=['OverallQual', 'GrLivArea'])

    st.write("---")

    # Prediction button
    if st.button('Predict Sale Price'):
        prediction = model.predict(input_data)[0]
        # Display prediction
        st.success(f"**Predicted Sale Price: ${prediction:,.2f}**")
        st.write(
            "This prediction is based on the selected 'Overall Quality' and 'Above Ground Living Area'. "
            "It serves as an estimate and should be used as a guide."
        )
