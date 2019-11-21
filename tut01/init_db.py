import os
import sqlite3
from sqlite3 import Error


def db_connect(db_path):
    con = None
    try:
        con = sqlite3.connect(db_path)
        print(f"New connection created successfully, sqlite3 version: {sqlite3.version}")
        return con
    except Error as e:
        print(e)
    return con


def create_table(con, create_table_sql):
    try:
        c = con.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

    customers_sql = """
    CREATE TABLE IF NOT EXISTS customers (
        id integer PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL
    );"""

    products_sql = """
    CREATE TABLE IF NOT EXISTS products (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price real NOT NULL
    );"""

    orders_sql = """
    CREATE TABLE IF NOT EXISTS orders (
        id integer PRIMARY KEY,
        date text NOT NULL,
        customer_id integer,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    );"""

    lineitems_sql = """
    CREATE TABLE IF NOT EXISTS lineitems (
        id integer PRIMARY KEY,
        quantity integer NOT NULL,
        total real NOT NULL,
        product_id integer,
        order_id integer,
        FOREIGN KEY (product_id) REFERENCES products (id),
        FOREIGN KEY (order_id) REFERENCES orders (id)
    );"""

    con = db_connect(DEFAULT_PATH)

    if con is not None:
        create_table(con, customers_sql)
        create_table(con, products_sql)
        create_table(con, orders_sql)
        create_table(con, lineitems_sql)
    else:
        print("Error! cannot create db connection.")


if __name__ == '__main__':
    main()
