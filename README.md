Weather App README

Introduction
This Weather App is a simple tool built using Python and Tkinter library to fetch and display weather information for a given city. It utilizes the OpenWeatherMap API to retrieve real-time weather data.

Requirements
Python 3.x
tkinter library
requests library
dotenv library

Installation

Clone this repository to your local machine using the following command:
git clone https://github.com/whitedevl007/weather_updates.git

Navigate to the project directory:
cd your-repo

Install the required libraries using pip:
pip install -r requirements.txt


Usage
Sign up for an account on OpenWeatherMap to get your API key.
Create a .env file in the root directory of the project and add your API key:
makefile
Copy code
OPENWEATHER_APIKEY=your-api-key-here
Run the application:
Copy code
python weather_app.py

Once the app window opens, enter the name of the city you want to get the weather information for in the provided text field.
Click on the "Get Result" button.
The app will display the current weather condition, temperature, minimum and maximum temperature, pressure, humidity, and wind speed for the entered city.


License
This project is licensed under the MIT License. Feel free to modify and distribute it according to your needs.


Acknowledgements
OpenWeatherMap for providing the weather data API.
dotenv library for managing environment variables.
Tkinter library for building the graphical user interface.
