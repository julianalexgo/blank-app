#Import Libraries 
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import mplfinance as mpf
import plotly.express as px

# Streamlit for web app
import streamlit as st

#Function to Save to CSV
def save_to_csv_from_google(ticker, syear, smonth, sday, eyear, emonth, eday):
    start = dt.datetime(syear, smonth, sday)
    end = dt.datetime(eyear, emonth, eday)
    df = web.DataReader(ticker, 'stooq', start, end)
    return df

with st.form('ticker_form'):
    st.write("Enter the ticker symbol and date range to fetch stock data.")
    ticker = st.text_input("Enter the ticker symbol:", key = 'ticker_name').upper()
    sdate = st.text_input("Enter start date (MM/DD/YYYY): ", key = 'start_date')
    edate = st.text_input("Enter end date (MM/DD/YYYY): ", key = 'end_date')
    submitted = st.form_submit_button("Fetch Data")

#Get inputs before splitting the code
#st.title("Stock Data Fetcher")
#ticker = st.text_input("Enter the ticker symbol (or 'exit' to quit):", key = 'ticker_name').upper()
#sdate = st.text_input("Enter start date (MM/DD/YYYY): ", key = 'start_date')
#edate = st.text_input("Enter end date (MM/DD/YYYY): ", key = 'end_date')


if submitted:
    if ticker and sdate and edate:
        try:
            smonth, sday, syear = map(int, sdate.split('/'))
            emonth, eday, eyear = map(int, edate.split('/'))
            df = save_to_csv_from_google(ticker, syear, smonth, sday, eyear, emonth, eday)
            st.dataframe(df)
            fig = px.line(df, x = df.index, y = df.High) #Reference them like this or like df['Close'] but refer to index this way
            st.plotly_chart(fig)
        except Exception as e:
            print(f"An error occurred: {e}")
    elif not ticker or not sdate or not edate:
        st.warning("Please complete all fields to fetch data.")


