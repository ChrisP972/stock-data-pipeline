import pandas as pd
import streamlit as st
from db import engine

st.title("Stock Price History")

data = pd.read_sql("SELECT time, open FROM stock_price_history ORDER BY time ASC", engine)


st.line_chart(data)
