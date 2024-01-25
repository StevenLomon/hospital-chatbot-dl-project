from flask import Flask, render_template, request
from chatbot import start_chat_v2

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/predict", methods=["POST"])
# def predict():
#     # Get input from the form
#     input_data = request.form["input_data"]

#     # Use your model to make predictions
#     prediction = your_model.predict(input_data)

#     return render_template("result.html", prediction=prediction)

start_chat_v2()
