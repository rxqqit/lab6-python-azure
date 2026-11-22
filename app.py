
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Azure with Python! V2</h1>
    <p>Виконав: Кісліцин Артем</p>
    <p>Група: КН-24/11</p>
    """

if __name__ == "__main__":
    app.run()
