from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({
                "visitors": 0,
                "rating_sum": 0,
                "rating_count": 0
            }, f)

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.route("/")
def home():

    data = load_data()

    data["visitors"] += 1

    save_data(data)

    average = 0

    if data["rating_count"] > 0:
        average = round(data["rating_sum"] / data["rating_count"], 1)

    return render_template(
        "index.html",
        visitors=data["visitors"],
        average=average,
        ratings=data["rating_count"]
    )


@app.route("/rate", methods=["POST"])
def rate():

    rating = int(request.json["rating"])

    data = load_data()

    data["rating_sum"] += rating

    data["rating_count"] += 1

    save_data(data)

    average = round(data["rating_sum"] / data["rating_count"], 1)

    return jsonify({
        "average": average,
        "ratings": data["rating_count"]
    })


if __name__ == "__main__":
    app.run(debug=True)