from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize(width=200, height=150)
window.config(padx=30, pady=30)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result.config(text=f"{km}")


miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

km_result = Label(text="0")
km_result.grid(row=1, column=1)
label1 = Label(text="Miles")
label1.grid(row=0, column=2)
label2 = Label(text="is equal to")
label2.grid(row=1,column=0)
label3 = Label(text="Km")
label3.grid(row=1, column=2)
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2,column=1)


window.mainloop()