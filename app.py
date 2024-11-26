import json
import requests
from flask import render_template, request, url_for, redirect

# secret_key and api
from config import *

from main import *

'''
main page where client pick city
post from form
or redirect from static/js/script.js
'''
@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        city = request.form['city']
        return redirect(url_for('get_weather', city=city))
    return render_template('main.html', title='Weather')

''' 
http post request from static/js/script.js with client geo.
return city
'''
@app.route('/get_cords', methods=['POST'])
def get_cords():
    data = request.get_json()
    lat = data['lat']
    lon = data['lon']
    city = get_city(lat, lon)
    return {'city': city}

'''
return page with actual weather
takes data from api
'''
@app.route('/<city>')
def get_weather(city):
    if get_location(city):
        lat, lon = get_location(city)
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'lat': lat, 'lon': lon, 'appid': weather_api, 'units': 'metric', 'lang': 'ru'}
        response = requests.get(url, params=params)
        data = json.loads(response.text)

        weather = data['weather'][0]['description']
        temp = f'{data['main']['temp']}°'
        feels_like = f'{data['main']['feels_like']}°'
        wind_speed =f'{data['wind']['speed']} м/с'
        return render_template(weather.html, title='Weather',
                               weather=weather, temp=temp,
                               feels_like=feels_like, wind_speed=wind_speed)
    return 'Не знаем такого города :/'

if __name__ == '__main__':
    app.run(debug=True)
