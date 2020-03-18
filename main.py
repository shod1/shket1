from flask_ngrok import run_with_ngrok
from flask import Flask

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def index():
    return 'Привет от приложени Flask'


if __name__ == '__main__':
    app.run()

