from tkinter import *

from numpy import pad


window = Tk()
window.title("BookStore")
window.config(padx=5, pady=10)

def view_all():
    print("view all")

def search_entry():
    print("search entry")

def add_entry():
    print("add entry")

def update_selected():
    print("update selected")

def delete_selected():
    print("delete selected")

def close_window():
    print("close window")



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

text_title = Text(window, height=1, width=20)
text_year = Text(window, height=1, width=20)
text_author = Text(window, height=1, width=20)
text_isbn = Text(window, height=1, width=20)

listbox_records = Listbox(window)
scrollbar_records = Scrollbar(window)
listbox_records.configure(pyscrollcommand=scrollbar_records.set)
scrollbar_records.configure(command=listbox_records.yview)


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