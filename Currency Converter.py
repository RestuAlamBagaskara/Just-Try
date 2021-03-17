from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

tk = Tk()
tk.title("Real Time Currency Converter")
tk.minsize(600,500)
tk.maxsize(600,500)
HEIGHT = 500
WIDTH = 500
FONT = font.Font(family="Comic Sans MS",  size = "10", weight="bold")

#batch of function
def clear():
    entry.delete(0, END)
    label_down["text"] = ""

def convert(c1,c2,amount):
    try:
        if amount == "":
            messagebox.showerror("Error", "Amount not specified")
        elif c1 == "Select" or c2 == "Select":
            messagebox.showinfo("Error", "Currency not selected")
        else:
            try:
                amount = float(amount)
                b = BtcConverter()
                c = CurrencyRates()
                if c1 == c2:
                    result = amount
                elif c1 == "BTC":
                    result = b.convert_btc_to_cur(amount, c2)
                elif c2 == "BTC":
                    result = b.convert_to_btc(amount, c1)
                else:
                    result = c.convert(c1, c2, int(amount))
                print(result)
                label_down["text"] = f"Conversion Result: {amount} {c2}\n{amount} {c1} = {result} {c2}"
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
                clear()
    except Exception:
        messagebox.showerror("Error", "Please try again")
        

def help():
    newwin = Tk()
    newwin.title("Reference")
    newwin.minsize(400, 300)
    newwin.maxsize(400, 300)
    newcanvas = Canvas(newwin, height= 400, width = 300)
    newcanvas.pack()
    newframe = Frame(newwin, bg='blue')
    newframe.place(relwidth = 1, relheight = 1)
    newlabel = Label(newframe, font = ("Comic Sans MS", 11, "bold"), fg ="black", anchor = "nw", justify = "left", bd =4)
    newlabel.place(relx = 0.05, rely = 0.05,relwidth = 0.90, relheight = 0.90)
    newlabel["text"] = "Abbrevations:\nIDR - Indonesia Rupiah\nUSD - USD Dollar\nEUR - Euro\nJPY - Japnese Yen\nGBP - Pound Sterling\nAUD - Australian Dollar\nCAD - Canadian Dollar\nCHF - Swiss Frank\nINR - Indian Rupees\nRUB - Russian Rubble\nCNY - Chinese Yuan"
    newbutton = Button(newframe, text = "Back",font = ("Comic Sans MS", 11, "bold"),  bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black", command = lambda:newwin.destroy())
    newbutton.place(relx = 0.76, rely = 0.82, relwidth = 0.14, relheight = 0.11)
    newwin.mainloop()
def exit():
    tk.destroy()

canvas = Canvas(tk, height=HEIGHT, width = WIDTH)
canvas.pack()
frame = Frame(tk, bg='yellow', bd=7)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.8, relheight = 0.25, anchor='n')

label_up = Label(frame)
label_up.place(relwidth = 1, relheight = 1)

label1 = Label(frame, text = "From", font = FONT, bd = 5, bg = 'pink', highlightbackground = 'red', fg = "white")
label1.place(relx = 0.15, rely = 0.02, relwidth = 0.15, relheight = 0.25)

option = [
    "IDR",
    "USD",
    "EUR",
    "JPY",
    "GBP",
    "AUD",
    "CAD",
    "CHF",
    "INR",
    "RUB",
    "CNY"
]

clicked1 = StringVar()
clicked1.set("Select")

listbox1 = OptionMenu(frame, clicked1, *option)
listbox1.config(bg='black', fg='white', activeforeground="Grey", font=FONT)
listbox1.place(relx = 0.07, rely = 0.3, relheight = 0.25, relwidth= 0.35)

label2 = Label(frame, text="To", font = FONT, bd = 5, bg = 'pink', highlightbackground = 'red', fg = "white")
label2.place(relx = 0.64, rely = 0.03, relheight = 0.25, relwidth = 0.15)

clicked2 = StringVar()
clicked2.set("Select")
listbox2 = OptionMenu(frame, clicked2, *option)
listbox2.config(bg='black', fg='white', activeforeground="Grey", font=FONT)
listbox2.place(relx = 0.57, rely = 0.3, relheight = 0.25, relwidth= 0.35)

label3 = Label(frame, text = "Amount", font = FONT,bg ='black', highlightbackground='#12a4d9', fg = "white")
label3.place(relx = 0.26,rely = 0.7,relwidth = 0.2, relheight = 0.25)

entry = Entry(frame, font=FONT, fg = "black")
entry.place(relx = 0.54, rely = 0.7, relwidth=0.26, relheight = 0.25)

button1 = Button(tk, text="Convert",font=FONT,bg = 'pink', fg='black', activeforeground='pink', activebackground = 'black' ,command =lambda:convert(clicked1.get(), clicked2.get(), entry.get()))
button1.place(relx = 0.16, rely = 0.4, relwidth = 0.13, relheight = 0.07)

button2 = Button(tk, text="Clear",font=FONT,bg = 'pink', fg='black', activeforeground='pink', activebackground = 'black' ,command = clear)
button2.place(relx = 0.35, rely = 0.4, relwidth = 0.13, relheight = 0.07)

button3 = Button(tk, text="Refrence",font=FONT,bg = 'pink', fg='black', activeforeground='pink', activebackground = 'black' ,command = help)
button3.place(relx = 0.52, rely = 0.4, relwidth = 0.15, relheight = 0.07)

button4 = Button(tk, text="Exit",font=FONT,bg = 'pink', fg='black', activeforeground='pink', activebackground = 'black' ,command = exit)
button4.place(relx = 0.7, rely = 0.4, relwidth = 0.12, relheight = 0.07)

lower_frame = Frame(tk, bg = 'green', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.53, relwidth = 0.8, relheight = 0.25, anchor = "n")

FONT = font.Font(family = "Comic Sans MS", size = "12", weight ="bold")
label_down = Label(lower_frame, font = FONT, fg="black", anchor = "nw", justify = 'left', bd = 10)
label_down.place( relwidth=1, relheight = 1)

tk.mainloop()