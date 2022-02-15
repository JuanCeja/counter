
from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "21"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] = session['count'] + 1
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def counter():
    print("im here")
    if 'count' not in session:
        session['count'] = 0
    session['count'] = session['count'] + 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)