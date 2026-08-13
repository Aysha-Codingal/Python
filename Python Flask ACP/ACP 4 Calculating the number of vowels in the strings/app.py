from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        count = 0
        
        for char in text:
            if char.lower() in 'aeiou':
                count += 1
                
        return render_template_string("<h2>Calculate Number of Vowels in Given String</h2><form method='POST' action='/'><label>Enter String:</label><input type='text' name='text' required><button type='submit'>Submit</button></form>{% if count is defined %}<h3>Entered Text: {{ text }}</h3><h3>Number of Vowels: {{ count }}</h3>{% endif %}", count=count, text=text)
    
    return render_template_string("<h2>Calculate Number of Vowels in Given String</h2><form method='POST' action='/'><label>Enter String:</label><input type='text' name='text' required><button type='submit'>Submit</button></form>")

if __name__ == '__main__':
    app.run(port=5000, debug=True)