import tkinter as tk
from tkinter import *
import requests

root = tk.Tk()
root.title('Weather')
root.geometry('400x400')
root.iconbitmap('myicon.ico')

tk.Label(root, text='Weather Forecast').place(x=150, y=10)
tk.Label(root, text='City', font=('Helvetica', 12)).pack(side='bottom')

city_var = StringVar()


def get_var():
    city = city_var.get()
    api_key = '9b9de0494ec0b52f4e2c9306f9c00915'
    try:
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
        print(weather_data.json())
        city_var.set('')
        tk.Label(root,
                 text=f'{city.title()}\n{weather_data.json()["weather"][0]["description"].title()}\n The Temperature is: {int(weather_data.json()["main"]["temp"] - 273.15)}°C',
                 font=('Calibri', 15)).place(x=85, y=150)
        root.img = tk.PhotoImage(file=f'img//{weather_data.json()["weather"][0]["icon"]}.png')
        tk.Label(root, image=root.img).place(x=165, y=225)
    except KeyError:
        tk.Label(root,
                 text=f'No City named: {city.title()}',
                 font=('Calibri', 15)).place(x=85, y=150)


tk.Entry(root, textvariable=city_var).pack(side='bottom')
tk.Button(root, text='Get', command=get_var, ).place(x=185, y=300)

root.mainloop()
