<div align="center">

<!-- Placeholder for a project banner -->
![Project Banner](https://via.placeholder.com/1200x300.png?text=Heritage+Housing+Price+Predictor)

# **Heritage Housing Price Predictor**

*A Streamlit web application for predicting housing prices in Ames, Iowa, using machine learning.*

</div>

<div align="center">

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) <!-- Assuming MIT License -->

</div>

---

> **Note:** The live Heroku deployment is currently experiencing an application error. This is a known issue and is actively being debugged.

<div align="center">

**[View Live Demo on Heroku](https://ci-heritage-housing-predictor-7f5331ad4224.herokuapp.com/)**

</div>

---

## 📖 Project Overview

This project presents a predictive analytics tool designed to bring data-driven insights to the real estate market in Ames, Iowa. The application leverages a `RandomForestRegressor` model to predict house sale prices based on key property attributes. It serves as a practical demonstration of a full-stack data science workflow, from data analysis and model training to deployment as an interactive web application.

The project follows a simplified CRISP-DM methodology, prioritizing a functional and valuable end-product that addresses specific business needs.

## 🎯 Business Requirements

The project was conceptualized for a fictional real estate agency, 'Heritage Housing', with two primary objectives:

1.  **Identify Value Drivers:** To understand which property features most significantly influence the final sale price.
2.  **Predict Sale Prices:** To create a tool that provides reliable price estimates, assisting agents in pricing strategies and managing client expectations.

The key business success metric is for the predictive model to achieve an **R-squared (R²) score of 0.75 or higher**, ensuring its predictions are reliable enough for business use. Our model successfully surpassed this metric.

---

## ✨ Features & Application Preview

The application is designed for simplicity and ease of use, organized into three main sections:

### 1. Project Summary
A landing page that provides a comprehensive overview of the project, its objectives, and the business case it addresses.

<!-- Placeholder for Project Summary screenshot -->
![Project Summary Page](https://via.placeholder.com/800x450.png?text=Project+Summary+Page+Screenshot)

### 2. Data Analysis
This section showcases key insights from our exploratory data analysis, featuring interactive plots that visualize the relationships between property features and sale prices.

<!-- Placeholder for Data Analysis screenshot -->
![Data Analysis Page](https://via.placeholder.com/800x450.png?text=Data+Analysis+Page+Screenshot)

### 3. Price Prediction
The core feature of the application. Users can input values for key property attributes and receive an instant sale price prediction from our trained model.

<!-- Placeholder for Price Prediction screenshot -->
![Price Prediction Page](https://via.placeholder.com/800x450.png?text=Price+Prediction+Page+Screenshot)

---

## 🛠️ Technology Stack

*   **Backend & Modeling:** Python, Pandas, Scikit-learn, joblib
*   **Frontend & UI:** Streamlit
*   **Data Visualization:** Matplotlib, Seaborn
*   **Deployment:** Heroku, Git

---

## 🚀 Getting Started Locally

To run this application on your local machine, follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Tarik-Box/Heritage-Housing-Issues.git
    cd Heritage-Housing-Issues
    ```

2.  **Set Up a Virtual Environment**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    streamlit run app.py
    ```
    The application will open in your default web browser.

---

## 🔗 Deployment

The application is deployed on Heroku. The deployment process involves:
1.  Connecting the GitHub repository to a Heroku app.
2.  Ensuring `Procfile`, `.python-version`, and `setup.sh` are correctly configured.
3.  Pushing the `main` branch to the Heroku remote to trigger a build and deployment.

**Live URL:** [https://ci-heritage-housing-predictor-7f5331ad4224.herokuapp.com/](https://ci-heritage-housing-predictor-7f5331ad4224.herokuapp.com/)

---

## 🙏 Credits

*   **Dataset:** [Ames Housing Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
*   **Assistance:** Gemini-CLI for project guidance and code generation.
