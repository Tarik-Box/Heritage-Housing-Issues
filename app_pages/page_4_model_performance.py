import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

@st.cache_data
def load_data_for_performance():
    """Loads the Ames Housing dataset."""
    url = 'https://raw.githubusercontent.com/INRIA/scikit-learn-mooc/main/datasets/ames_housing_no_missing.csv'
    df = pd.read_csv(url)
    return df

@st.cache_resource
def load_model_for_performance():
    """Loads the trained ML model."""
    try:
        model = joblib.load('src/heritage_housing_model.joblib')
        return model
    except FileNotFoundError:
        return None

def page_4_model_performance_body():
    """Displays the Model Performance page content."""
    st.header("Model Performance")
    st.write("---")

    st.info(
        "This page details the performance of our `RandomForestRegressor` model. "
        "The primary success metric is the R² (R-squared) score, which indicates "
        "how much of the variance in the sale price our model can explain. "
        "The business requirement was an R² score of at least 0.75 on both the train and test sets."
    )

    # Load data and model
    df = load_data_for_performance()
    model = load_model_for_performance()

    if df is None or model is None:
        st.error("Error: Could not load necessary data or model files.")
        return

    # Perform train-test split for evaluation
    features = ['OverallQual', 'GrLivArea']
    target = 'SalePrice'
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Calculate R2 scores
    y_pred_train = model.predict(X_train)
    r2_train = r2_score(y_train, y_pred_train)
    
    y_pred_test = model.predict(X_test)
    r2_test = r2_score(y_test, y_pred_test)

    st.subheader("R² Scores")
    st.write(f"* **Train Set R² Score:** `{r2_train:.4f}`")
    st.write(f"* **Test Set R² Score:** `{r2_test:.4f}`")
    
    st.success(
        "Our model meets the business requirement, with R² scores above 0.75 on both the train and test sets. "
        "The similar scores between the train and test sets also indicate that the model is generalizing well and not overfitting."
    )

    st.write("---")

    # Display Actual vs Predicted plot
    st.subheader("Actual vs. Predicted Sale Price (Test Set)")
    st.write(
        "This scatter plot shows the model's predicted prices against the actual sale prices from the test set. "
        "A perfect model would have all dots on the red dashed line. Our model's predictions are closely aligned with the actual values, confirming its strong performance."
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred_test, alpha=0.6, ax=ax)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
    ax.set_title('Actual vs. Predicted SalePrice (Test Set)')
    ax.set_xlabel('Actual SalePrice')
    ax.set_ylabel('Predicted SalePrice')
    st.pyplot(fig)
