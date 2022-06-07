from tkinter import *
from backend_oop import Database


window = Tk()
window.title("BookStore")
window.config(padx=5, pady=10)

file_path = "program-OOP/books.db"
database = Database(path=file_path)

def get_selected_row(event):
    try:
        global selected_tuple
        index=listbox_records.curselection()[0]
        selected_tuple = listbox_records.get(index)
        clear_all_entries()
        text_title.insert(END, selected_tuple[1])
        text_author.insert(END, selected_tuple[2])
        text_year.insert(END, selected_tuple[3])
        text_isbn.insert(END, selected_tuple[4])
        return selected_tuple
    except IndexError:
        print("Listbox currently empty")

def get_all_entries():
    title = text_title.get()
    author = text_author.get()
    year = text_year.get()
    isbn = text_isbn.get()
    return title, author, year, isbn

def clear_all_entries():
    text_title.delete(0, END)
    text_year.delete(0, END)
    text_author.delete(0, END)
    text_isbn.delete(0, END)

def view_all():
    print("view all")
    listbox_records.delete(0, END)
    for row in database.view_db():
        listbox_records.insert(row[0]-1, row)

def search_entry():
    print("search entry")
    listbox_records.delete(0, END)
    title, author, year, isbn = get_all_entries()
    for row in database.search_db(title=title, author=author, year=year, isbn=isbn):
        listbox_records.insert(row[0]-1, row)

def add_entry():
    print("add entry")
    title, author, year, isbn = get_all_entries()
    database.insert_to_db(title=title, author=author, year=year, isbn=isbn)
    view_all()

def update_selected():
    selected_id = selected_tuple[0]
    print(f"update selected: {selected_tuple}")
    title, author, year, isbn = get_all_entries()
    database.update_db(id=selected_id, title=title, author=author, year=year, isbn=isbn)
    view_all()

def delete_selected():
    selected_id = selected_tuple[0]
    print(f"delete selected {listbox_records.get(ACTIVE)}")
    database.delete_db(selected_id)
    view_all()

def close_window():
    print("close window")
    window.destroy()


label_title = Label(window, text="Title")
label_year = Label(window, text="Year")
label_author = Label(window, text="Author")
label_isbn = Label(window, text="ISBN")

button_view_all = Button(window, text="View All", command=view_all)
button_search = Button(window, text="Search Entry", command=search_entry)
button_add = Button(window, text="Add Entry", command=add_entry)
button_update = Button(window, text="Update Selected", command=update_selected)
button_delete = Button(window, text="Delete Selected", command=delete_selected)
button_close = Button(window, text="Close", command=close_window)


text_title = Entry(window)
text_year = Entry(window)
text_author = Entry(window)
text_isbn = Entry(window)

listbox_records = Listbox(window, width=50)
scrollbar_records = Scrollbar(window)
listbox_records.configure(yscrollcommand=scrollbar_records.set)
scrollbar_records.configure(command=listbox_records.yview)
listbox_records.bind("<<ListboxSelect>>", get_selected_row)


label_title.grid(row=0, column=0)
text_title.grid(row=0, column=1)
label_author.grid(row=0, column=2)
text_author.grid(row=0, column=3)

label_year.grid(row=1, column=0)
text_year.grid(row=1, column=1)
label_isbn.grid(row=1, column=2)
text_isbn.grid(row=1, column=3)

button_view_all.grid(row=2, column=3, sticky="ew")
button_search.grid(row=3, column=3, sticky="ew")
button_add.grid(row=4, column=3, sticky="ew")
button_update.grid(row=5, column=3, sticky="ew")
button_delete.grid(row=6, column=3, sticky="ew")
button_close.grid(row=7, column=3, sticky="ew")

listbox_records.grid(row=2, column=0, rowspan=6, columnspan=2, sticky="ew")
scrollbar_records.grid(row=2, column=2, rowspan=6, sticky="ns")



window.mainloop()