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


def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location =geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home =pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")



# Search Box implementation
Search_image=PhotoImage(file ="./search.png")
myImage=Label(image=Search_image)
myImage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=45, y=45)
textfield.focus()

search_icon=PhotoImage(file="./search_icon.png")
myImage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040", command=getWeather)
myImage_icon.place(x=400,y=34)

#Placing the logo
Logo_image=PhotoImage(file="./logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Buttonbox
Frame_image=PhotoImage(file="./box.png")
frame_myImage=Label(image=Frame_image)
frame_myImage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial", 15, "bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvitica",20))
clock.place(x=30,y=130)


#label
#wind
label1=Label(root,text="Wind", font=("Helvetica",15,'bold'),fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

#
label2=Label(root,text="Humidity", font=("Helvetica",15,'bold'),fg="white", bg="#1ab5ef")
label2.place(x=225, y=400)

#
label3=Label(root,text="Description", font=("Helvetica",15,'bold'),fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

#
label4=Label(root,text="Pressure", font=("Helvetica",15,'bold'),fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)


t=Label(font=("arial",70, "bold"), fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=255,y=430)

d=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450,y=430)

p=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=680,y=430)



root.mainloop() 
