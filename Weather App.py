import tkinter
from tkinter import *
import customtkinter
import requests


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")





def function():
    user_input = input_user.get()
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    
    if weather_data.json()['cod'] == '404':
        label2.configure(text= 'No city Found, try again')
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        celsius = (temp - 32)* 5/9

        label1.configure(text=f"{user_input} is : {weather}")
        label2.configure(text= f"{user_input} is : {celsius:2f} oC")



api_key = '59083c8cfa19f6b54a89051322b113db'

app = customtkinter.CTk()
app.geometry('500x450')
app.title("Weather Application")
FontApp1 = ('Poppins', 32, 'bold')
FontApp2 = ('Poppins', 20,)





label = customtkinter.CTkLabel(app, text='Weather Application', text_color='white', font=FontApp1, width=300, height=85)
label.pack(padx =20, pady=5)

input_user = customtkinter.CTkEntry(app, placeholder_text="City", width=280, height=45, corner_radius=8, border_width=1.5, border_color='#3F4443')
input_user.pack(padx=20, pady=5)


button = customtkinter.CTkButton(app, text="Search", command=function, width=200, height=40, corner_radius=8, border_width=1.5, border_color='#3F4443')
button.pack(padx=40, pady=30)

label1 = customtkinter.CTkLabel(app, text="", text_color="white", font=FontApp2, width=300, height=2)
label1.pack(padx=20, pady=2)

label2 = customtkinter.CTkLabel(app, text="", text_color="white", font=FontApp2, width=300, height=2)
label2.pack(padx=20, pady=20)


app.mainloop()