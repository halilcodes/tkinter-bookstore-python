import sqlite3
import string

from colorama import Cursor
from numpy import insert

"""
1. Connect to a Database
2. Create a cursor object
3. Write SQL query
4. Commit changes
5. Close database connection
"""
db_name = "lite.db"

def create_table(db_name="lite.db") -> None:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    conn.commit()
    conn.close()


def insert_into_table(item:string, quantity:int, price:float, db_name="lite.db") -> None:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    #cursor.execute(f"INSERT INTO store VALUES ({item}, {quantity}, {price})")
    cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    
    conn.commit()
    conn.close()

def view_db(db_name="lite.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    
    conn.close()

    return rows

def delete_from_db(item:str, db_name="lite.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    
    conn.commit()
    conn.close()

def update_db(item:string, quantity:int, price:float, db_name="lite.db") -> None:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()    

    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))

    conn.commit()
    conn.close()


update_db("Water Glass", 11, 6)
#delete_from_db(item="Wine Glass")
print(view_db())