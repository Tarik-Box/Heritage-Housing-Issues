import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_2_data_analysis_body():
    """Displays the Data Analysis page content."""
    st.header("Data Analysis")
    st.write("---")

    st.info(
        "This section explores key relationships within the Ames Housing dataset. "
        "We'll visualize the factors that have the strongest impact on `SalePrice`, "
        "helping us understand the market dynamics in Ames, Iowa."
    )

    # Load the dataset (re-loading for independent page execution)
    url = 'https://raw.githubusercontent.com/INRIA/scikit-learn-mooc/main/datasets/ames_housing_no_missing.csv'
    df = pd.read_csv(url)

    st.write("---")

    st.subheader("Correlation with SalePrice")
    st.write(
        "First, let's look at the top features that correlate most strongly with the `SalePrice`. "
        "A higher correlation coefficient (closer to 1 or -1) indicates a stronger linear relationship."
    )
    correlations = df.corr(numeric_only=True)['SalePrice'].sort_values(ascending=False)
    st.write(correlations.head(10))

    st.markdown(
        "As observed, `OverallQual` (Overall Material and Finish Quality) and "
        "`GrLivArea` (Above Grade (Ground) Living Area Square Feet) are among the most correlated features. "
        "These will be critical for our prediction model."
    )

    st.write("---")

    st.subheader("SalePrice vs. Overall Quality")
    st.write(
        "This box plot illustrates how the `SalePrice` varies with the `OverallQual` score. "
        "It clearly shows that houses with higher overall quality tend to have significantly higher sale prices."
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='OverallQual', y='SalePrice', data=df, ax=ax)
    ax.set_title('SalePrice vs. Overall Quality')
    ax.set_xlabel('Overall Quality (1-10)')
    ax.set_ylabel('Sale Price')
    st.pyplot(fig)

    st.write("---")

    st.subheader("SalePrice vs. Above Ground Living Area")
    st.write(
        "This scatter plot visualizes the relationship between the above-ground living area (`GrLivArea`) "
        "and the `SalePrice`. We can see a strong positive linear trend, indicating that larger houses "
        "generally command higher prices."
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='GrLivArea', y='SalePrice', data=df, alpha=0.6, ax=ax)
    ax.set_title('SalePrice vs. Above Grade Living Area (GrLivArea)')
    ax.set_xlabel('Above Grade Living Area (sq. ft.)')
    ax.set_ylabel('Sale Price')
    st.pyplot(fig)

    st.write("---")

    st.subheader("Distribution of Sale Price")
    st.write(
        "This histogram shows the distribution of `SalePrice` in the dataset. "
        "The distribution is right-skewed, which is typical for real estate prices. "
        "Understanding this distribution is important for model interpretation."
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['SalePrice'], kde=True, ax=ax)
    ax.set_title('Distribution of SalePrice')
    ax.set_xlabel('Sale Price')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
