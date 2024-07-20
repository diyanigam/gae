from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    if (name in "deveg devesh Devesh DEVESH DEVEG Deveg"):
        return render_template('greet.html', name=name)
    return f'Hi, {name} :/'

if __name__ == '__main__':
    app.run(port = 5001, host="0.0.0.0")

