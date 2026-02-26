import pandas as pd
import streamlit as st
from sqlalchemy import text
from db import engine

st.title("Stock Price History")

# Ticker select
tickers = pd.read_sql("SELECT DISTINCT ticker FROM stock_price_history ORDER BY ticker", engine)["ticker"].tolist()
ticker = st.selectbox("Ticker", tickers)

# Parameter select
data_point = st.selectbox("Data Point", ["open", "high", "low", "close", "volume"])

data = pd.read_sql(text("""SELECT * 
                   FROM stock_price_history 
                   WHERE ticker = :ticker
                   ORDER BY time ASC
                   """),
                    engine, params={"ticker": ticker})

data["time"] = pd.to_datetime(data["time"])

data = data.set_index("time")
st.line_chart(data[data_point])
