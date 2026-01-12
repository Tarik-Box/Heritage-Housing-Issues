import streamlit as st
from app_pages.page_1_summary import page_1_summary_body
from app_pages.page_2_data_analysis import page_2_data_analysis_body
from app_pages.page_3_price_prediction import page_3_price_prediction_body
from app_pages.page_4_model_performance import page_4_model_performance_body

def main():
    """Main function to set up and run the Streamlit app."""
    st.set_page_config(page_title="Heritage Housing Issues", page_icon="🏘️", layout="wide")
    
    st.title("🏘️ Heritage Housing Issues")
    st.caption("A Predictive Analytics Web Application for Ames, Iowa Housing Prices.")

    st.sidebar.title("Navigation")
    
    # Define available pages
    PAGES = {
        "Project Summary": page_1_summary_body,
        "Data Analysis": page_2_data_analysis_body,
        "Price Prediction": page_3_price_prediction_body,
        "Model Performance": page_4_model_performance_body # New page
    }
    
    selected_page = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Run the function corresponding to the selected page
    page_function = PAGES[selected_page]
    page_function()

if __name__ == "__main__":
    main()
