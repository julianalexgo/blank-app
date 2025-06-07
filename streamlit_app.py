#Import Libraries 
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import datetime as dt
import mplfinance as mpf
import plotly.express as px

#Streamlit for web app
import streamlit as st

#Streamlit configuration
st.set_page_config(page_title = "FetchStocks")

#Function to Save to CSV
def fetch_stocks(ticker, syear, smonth, sday, eyear, emonth, eday):
    start = dt.datetime(syear, smonth, sday)
    end = dt.datetime(eyear, emonth, eday)
    df = web.DataReader(ticker, 'stooq', start, end)
    return df

with st.form('ticker_form'):
    st.write("Enter the ticker symbol and date range to fetch stock data.")
    ticker = st.text_input("Enter the ticker symbol:", key = 'ticker_name').upper()
    sdate = st.date_input("Select start date:", key = 'sdate', value = None, format = "MM/DD/YYYY", min_value = dt.date(1900, 1, 1), max_value = 'today')
    edate = st.date_input("Select end date:", key = 'edate', value = 'today', format = "MM/DD/YYYY", min_value = sdate, max_value = 'today')
    submitted = st.form_submit_button("Fetch Data")

#Get inputs before splitting the code
#st.title("Stock Data Fetcher")
#ticker = st.text_input("Enter the ticker symbol (or 'exit' to quit):", key = 'ticker_name').upper()
#sdate = st.text_input("Enter start date (MM/DD/YYYY): ", key = 'start_date')
#edate = st.text_input("Enter end date (MM/DD/YYYY): ", key = 'end_date')

if submitted:
    st.success(f"Fetching data for {ticker} from {sdate} to {edate}...")
    if (ticker or sdate or edate) != None:
        try:
            df = fetch_stocks(ticker, sdate.year, sdate.month, sdate.day, edate.year, edate.month, edate.day)
            st.dataframe(df)
            fig = px.line(df, x = df.index, y = df.High) #Reference them like this or like df['Close'] but refer to index this way
            st.plotly_chart(fig)
        except Exception as e:
            print(f"An error occurred: {e}")
    elif (ticker or sdate or edate) is None:
        st.warning("Please enter a ticker symbol and dates to fetch data.")


