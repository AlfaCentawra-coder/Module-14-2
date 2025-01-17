import sqlite3

def initiate_db(db_name="initiate.db"):
    """Creates the Products table if it doesn't exist."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def get_all_products(db_name="initiate.db"):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products
