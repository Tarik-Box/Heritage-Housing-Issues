import streamlit as st

def page_1_summary_body():
    """Displays the Project Summary content."""
    st.header("Project Summary")
    st.write("---")

    st.info(
        "**General Information**\n\n"
        "This project is a data-driven web application designed to predict housing prices in Ames, Iowa. "
        "It uses a machine learning model trained on a well-known dataset of house sales in the area. "
        "The primary goal is to provide users with a tool to understand property values and get instant price estimates based on key house features."
    )

    st.write("---")
    
    st.warning(
        "**Project Business Requirements**\n\n"
        "The project aims to solve two business needs for the 'Heritage Housing' real estate agency:\n\n"
        "1. To identify key features that influence house sale prices.\n\n"
        "2. To provide a tool that reliably predicts sale prices based on these features.\n\n"
        "The predictive model is required to achieve an R-squared (R²) score of at least **0.75** to be considered effective for business use."
    )

    st.write("---")

    st.success(
        "**The Dataset: Ames, Iowa Housing Data**\n\n"
        "We used a dataset of 2,930 house sales in Ames, Iowa, with 81 attributes per sale. "
        "This includes features like `GrLivArea` (living area), `OverallQual` (quality), and `YearBuilt`. "
        "Our model predicts the final `SalePrice`."
    )

