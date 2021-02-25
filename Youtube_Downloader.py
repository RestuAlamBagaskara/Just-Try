from tkinter import * 
from pytube import YouTube

tk = Tk()
tk.geometry("350x500")
tk.title("Download Video from Youtube")
def unduh():
    try:
        var.set("Sedang Mendownload...")
        tk.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video Sukses diDownload")
    except Exception as e:
        var.set("Link Tidak Ditemukan")
        tk.update()
        link.set("Masukkan Link")

Label(tk, text= "Silakan Download Video Anda", font= "Consolan 13 bold").pack()
var = StringVar()
var.set("Masukkan Link di Bawah")
Entry(tk, textvariable=var, width = 50).pack()
link = StringVar()
Entry(tk, textvariable=link, width = 50).pack()
Button(tk, text="Download", command = unduh).pack()
tk.mainloop()