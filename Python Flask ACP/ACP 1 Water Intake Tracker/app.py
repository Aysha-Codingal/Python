from flask import Flask, render_template, request
 
app = Flask(__name__)
 
 
@app.route("/")
def home():
    return render_template("index.html")
 
 
@app.route("/track", methods=["POST"])
def track_water():
 
    name = request.form["name"]
    goal = int(request.form["goal"])
    glasses = int(request.form["glasses"])
 
    remaining = goal - glasses
 
    if glasses >= goal:
        message = "Great job! You reached your water intake goal today."
        status = "Goal completed"
        
    else:
        message = "Keep going! You still need to drink more water."
        status = "Goal not completed"

    return render_template(
        "index.html",
        name = name,
        goal = goal,
        glasses = glasses,
        remaining = remaining,
        message = message,
        status = status
    )
 
 
if __name__ == "__main__":
    app.run(debug=True)
