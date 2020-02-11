from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    response = requests.get(
        'https://api.github.com/users/edipojuan', verify=False)
    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        return "Nenhum valor encontrado."


@app.route("/test")
def test():
    return "Test!"
