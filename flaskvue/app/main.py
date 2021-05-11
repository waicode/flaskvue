from flask import render_template
from flaskvue import app

@app.route('/', methods=['GET'])
def show():
    return render_template('index.html')