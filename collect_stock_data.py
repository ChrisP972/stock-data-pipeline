import click
import pandas as pd
from sqlalchemy import create_engine, text


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='stocks', help='PostgreSQL database name')
def collect_stock_data(pg_user, pg_pass, pg_host, pg_port,
                       pg_db):

    # Create database connection
    engine = create_engine(
        f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
    )

    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print(
            f"Connected to Postgres OK: db={pg_db} host={pg_host}:{pg_port}")


if __name__ == '__main__':
    collect_stock_data()
