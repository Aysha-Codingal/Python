from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods = ["POST"])
def calculate():
    units = int(request.form["units"])
    bill = units * 5

    if units <= 100:
        messege = "Great! You Are An Energy Saver! 🌸"

    elif units <= 200:
        messege = "Not Bad! Try Saving A Little More Light! 💡" 

    else:
        messege = "Whoa! Time To Switch Off Some Lights! 😊" 

    return render_template("index.html", units = units, bill = bill, messege = messege)

if __name__ == "__main__":
    app.run(debug = True)
          