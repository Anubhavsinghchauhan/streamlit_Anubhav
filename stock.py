import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Prediction")
title = st.text_input("enter the stock name ",'AAPL')
st.write("stock name", title)

start_date_a = st.date_input("enter start date of stock", datetime.date(2019, 7, 6))
end_datee= st.date_input("enter end date of stock", datetime.date(2019, 7, 6))

dat = yf.Ticker(title)
df=dat.history(period="1d",start=start_date_a, end=end_datee)

st.dataframe(df)
st.line_chart(df['Close'])