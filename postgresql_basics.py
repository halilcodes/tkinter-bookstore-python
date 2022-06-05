from turtle import update
import psycopg2
import string
import database_credentials as db_cred

from colorama import Cursor
from numpy import insert

"""
1. Connect to a Database
2. Create a cursor object
3. Write SQL query
4. Commit changes
5. Close database connection
"""
db_name = f"dbname='database1' user={db_cred.postgreSQL_user} password={db_cred.postgreSQL_pass} host='localhost' port={db_cred.port}"

def create_table(db_name=db_name) -> None:
    conn = psycopg2.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    conn.commit()
    conn.close()


def insert_into_table(item:string, quantity:int, price:float, db_name=db_name) -> None:
    conn = psycopg2.connect(db_name)
    cursor = conn.cursor()
    #cursor.execute(f"INSERT INTO store VALUES ({item}, {quantity}, {price})")

    # below is open for SQL injection attacks
    #cursor.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))

    cursor.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))

    
    conn.commit()
    conn.close()


def view_db(db_name=db_name):
    conn = psycopg2.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    
    conn.close()

    return rows

def delete_from_db(item:str, db_name=db_name):
    conn = psycopg2.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    
    conn.commit()
    conn.close()

def update_db(item:string, quantity:int, price:float, db_name=db_name) -> None:
    conn = psycopg2.connect(db_name)
    cursor = conn.cursor()    

    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))

    conn.commit()
    conn.close()


update_db("Orange", 500, 80.08)
print(view_db())