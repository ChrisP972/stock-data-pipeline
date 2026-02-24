import yfinance as yf
import click
import pandas as pd
from sqlalchemy import insert
from db import engine, init_db, stock_table

YF_TO_DB = {
    "Ticker": "ticker",
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close",
    "Volume": "volume",
    # yfinance may call it Date or Datetime depending on time interval selected
    "Date": "time",
    "Datetime": "time",
}


@click.command()
@click.option('--target-table', default='stock_price_history', help='Target table name')
@click.option('--ticker', default='AAPL', help='Stock ticker')
@click.option('--period', default='1y', help='Time period')
@click.option('--interval', default='1d', help='Time interval')
def collect_stock_data(target_table, ticker, period, interval):

    init_db()

    # Retrieve stock data
    data = yf.Ticker(ticker).history(period=period, interval=interval)

    # Add ticker column
    data.insert(0, 'Ticker', ticker)

    # Convert date/datetime index to real column
    data = data.reset_index()

    # Match column naming for db schema
    data = data.rename(columns=YF_TO_DB)

    # Keep columns from db schema
    rows = data[list(stock_table.c.keys())].to_dict(orient="records")

    with engine.begin() as conn:
        conn.execute(insert(stock_table), rows)


if __name__ == '__main__':
    collect_stock_data()
