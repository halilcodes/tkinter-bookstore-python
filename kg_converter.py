from tkinter import *

window = Tk()
window.title("KG Converter")

def kg_converter():
    print("converted!")
    text_grams.delete('1.0', END)
    text_pounds.delete('1.0', END)
    text_ounces.delete('1.0', END)
    try:
        entry_float = float(entry_kg.get())
        entry_grams = entry_float * 1000
        entry_pounds = entry_float * 2.20462
        entry_ounces = entry_float * 35.274
        text_grams.insert(END, entry_grams)
        text_pounds.insert(END, entry_pounds)
        text_ounces.insert(END, entry_ounces)
    except ValueError:
        print("Enter Valid Input!")
        text_grams.insert(END, "enter a valid number!")
        text_pounds.insert(END, "enter a valid number!")
        text_ounces.insert(END, "enter a valid number!")


title_kg = Label(window, text="Kg")
title_kg.grid(row=0, column=0)

entry_kg = Entry(window)
entry_kg.grid(row=0, column=1)
convert_button = Button(text="Convert", command=kg_converter)
convert_button.grid(row=0, column=2)

title_grams = Label(window, text="Grams")
title_grams.grid(row=1, column=0)
title_pounds = Label(window, text="Pounds")
title_pounds.grid(row=1, column=1)
title_ounces = Label(window, text="Ounces")
title_ounces.grid(row=1, column=2)

text_grams = Text(window, height=1, width=20)
text_grams.grid(row=2, column=0)
text_pounds = Text(window, height=1, width=20)
text_pounds.grid(row=2, column=1)
text_ounces = Text(window, height=1, width=20)
text_ounces.grid(row=2, column=2)

window.mainloop()