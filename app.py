import os
from flask import Flask, render_template, request
from chatbot import (
    start_chat_v2,
    fuzzy_match,
    predict_tag_v2,
    generate_response,
    update_context,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    current_context = ""

    # Get input from the form
    input_data = request.form["userinput"]
    print("Input Data:", input_data)

    # Use your model to make predictions
    fuzzy_check = fuzzy_match(input_data.lower())
    tag = predict_tag_v2(fuzzy_check)
    response = generate_response(tag, current_context)
    print(f"Response Data: {response}")
    update_context(tag)

    return render_template("result.html", response=response)


# os.system("CLS")
# start_chat_v2()

if __name__ == "__main__":
    current_context = ""
    input_data = "Hello there!"
    response = generate_response(input_data, current_context)
    print(f"Response Data: {response}")
    app.run(debug=True)
