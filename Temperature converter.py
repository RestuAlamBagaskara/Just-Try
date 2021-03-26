from tkinter import *
from tkinter import messagebox
import tkinter.font as font

tk = Tk()
tk.title("Temperature Converter")
tk.minsize(600,500)
tk.maxsize(600,500)
HEIGHT = 500
WIDTH = 500
FONT = font.Font(family="Comic Sans MS",  size = "10", weight="bold")

#batch of function
def clear():
    entry.delete(0, END)
    label_down["text"] = ""

def convert(w1,w2,amount):
    try:
        if amount == "":
            messagebox.showinfo("Error", "Masukkan Suhu")
        elif w1 == "Select" or w2 == "Select":
            messagebox.showinfo("Error", "Satuan Belum Dipilih")
        else:
            try:
                amount = int(amount)
                if w1 == w2:
                    result = amount
                elif w1 == "Celcius":
                    if w2 == "Reamur":
                        result = amount*(4/5)
                    elif w2 == "Fahrenheit":
                        result = (amount*(9/5))+32
                    elif w2 == "Kelvin":
                        result = amount+273
                elif w1 == "Fahrenheit":
                    if w2 == "Celcius":
                        result = (5/9)*(amount-32)
                    elif w2 == "Reamur":
                        result = (4/9)*(amount-32)
                    elif w2 == "Kelvin":
                        result = (5/9)*(amount+459.4)
                elif w1 == "Reamur":
                    if w2 == "Celcius":
                        result = amount*(5/4)
                    elif w2 == "Fahrenheit":
                        result = (amount*(9/4))+32
                    elif w2 == "Kelvin":
                        result = (amount*(5/4))+273
                elif w1 == "Kelvin":
                    if w2 == "Celcius":
                        result = amount+273
                    elif w2 == "Fahrenheit":
                        result = (amount*(9/4))+32
                    elif w2 == "Reamur":
                        result = (4/5)*(amount-273)
                    
                print(result)
                label_down["text"] = f"Conversion Result: {amount} {w1}\n{amount} {w1} = {result} {w2}"
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
                clear()
    except Exception:
        messagebox.showerror("Error", "Please try again")
        

def exit():
    tk.destroy()

canvas = Canvas(tk, height=HEIGHT, width = WIDTH)
canvas.pack()
frame = Frame(tk, bg='red', bd=7)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.8, relheight = 0.25, anchor='n')

label_up = Label(frame)
label_up.place(relwidth = 1, relheight = 1)

label1 = Label(frame, text = "Dari", font = FONT, bd = 5, bg = 'black', highlightbackground = 'red', fg = "white")
label1.place(relx = 0.15, rely = 0.02, relwidth = 0.15, relheight = 0.25)

option = [
    "Celcius",
    "Fahrenheit",
    "Reamur",
    "Kelvin",
]

clicked1 = StringVar()
clicked1.set("Select")

listbox1 = OptionMenu(frame, clicked1, *option)
listbox1.config(bg='dark blue', fg='orange', activeforeground="red",activebackground="orange", font=FONT)
listbox1.place(relx = 0.07, rely = 0.3, relheight = 0.25, relwidth= 0.35)

label2 = Label(frame, text="Ke", font = FONT, bd = 5, bg = 'black', highlightbackground = 'red', fg = "white")
label2.place(relx = 0.64, rely = 0.03, relheight = 0.25, relwidth = 0.15)

clicked2 = StringVar()
clicked2.set("Select")
listbox2 = OptionMenu(frame, clicked2, *option)
listbox2.config(bg='dark blue', fg='orange', activeforeground="red",activebackground="orange", font=FONT)
listbox2.place(relx = 0.57, rely = 0.3, relheight = 0.25, relwidth= 0.35)

label3 = Label(frame, text = "Panjang", font = FONT,bg ='black', highlightbackground='#12a4d9', fg = "white")
label3.place(relx = 0.26,rely = 0.7,relwidth = 0.2, relheight = 0.25)

entry = Entry(frame, font=FONT, fg = "black")
entry.place(relx = 0.54, rely = 0.7, relwidth=0.26, relheight = 0.25)

button1 = Button(tk, text="Konversi",font=FONT,bg = 'orange', fg='black', activeforeground='white', activebackground = 'black' ,command =lambda:convert(clicked1.get(), clicked2.get(), entry.get()))
button1.place(relx = 0.16, rely = 0.4, relwidth = 0.13, relheight = 0.07)

button2 = Button(tk, text="Bersihkan",font=FONT,bg = 'orange', fg='black', activeforeground='white', activebackground = 'black' ,command = clear)
button2.place(relx = 0.43, rely = 0.4, relwidth = 0.13, relheight = 0.07)

button4 = Button(tk, text="Keluar",font=FONT,bg = 'orange', fg='black', activeforeground='white', activebackground = 'black' ,command = exit)
button4.place(relx = 0.7, rely = 0.4, relwidth = 0.12, relheight = 0.07)

lower_frame = Frame(tk, bg = 'blue', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.53, relwidth = 0.8, relheight = 0.25, anchor = "n")

FONT = font.Font(family = "Comic Sans MS", size = "12", weight ="bold")
label_down = Label(lower_frame, font = FONT, fg="black", anchor = "nw", justify = 'left', bd = 10)
label_down.place( relwidth=1, relheight = 1)

tk.mainloop()