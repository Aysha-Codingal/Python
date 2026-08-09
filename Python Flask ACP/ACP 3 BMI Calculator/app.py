from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    status = None
    
    if requests.method == 'POST':
        try:
            weight = float(requests.form.get('weight', 0))
            height = float(requests.form.get('height', 0))
            
            if height > 0:
                bmi = round(weight / ((height / 100) ** 2), 2)
                if bmi < 18.5:
                    status = "Underweight"
                elif 18.5 <= bmi < 25:
                    status = "Normal weight"
                else:
                    status = "Overweight"
        except (ValueError, TypeError):
            pass

    return render_template('index.html', bmi=bmi, status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)