from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def show_resume():
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    user_skills = request.form.get('skills')
    user_about = request.form.get('about')

    return render_template(
        'resume.html',
        name=user_name,
        email=user_email,
        skills=user_skills,
        about=user_about
    )

if __name__ == '__main__':
    app.run(debug=True)