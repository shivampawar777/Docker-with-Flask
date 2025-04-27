from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<br><br><h1 style="text-align: center">This response is from Flask application...</h1>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)

