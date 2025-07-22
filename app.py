from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'fd8242461fef0affcd2d4e276de346e8'  

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None
    error = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data['cod'] == '404':
            error = 'City not found.'
        else:
            weather = {
                'city': city,
                'description': data['weather'][0]['main'],
                'temperature': round(data['main']['temp'])
            }
    return render_template('index.html', weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)
