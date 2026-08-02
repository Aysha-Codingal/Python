from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "93e941f4bb3c74ab05ce330b81ec2e9a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

@app.route("/")
def home():
    return render_template("index.html",weather = None, error = None)

@app.route("/weather", methods = ["POST"])
def weather():
    city = request.form['city']
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        weather_data = {
            "country_code": data['sys']['country'],
            "temprature": data["main"]["temp"],
            "location": data["name"],
        } 

        return render_template('index.html', weather = weather_data, error = None)
    else:
        return render_template('index.html', weather = None, error = "City Not Found !")
    
if __name__ == "__main__":
    app.run(debug = True)
          