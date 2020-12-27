from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result.html")
def result():
    return render_template("result.html")


@app.route("/data.html")
def data():
    return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=False)