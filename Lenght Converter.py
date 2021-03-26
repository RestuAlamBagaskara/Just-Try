from tkinter import *
from tkinter import messagebox
import tkinter.font as font

tk = Tk()
tk.title("Lenght Converter")
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
            messagebox.showinfo("Error", "Masukkan Jumlah")
        elif w1 == "Select" or w2 == "Select":
            messagebox.showinfo("Error", "Satuan Belum Dipilih")
        else:
            try:
                amount = int(amount)
                if w1 == w2:
                    result = amount
                elif w1 == "km":
                    if w2 == "hm":
                        result = amount*10
                    elif w2 == "dam":
                        result = amount*100
                    elif w2 == "m":
                        result = amount*1000
                    elif w2 == "dm":
                        result = amount*10000
                    elif w2 == "cm":
                        result = amount*100000
                    elif w2 == "mm":
                        result = amount*1000000
                    elif w2 == "Inch":
                        result = amount*100000/2.54
                    elif w2 == "mil":
                        result = amount*1.6093
                    elif w2 == "feet":
                        result = amount*100000/30.48
                    elif w2 == "yard":
                        result = amount*100000/(30.48*3)
                elif w1 == "hm":
                    if w2 == "km":
                        result = amount/10
                    elif w2 == "dam":
                        result = amount*10
                    elif w2 == "m":
                        result = amount*100
                    elif w2 == "dm":
                        result = amount*1000
                    elif w2 == "cm":
                        result = amount*10000
                    elif w2 == "mm":
                        result = amount*100000
                    elif w2 == "Inch":
                        result = amount*10000/2.54
                    elif w2 == "mil":
                        result = amount*1.6093*10
                    elif w2 == "feet":
                        result = amount*10000/30.48
                    elif w2 == "yard":
                        result = amount*10000/(30.48*3)
                elif w1 == "dam":
                    if w2 == "km":
                        result = amount/100
                    elif w2 == "hm":
                        result = amount/10
                    elif w2 == "m":
                        result = amount*10
                    elif w2 == "dm":
                        result = amount*100
                    elif w2 == "cm":
                        result = amount*1000
                    elif w2 == "mm":
                        result = amount*10000
                    elif w2 == "Inch":
                        result = amount*1000/2.54
                    elif w2 == "mil":
                        result = amount*1.6093*100
                    elif w2 == "feet":
                        result = amount*1000/30.48
                    elif w2 == "yard":
                        result = amount*1000/(30.48*3)
                elif w1 == "m":
                    if w2 == "km":
                        result= amount/1000
                    elif w2 == "hm":
                        result = amount/100
                    elif w2 == "dam":
                        result = amount/10
                    elif w2 == "dm":
                        result = amount*10
                    elif w2 == "cm":
                        result = amount/100
                    elif w2 == "mm":
                        result = amount/1000
                    elif w2 == "Inch":
                        result = amount*100*2.54
                    elif w2 == "mil":
                        result = amount*1.6093/1000
                    elif w2 == "feet":
                        result = amount*100/30.48
                    elif w2 == "yard":
                        result = amount*100/(30.48*3)
                elif w1 == "dm":
                    if w2 == "km":
                        result = amount/10000
                    elif w2 == "hm":
                        result = amount/1000
                    elif w2 == "dam":
                        result = amount/100
                    elif w2 == "m":
                        result = amount/10
                    elif w2 == "cm":
                        result = amount*10
                    elif w2 == "mm":
                        result = amount*100
                    elif w2 == "Inch":
                        result = amount*10*2.54
                    elif w2 == "mil":
                        result = amount*1.6093/10000
                    elif w2 == "feet":
                        result = amount*10/30.48
                    elif w2 == "yard":
                        result = amount*10/(30.48*3)
                elif w1 == "cm":
                    if w2 == "km":
                        result = amount/100000
                    elif w2 == "hm":
                        result = amount/10000
                    elif w2 == "dam":
                        result = amount/1000
                    elif w2 == "m":
                        result = amount/100
                    elif w2 == "dm":
                        result = amount/10
                    elif w2 == "mm":
                        result = amount*10
                    elif w2 == "Inch":
                        result = amount/2.54
                    elif w2 == "mil":
                        result = amount*1.6093*100000
                    elif w2 == "feet":
                        result = amount/30.48
                    elif w2 == "yard":
                        result = amount/(30.48*3)
                elif w1 == "mm":
                    if w2 == "km":
                        result = amount/1000000
                    elif w2 == "hm":
                        result = amount/100000
                    elif w2 == "dam":
                        result = amount/10000
                    elif w2 == "m":
                        result = amount/1000
                    elif w2 == "dm":
                        result = amount/100
                    elif w2 == "cm":
                        result = amount/10
                    elif w2 == "Inch":
                        result = amount/2.54/10
                    elif w2 == "mil":
                        result = amount*1.6093*1000000
                    elif w2 == "feet":
                        result = amount/(30.48*10)
                    elif w2 == "yard":
                        result = amount/(30.48*3*10)
                elif w1 == "Inch":
                    if w2 == "km":
                        result = (amount*2.54)/100000
                    elif w2 == "hm":
                        result = (amount*2.54)/10000
                    elif w2 == "dam":
                        result =(amount*2.54)/1000
                    elif w2 == "m":
                        result = (amount*2.54)/100
                    elif w2 == "dm":
                        result = (amount*2.54)/10
                    elif w2 == "cm":
                        result = (amount*2.54)
                    elif w2 == "mm":
                        result = (amount*2.54)*10
                    elif w2 == "mil":
                        result = (amount*1.6093*100000)*2.54
                    elif w2 == "feet":
                        result =( amount/30.48)*2.54
                    elif w2 == "yard":
                        result = (amount/(30.48*3))*2.54
                elif w1 == "mil":
                    if w2 == "km":
                        result = (amount*1.6093)
                    elif w2 == "hm":
                        result = (amount*1.6093)*10
                    elif w2 == "dam":
                        result =(amount*1.6093)*100
                    elif w2 == "m":
                        result = (amount*1.6093)*1000
                    elif w2 == "dm":
                        result = (amount*1.6093)*10000
                    elif w2 == "cm":
                        result = (amount*1.6093)*100000
                    elif w2 == "mm":
                        result = (amount*1.6093)*1000000
                    elif w2 == "Inch":
                        result = ((amount*1.6093)*100000)*2.54
                    elif w2 == "feet":
                        result = ((amount*1.6093)*100000/30.48)
                    elif w2 == "yard":
                        result = ((amount*1.6093)*100000*(30.48*3))
                elif w1 == "feet":
                    if w2 == "km":
                        result = (amount/30.48)/100000
                    elif w2 == "hm":
                        result = (amount/30.48)/10000
                    elif w2 == "dam":
                        result = (amount/30.48)/1000
                    elif w2 == "m":
                        result = (amount/30.48)/100
                    elif w2 == "dm":
                        result = (amount/30.48)/10
                    elif w2 == "cm":
                        result = (amount/30.48)
                    elif w2 == "mm":
                        result = (amount/30.48)*10
                    elif w2 == "mil":
                        result = (amount*1.6093*100000)/30.48
                    elif w2 == "Inch":
                        result =( amount/30.48)/2.54
                    elif w2 == "yard":
                        result = amount/3
                elif w2 == "yard":
                    if w2 == "km":
                        result = (amount*3/30.48)/100000
                    elif w2 == "hm":
                        result = (amount*3/30.48)/10000
                    elif w2 == "dam":
                        result =(amount*3/30.48)/1000
                    elif w2 == "m":
                        result = (amount*3/30.48)/100
                    elif w2 == "dm":
                        result = (amount*3/30.48)/10
                    elif w2 == "cm":
                        result = (amount*3/30.48)
                    elif w2 == "mm":
                        result = (amount*3/30.48)*10
                    elif w2 == "mil":
                        result = (amount*1.6093*100000)*3/30.48
                    elif w2 == "Inch":
                        result =( amount*3/30.48)/2.54
                    elif w2 == "feet":
                        result = amount*3
                print(result)
                label_down["text"] = f"Conversion Result: {amount} {w1}\n{amount} {w1} = {result} {w2}"
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
                clear()
    except Exception:
        messagebox.showerror("Error", "Please try again")
        

def help():
    newwin = Tk()
    newwin.title("Keterangan")
    newwin.minsize(400, 300)
    newwin.maxsize(400, 300)
    newcanvas = Canvas(newwin, height= 400, width = 300)
    newcanvas.pack()
    newframe = Frame(newwin, bg='blue')
    newframe.place(relwidth = 1, relheight = 1)
    newlabel = Label(newframe, font = ("Comic Sans MS", 11, "bold"), fg ="black", anchor = "nw", justify = "left", bd =4)
    newlabel.place(relx = 0.05, rely = 0.05,relwidth = 0.90, relheight = 0.90)
    newlabel["text"] = "Keterangan:\nSAYA RASA SUDAH CUKUP JELAS"
    newbutton = Button(newframe, text = "Back",font = ("Comic Sans MS", 11, "bold"),  bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black", command = lambda:newwin.destroy())
    newbutton.place(relx = 0.76, rely = 0.82, relwidth = 0.14, relheight = 0.11)
    newwin.mainloop()
def exit():
    tk.destroy()

canvas = Canvas(tk, height=HEIGHT, width = WIDTH)
canvas.pack()
frame = Frame(tk, bg='red', bd=7)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.8, relheight = 0.25, anchor='n')

label_up = Label(frame)
label_up.place(relwidth = 1, relheight = 1)

label1 = Label(frame, text = "Dari", font = FONT, bd = 5, bg = 'grey', highlightbackground = 'red', fg = "black")
label1.place(relx = 0.15, rely = 0.02, relwidth = 0.15, relheight = 0.25)

option = [
    "km",
    "hm",
    "dam",
    "m",
    "dm",
    "cm",
    "mm",
    "Inch",
    "mil",
    "feet",
    "yard",
]

clicked1 = StringVar()
clicked1.set("Select")

listbox1 = OptionMenu(frame, clicked1, *option)
listbox1.config(bg='black', fg='yellow', activeforeground="green",activebackground="grey", font=FONT)
listbox1.place(relx = 0.07, rely = 0.3, relheight = 0.25, relwidth= 0.35)

label2 = Label(frame, text="Ke", font = FONT, bd = 5, bg = 'grey', highlightbackground = 'red', fg = "black")
label2.place(relx = 0.64, rely = 0.03, relheight = 0.25, relwidth = 0.15)

clicked2 = StringVar()
clicked2.set("Select")
listbox2 = OptionMenu(frame, clicked2, *option)
listbox2.config(bg='black', fg='yellow', activeforeground="green",activebackground="grey", font=FONT)
listbox2.place(relx = 0.57, rely = 0.3, relheight = 0.25, relwidth= 0.35)

label3 = Label(frame, text = "Panjang", font = FONT,bg ='black', highlightbackground='#12a4d9', fg = "white")
label3.place(relx = 0.26,rely = 0.7,relwidth = 0.2, relheight = 0.25)

entry = Entry(frame, font=FONT, fg = "black")
entry.place(relx = 0.54, rely = 0.7, relwidth=0.26, relheight = 0.25)

button1 = Button(tk, text="Konversi",font=FONT,bg = 'grey', fg='black', activeforeground='white', activebackground = 'black' ,command =lambda:convert(clicked1.get(), clicked2.get(), entry.get()))
button1.place(relx = 0.16, rely = 0.4, relwidth = 0.13, relheight = 0.07)

button2 = Button(tk, text="Bersihkan",font=FONT,bg = 'grey', fg='black', activeforeground='white', activebackground = 'black' ,command = clear)
button2.place(relx = 0.35, rely = 0.4, relwidth = 0.13, relheight = 0.07)

button3 = Button(tk, text="Keterangan",font=FONT,bg = 'grey', fg='black', activeforeground='white', activebackground = 'black' ,command = help)
button3.place(relx = 0.52, rely = 0.4, relwidth = 0.15, relheight = 0.07)

button4 = Button(tk, text="Keluar",font=FONT,bg = 'grey', fg='black', activeforeground='white', activebackground = 'black' ,command = exit)
button4.place(relx = 0.7, rely = 0.4, relwidth = 0.12, relheight = 0.07)

lower_frame = Frame(tk, bg = 'Blue', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.53, relwidth = 0.8, relheight = 0.25, anchor = "n")

FONT = font.Font(family = "Comic Sans MS", size = "12", weight ="bold")
label_down = Label(lower_frame, font = FONT, fg="black", anchor = "nw", justify = 'left', bd = 10)
label_down.place( relwidth=1, relheight = 1)

tk.mainloop()