import requests
from flask import Flask, render_template, redirect, request, flash


app = Flask(__name__)


@app.route('/')
@app.route('/city')
def home():
    return render_template('index.html')
@app.route('/city', methods=['GET', 'POST'])
def city():
    if request.method == 'POST':
        try:
            city = request.form['city'].capitalize()
            api_key = 'bbf02f6c2bc9cf7676e9928e294b82b3'
            con = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
            data = con.json()
            temp = data['main']['temp']
            celciusz = int(round(temp-273.15,0))
            weather = data['weather'][0]['main']
            desc = data['weather'][0]['description']
            pressure = data['main']['pressure']
            country = data['sys']['country']
            wind = data['wind']['speed']    
            print(desc)
            return render_template('index.html', city=city, celciusz = celciusz, pressure=pressure, country=country, weather=weather, desc=desc, wind=wind)
        except KeyError:
            error = f"City '{city}' does not exist"
            return render_template('index.html', error=error,)


if __name__=='__main__':
    app.run(debug=True)