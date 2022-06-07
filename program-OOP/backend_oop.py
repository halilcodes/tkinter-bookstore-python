import sqlite3

class Database:


    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, \
                                                        title TEXT, author TEXT, \
                                                        year INTEGER, isbn INTEGER)")
        self.conn.commit()


    def insert_to_db(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view_db(self):
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()
        return rows

    def search_db(self, title="", author="", year=1, isbn=1):
        self.cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",\
                             (title, author, year, isbn))
        rows = self.cursor.fetchall()    
        return rows

    def delete_db(self, id):
        self.cursor.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
              

    def update_db(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",\
                             (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
           


if __name__ == "__main__":
    file_path = "program-OOP/books.db"
    database = Database(path=file_path)
