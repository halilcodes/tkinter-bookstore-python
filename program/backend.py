import sqlite3

def connect_to_db():
    conn = sqlite3.connect("program/books.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, \
                                                    title TEXT, author TEXT, \
                                                    year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert_to_db(title, author, year, isbn):
    conn = sqlite3.connect("program/books.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view_db():
    conn = sqlite3.connect("program/books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_db(title="", author="", year=1, isbn=1):
    conn = sqlite3.connect("program/books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()    
    return rows

def delete_db(id):
    conn = sqlite3.connect("program/books.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()      

def update_db(id, title, author, year, isbn):
    conn = sqlite3.connect("program/books.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()   

connect_to_db()