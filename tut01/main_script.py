from db.db_utils import db_connect

con = db_connect()
cur = con.cursor()

customers_sql = """
CREATE TABLE customers (
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL
)"""
cur.execute(customers_sql)

products_sql = """
CREATE TABLE products (
    id integer PRIMARY KEY,
    name text NOT NULL,
    price real NOT NULL
)"""
cur.execute(products_sql)

orders_sql = """
CREATE TABLE orders (
    id integer PRIMARY KEY,
    date text NOT NULL,
    customer_id integer,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
)"""
cur.execute(orders_sql)

lineitems_sql = """
CREATE TABLE lineitems (
    id integer PRIMARY KEY,
    quantity integer NOT NULL,
    total real NOT NULL,
    product_id integer,
    order_id integer,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (order_id) REFERENCES orders (id)
)"""
cur.execute(lineitems_sql)
