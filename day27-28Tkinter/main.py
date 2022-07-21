from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    number = int(new_text) * 1.609
    my_label.config(text=number)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="0", font=("Arial", 10, "bold",))
my_label.config(text="0")
my_label.grid(column=2, row=1)
my_label.config(padx=0, pady=0)

my_label2 = Label(text="is equal to", font=("Arial", 10, "bold",))
my_label2.config(text="is equal to")
my_label2.grid(column=0, row=1)
my_label2.config(padx=0, pady=0)

my_label3 = Label(text="Miles", font=("Arial", 10, "bold",))
my_label3.config(text="Miles")
my_label3.grid(column=3, row=0)
my_label3.config(padx=0, pady=0)

my_label4 = Label(text="Km", font=("Arial", 10, "bold",))
my_label4.config(text="Km")
my_label4.grid(column=3, row=1)
my_label4.config(padx=0, pady=0)


#Button

new_button = Button(text="Calculate", command=button_clicked)
new_button.config(text="Calculate")
new_button.grid(column=2, row=2)


#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=0)









window.mainloop()