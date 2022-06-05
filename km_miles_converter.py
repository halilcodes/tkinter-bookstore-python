from tkinter import *

window = Tk()

def km_to_miles():
    print("Success!")
    try:
        km_entry = float(entry_1.get())
        entry_in_miles = round(km_entry * 0.621371, 2)
        text_1.insert(END, entry_in_miles)
    except ValueError:
        text_1.insert(END, "enter a valid number!")
        print("enter a valid number!")



button_1 = Button(window, text="Execute", command=km_to_miles)
#button_1.pack() add button to window randomly
button_1.grid(row=0, column=0)


entry_1 = Entry(window)
entry_1.grid(row=0, column=1)

text_1 = Text(window, height=1, width=20)
text_1.grid(row=0, column=2)



# make sure window does not close until we choose it to
window.mainloop()