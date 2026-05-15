from flask import Flask

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


@app.route('/')
def home():
    return 'SERVICERUNNING'


if __name__ == '__main__':
    print("SERVICERUNNING")
    app.run(host='0.0.0.0', port=8000)
