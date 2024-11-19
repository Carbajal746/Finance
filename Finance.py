import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "EDA", "Insights", "Prediction"])

# Home Page
if page == "Home":
    st.title("Mexican Stock Market & Interest Rate Analysis")
    st.write("This dashboard provides insights and analysis of major Mexican stocks and interest rate trends.")
    st.write("Select a section from the sidebar to start exploring the data.")

# EDA Page
elif page == "EDA":
    st.title("Exploratory Data Analysis (EDA)")
    st.write("### Simulated Logarithmic Returns Dataframe for AMXL.MX")

    # Generate simulated log returns data
    np.random.seed(42)
    simulated_log_returns = np.random.normal(0, 0.02, 252)
    log_returns_df = pd.DataFrame(simulated_log_returns, columns=["Simulated_AMXL_Log_Returns"])

    # Display data
    st.write(log_returns_df)

    # Summary statistics
    st.write("### Summary Statistics for Simulated Logarithmic Returns")
    st.write(log_returns_df.describe())

    # Distribution plot
    st.write("### Distribution of Simulated AMXL.MX Logarithmic Returns")
    fig = px.histogram(log_returns_df, x="Simulated_AMXL_Log_Returns",
                       title="Distribution of Simulated AMXL.MX Logarithmic Returns", nbins=30)
    st.plotly_chart(fig)

# Insights Page
elif page == "Insights":
    st.title("Insights")
    st.write("### Scatter Plot: Simulated Logarithmic Returns vs Shifted Series")

    # Scatter plot for shifted series
    shifted_log_returns = log_returns_df.shift(-1)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=log_returns_df["Simulated_AMXL_Log_Returns"], y=shifted_log_returns["Simulated_AMXL_Log_Returns"])
    plt.title("Scatter Plot of Simulated Logarithmic Returns vs Shifted Series")
    plt.xlabel("Simulated AMXL Log Returns")
    plt.ylabel("Shifted Log Returns")
    st.pyplot(plt)

# Prediction Page
elif page == "Prediction":
    st.title("Prediction")
    st.write("This section could include predictive models or forecasts for the selected stocks or interest rates.")
    st.write("Currently under construction...")
