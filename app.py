import os
import pickle

from flask import Flask, render_template, send_from_directory
from tensorflow.keras.models import load_model
from helpers.cleaner import review_cleaner

app = Flask(__name__)

vectorizer = pickle.load(open("model/vectorizer_tfidf.h5","rb"))
model = pickle.load(open("model/model.h5","rb"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result.html/<text>")
def result(text):
    cleaned = review_cleaner(text)
    review_bag = vectorizer.transform([cleaned]).toarray()
    prediction = model.predict(review_bag)
    return render_template("result.html", res="Negative sentiment" if prediction[0] == 0 else "Positive sentiment")


@app.route("/data.html")
def data():
    return render_template("data.html")


@app.route('/favicon.ico')
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=False)