import os
import pickle
import helpers.db as db

from flask import Flask, render_template, send_from_directory, request
from helpers.cleaner import review_cleaner

app = Flask(__name__, static_folder="public", template_folder="views")

vectorizer = pickle.load(open("model/vectorizer_tfidf.h5", "rb"))
model = pickle.load(open("model/model.h5", "rb"))


@app.route("/")
@app.route("/home.html")
def home():
    return render_template("home.html")


@app.route("/result.html", methods=["POST"])
def result():
    raw_review = request.form.get("review")
    cleaned_review = review_cleaner(raw_review)
    review_bag = vectorizer.transform([cleaned_review]).toarray()
    prediction = model.predict(review_bag)
    pred_string = "Negative sentiment" if prediction[0] == 0 else "Positive sentiment"

    rid = db.add_row(raw_review, pred_string)

    return render_template("result.html", res=pred_string, rid=rid)


@app.route("/data.html")
def data():
    data_li = db.get_data()
    return render_template("data.html", data_li=data_li)


@app.route("/feedback.html")
@app.route("/feedback.html/<submit>")
def feedback(submit=None):
    thanks = True if submit == "submit" else False
    feed_li = db.get_pending_feedback()
    return render_template("feedback.html", feed_li=feed_li, thanks=thanks)


@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    rid = data["rid"]
    feedback = data["feedback"]

    return str(db.update_feedback(rid, feedback))


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    app.run(debug=False)