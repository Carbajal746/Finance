import streamlit as st
import yfinance as yf
import pandas as pd

# ================================
# Dashboard Title and Introduction
# ================================
st.title("Mexican Stock Market & Interest Rate Dashboard")
st.write("Welcome to the Mexican Stock Market Dashboard. This dashboard provides insights and analysis of major Mexican stocks and interest rate trends.")

# ================================
# Sidebar Navigation
# ================================
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Stock Statistics", "Interest Rate Analysis", "Market Insights", "Settings"])

# ================================
# Fetch Stock Data
# ================================
def fetch_stock_data(tickers):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")
        data[ticker] = hist['Close']
    return pd.DataFrame(data)

# Fetch Interest Rate Data (e.g., US Treasury Rates)
def fetch_interest_rate():
    # Replace with actual source or method to get interest rates if necessary
    return pd.Series([4.25, 4.35, 4.30, 4.40, 4.20, 4.15, 4.05, 4.10, 4.25, 4.20],
                     index=pd.date_range(start="2023-01-01", periods=10, freq='M'))

# ================================
# Dashboard Summary Metrics
# ================================
st.header("Dashboard Summary")
col1, col2, col3 = st.columns(3)

# Summary metrics with colors
col1.metric("Total Stocks Analyzed", "5", "+1", delta_color="normal")
col2.metric("Average Interest Rate (%)", "4.20%", "-0.05%", delta_color="normal")
col3.metric("Top Stock Performer", "AMXL", "+10%", delta_color="normal")  # AMXL as an example

# ================================
# Page Content Based on Selection
# ================================
if page == "Overview":
    st.subheader("Overview")
    st.write("""
    This section provides a high-level overview of the project's objectives and recent findings.

    **Project Goals:**
    - Analyze major Mexican stocks to identify trends and performance metrics.
    - Evaluate the impact of interest rate changes on the stock market.
    - Provide actionable insights for investors.
    """)

elif page == "Stock Statistics":
    st.subheader("Stock Statistics")

    # Define tickers for major Mexican stocks
    tickers = ["AMXL.MX", "GFNORTEO.MX", "CEMEXCPO.MX", "WALMEX.MX", "BIMBOA.MX"]

    # Fetch stock data
    stock_data = fetch_stock_data(tickers)

    # Display stock prices
    st.line_chart(stock_data)

elif page == "Interest Rate Analysis":
    st.subheader("Interest Rate Analysis")

    # Fetch interest rate data
    interest_rate_data = fetch_interest_rate()

    # Display interest rate trends
    st.line_chart(interest_rate_data)

elif page == "Market Insights":
    st.subheader("Market Insights")
    st.write("Analysis and insights on how the stock market is performing against interest rate trends.")

    # Example of insights based on data
    st.write("The trends suggest a correlation between rising interest rates and stock market fluctuations.")

elif page == "Settings":
    st.subheader("Settings")
    st.write("Adjust settings and preferences for the dashboard here.")
    st.selectbox("Select Theme", ["Light", "Dark"])

# ================================
# Footer Information
# ================================
st.write("For more detailed information, please refer to the documentation or contact the project team.")


