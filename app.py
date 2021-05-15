from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show():
    return render_template('index.html', message='Main Flask message')

def __app_run():
    app_port = 5000
    app.run(host='0.0.0.0', port=app_port, debug=True)

if __name__ == '__main__':
    __app_run()
