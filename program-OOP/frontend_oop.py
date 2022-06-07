from tkinter import *
from backend_oop import Database

file_path = "program-OOP/books.db"

database = Database(path=file_path)


class Window(object):

    def __init__(self, window) -> None:
        self.window = window
        self.window.title("BookStore")
        self.window.config(padx=5, pady=10)
        label_title = Label(window, text="Title")
        label_year = Label(window, text="Year")
        label_author = Label(window, text="Author")
        label_isbn = Label(window, text="ISBN")

        button_view_all = Button(window, text="View All", command=self.view_all)
        button_search = Button(window, text="Search Entry", command=self.search_entry)
        button_add = Button(window, text="Add Entry", command=self.add_entry)
        button_update = Button(window, text="Update Selected", command=self.update_selected)
        button_delete = Button(window, text="Delete Selected", command=self.delete_selected)
        button_close = Button(window, text="Close", command=self.close_window)


        self.text_title = Entry(window)
        self.text_year = Entry(window)
        self.text_author = Entry(window)
        self.text_isbn = Entry(window)

        self.listbox_records = Listbox(window, width=50)
        scrollbar_records = Scrollbar(window)
        self.listbox_records.configure(yscrollcommand=scrollbar_records.set)
        scrollbar_records.configure(command=self.listbox_records.yview)
        self.listbox_records.bind("<<ListboxSelect>>", self.get_selected_row)


        label_title.grid(row=0, column=0)
        self.text_title.grid(row=0, column=1)
        label_author.grid(row=0, column=2)
        self.text_author.grid(row=0, column=3)

        label_year.grid(row=1, column=0)
        self.text_year.grid(row=1, column=1)
        label_isbn.grid(row=1, column=2)
        self.text_isbn.grid(row=1, column=3)

        button_view_all.grid(row=2, column=3, sticky="ew")
        button_search.grid(row=3, column=3, sticky="ew")
        button_add.grid(row=4, column=3, sticky="ew")
        button_update.grid(row=5, column=3, sticky="ew")
        button_delete.grid(row=6, column=3, sticky="ew")
        button_close.grid(row=7, column=3, sticky="ew")

        self.listbox_records.grid(row=2, column=0, rowspan=6, columnspan=2, sticky="ew")
        scrollbar_records.grid(row=2, column=2, rowspan=6, sticky="ns")


    def get_selected_row(self, event):
        try:
            global selected_tuple
            index=self.listbox_records.curselection()[0]
            selected_tuple = self.listbox_records.get(index)
            self.clear_all_entries()
            self.text_title.insert(END, selected_tuple[1])
            self.text_author.insert(END, selected_tuple[2])
            self.text_year.insert(END, selected_tuple[3])
            self.text_isbn.insert(END, selected_tuple[4])
            return selected_tuple
        except IndexError:
            print("Listbox currently empty")

    def get_all_entries(self):
        title = self.text_title.get()
        author = self.text_author.get()
        year = self.text_year.get()
        isbn = self.text_isbn.get()
        return title, author, year, isbn

    def clear_all_entries(self):
        self.text_title.delete(0, END)
        self.text_year.delete(0, END)
        self.text_author.delete(0, END)
        self.text_isbn.delete(0, END)

    def view_all(self):
        print("view all")
        self.listbox_records.delete(0, END)
        for row in database.view_db():
            self.listbox_records.insert(row[0]-1, row)

    def search_entry(self):
        print("search entry")
        self.listbox_records.delete(0, END)
        title, author, year, isbn = self.get_all_entries()
        for row in database.search_db(title=title, author=author, year=year, isbn=isbn):
            self.listbox_records.insert(row[0]-1, row)

    def add_entry(self):
        print("add entry")
        title, author, year, isbn = self.get_all_entries()
        database.insert_to_db(title=title, author=author, year=year, isbn=isbn)
        self.view_all()

    def update_selected(self):
        selected_id = selected_tuple[0]
        print(f"update selected: {selected_tuple}")
        title, author, year, isbn = self.get_all_entries()
        database.update_db(id=selected_id, title=title, author=author, year=year, isbn=isbn)
        self.view_all()

    def delete_selected(self):
        selected_id = selected_tuple[0]
        print(f"delete selected {self.listbox_records.get(ACTIVE)}")
        database.delete_db(selected_id)
        self.view_all()

    def close_window(self):
        print("close window")
        window.destroy()



window = Tk()
Window(window)
window.mainloop()