from tkinter import *
import qrcode

root = Tk()
root.title("QR Code Generator")
root.geometry("700x500")
root.configure(bg="#c23c3c")
root.resizable(False, False)

#image = PhotoImage(file="QR/qr.png")
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

def generate():
    name = title.get()
    text = entry.get()
    qr =qrcode.make(text)
    qr.save("QR/" + str(name) + ".png")

    Image = PhotoImage(file="QR/" + str(name) + ".png")
    Image_view.config(image)

Image_view = Label(root, bg="#AE2321")
Image_view.pack(padx=50, pady=50,side=RIGHT)

Label(root,text="Title", fg="white",bg="#AE2321", font=15).place(x=50,y=170)

title=Entry(root, width=13, font="arial 15")
title.place(x=50,y=200)

entry=Entry(root, width=18, font="arial 15")
entry.place(x=50,y=250)

Button(root,text="Generate QR Code", bg="#AE2321", fg="white", font="arial 15", command=generate).place(x=50,y=300)

root.mainloop()