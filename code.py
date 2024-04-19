import tkinter as tk
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def getWeather():
    city = textField.get()
    api_key = os.environ.get('OPENWEATHER_APIKEY')
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    json_data = requests.get(api_url).json()
    
    condition = json_data['weather'][0]['main']
    temp = json_data['main']['temp']
    min_temp = json_data['main']['temp_min']
    max_temp = json_data['main']['temp_max']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind)
    
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

smallText = ("poppins", 15, "bold")
largeText = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=largeText)
submitButton = tk.Button(canvas, text="Get Result", command=getWeather)

textField.pack(pady=20)
submitButton.pack(pady=15)
textField.focus()

label1 = tk.Label(canvas, font=largeText)
label1.pack()
label2 = tk.Label(canvas, font=smallText)
label2.pack()

canvas.mainloop()