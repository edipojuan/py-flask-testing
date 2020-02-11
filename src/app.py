from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Testtt123!"


@app.route("/test")
def test():
    return "Test!"
