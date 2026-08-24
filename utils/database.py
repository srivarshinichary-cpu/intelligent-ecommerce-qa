import sqlite3


DATABASE_NAME = "data/ecommerce.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


def insert_order(
    order_id,
    product_name,
    quantity,
    price,
    status
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO orders
        (order_id, product_name, quantity, price, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        order_id,
        product_name,
        quantity,
        price,
        status
    ))

    connection.commit()

    connection.close()


def get_order(order_id):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT order_id, product_name, quantity, price, status
        FROM orders
        WHERE order_id = ?
    """, (order_id,))

    order = cursor.fetchone()

    connection.close()

    return order