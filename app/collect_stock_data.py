import yfinance as yf
import click
import pandas as pd
from sqlalchemy import insert
from sqlalchemy.dialects.postgresql import insert as pg_insert
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
@click.option("--ticker", default="AAPL", help="Stock ticker")
@click.option("--period", default="2y", help="Time period")
@click.option("--interval", default="1d", help="Time interval")
def collect_stock_data(ticker, period, interval):

    init_db()

    # Retrieve stock data
    data = yf.Ticker(ticker).history(period=period, interval=interval)

    # Add ticker column
    data.insert(0, "Ticker", ticker)

    # Convert date/datetime index to real column
    data = data.reset_index()

    # Match column naming for db schema
    data = data.rename(columns=YF_TO_DB)

    # Keep columns from db schema
    rows = data[list(stock_table.c.keys())].to_dict(orient="records")

    # Insert rows into stock table
    with engine.begin() as conn:
        insert_stmt = pg_insert(stock_table).values(rows)
        insert_stmt = insert_stmt.on_conflict_do_nothing(index_elements=["ticker", "time"])
        conn.execute(insert_stmt)   

if __name__ == "__main__":
    collect_stock_data()
