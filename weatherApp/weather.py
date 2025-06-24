from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk , messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


# Search Box implementation
Search_image=PhotoImage(file ="./search.png")
myImage=Label(image=Search_image)
myImage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=45, y=45)
textfield.focus()

search_icon=PhotoImage(file="./search_icon.png")
myImage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040")
myImage_icon.place(x=400,y=34)

#Placing the logo
Logo_image=PhotoImage(file="./logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)



root.mainloop()