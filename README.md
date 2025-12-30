# Heritage Housing Issues

## Project Overview

This project is a predictive analytics web application built using Python and Streamlit. Its main purpose is to help users understand which house attributes significantly influence sale prices in Ames, Iowa, and to provide a quick way to predict a house's sale price based on its features.

The application follows a simplified CRISP-DM (Cross-Industry Standard Process for Data Mining) approach, focusing on delivering practical business value rather than academic complexity. It's designed to be straightforward and functional, aiming for clarity and ease of use.

## Business Requirements

The primary driver for this project comes from a fictional local real estate agency, 'Heritage Housing'. They have identified two core needs to enhance their competitive edge and service quality:

1.  **Understand Property Value Drivers:** The agency needs to pinpoint the key characteristics of a house that have the most significant impact on its market value. This insight will empower their agents to provide more informed advice to clients regarding property valuations and strategic pricing.

2.  **Predict Sale Prices:** A robust tool is required to offer quick and reliable predictions of a house's sale price, given a set of its features. This tool would serve as a crucial aid for agents to validate initial asking prices and effectively manage client expectations by providing data-backed estimates.

    *   **Success Metric:** The predictive model developed for this purpose must achieve an **R-squared (R²)** score of at least **0.75** on the test set. This threshold ensures the model is sufficiently accurate and trustworthy for practical business applications.

## Dataset Description

The project utilizes the well-known **Ames Housing Dataset**, a comprehensive collection of house sales data from Ames, Iowa. This dataset includes 2,930 individual house sales records, each described by 81 different attributes.

Key types of attributes include:
*   **Physical Characteristics:** Such as `GrLivArea` (above-ground living area in square feet), `OverallQual` (a rating of overall material and finish quality from 1 to 10), and `YearBuilt` (the original construction date).
*   **Location & Neighborhood Factors:** Information detailing the physical location within Ames and specific neighborhood characteristics.
*   **Amenities:** Features like `GarageCars` (the size of the garage in car capacity) and `TotalBsmtSF` (total square feet of basement area).

The primary variable we are interested in predicting is `SalePrice`. The version of the dataset used for this project has been preprocessed to handle missing values, simplifying our initial data cleaning steps.

## Machine Learning Business Case

The central machine learning task in this project is **regression**, specifically predicting a continuous numerical value: the `SalePrice` of a house. A `RandomForestRegressor` model was chosen for its balance of interpretability, robustness, and good performance on tabular data.

The model's ability to achieve an R² score exceeding 0.75 directly addresses the agency's need for reliable price predictions. By automating this process, agents can spend less time on manual estimations and more time on client interactions, leveraging data-driven insights to close deals more effectively.

## Dashboard Design

The Streamlit web application is designed to be user-friendly and intuitive, structured into three distinct pages accessible via a sidebar navigation:

1.  **Project Summary:**
    *   **Purpose:** Provides a high-level overview of the project, explaining its background, the business problems it aims to solve, and a brief description of the dataset used.
    *   **Content:** General information about the app, the "Heritage Housing" business requirements, and details about the Ames Housing Dataset.

2.  **Data Analysis:**
    *   **Purpose:** Allows users to explore key insights derived from the dataset through visualizations. This page aims to illustrate the factors that significantly impact house prices, reinforcing the business's understanding of market drivers.
    *   **Content:** Displays top features correlated with `SalePrice` (e.g., `OverallQual`, `GrLivArea`), along with illustrative plots such as `SalePrice` vs. `OverallQual` (boxplot), `SalePrice` vs. `GrLivArea` (scatterplot), and the overall distribution of `SalePrice` (histogram).

3.  **Price Prediction:**
    *   **Purpose:** The core interactive feature, enabling users to input specific house characteristics and receive an instant sale price prediction.
    *   **Content:** Provides input widgets (sliders) for `OverallQual` and `GrLivArea`. Users can adjust these values, click a "Predict Sale Price" button, and see the estimated value based on the trained machine learning model. This directly fulfills the agency's need for a predictive tool.

## Deployment Information

The Streamlit application is designed for easy deployment and accessibility.

### Running Locally

To run this application on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Tarik-Box/Heritage-Housing-Issues.git
    cd Heritage-Housing-Issues
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    The application should open in your default web browser.

### Deployment on Heroku

The application is deployed on Heroku and can be accessed live at:
[https://ci-heritage-housing-predictor-7f5331ad4224.herokuapp.com/](https://ci-heritage-housing-predictor-7f5331ad4224.herokuapp.com/)

**Deployment Process:**

1.  **Heroku Account & CLI:** Ensure you have a Heroku account and the Heroku CLI installed and logged in.
2.  **Create Heroku App:** From your project directory, run `heroku create YOUR_APP_NAME` (replace `YOUR_APP_NAME` with a unique name, e.g., `ci-heritage-housing-predictor`).
3.  **Configure Buildpacks:** Heroku automatically detects the Python buildpack.
4.  **Push to Heroku:** Deploy the application by pushing your Git repository to Heroku: `git push heroku main`.
5.  **Access Application:** Once deployed, open the app in your browser: `heroku open`.
6.  **Troubleshooting:** Check Heroku logs (`heroku logs --tail`) for any deployment issues.


## Credits

*   **Dataset:** Ames Housing Dataset
*   **Tools:** Python, Streamlit, Pandas, Scikit-learn, Matplotlib, Seaborn, joblib
*   **Assistance:** Gemini-CLI (for project guidance and code generation)