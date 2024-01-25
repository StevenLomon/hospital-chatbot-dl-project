# Example Flask route
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get input from the form
    input_data = request.form["input_data"]

    # Use your model to make predictions
    prediction = your_model.predict(input_data)

    return render_template("result.html", prediction=prediction)
