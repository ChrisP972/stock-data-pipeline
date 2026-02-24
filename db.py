from sqlalchemy import (
    create_engine, MetaData, Table, Column, Double,
    Integer, String, DateTime)

# Create database connection
engine = create_engine(f'postgresql+psycopg://root:root@localhost:5432/stocks')

# Create schema of the stock data table
metadata_obj = MetaData()

stock_table = Table(
    "stock_price_history",
    metadata_obj,
    Column('ticker', String, primary_key=True),
    Column('time', DateTime, primary_key=True),
    Column('open', Double),
    Column('high', Double),
    Column('low', Double),
    Column('close', Double),
    Column('volume', Integer),
)


def init_db() -> None:
    metadata_obj.create_all(engine)
