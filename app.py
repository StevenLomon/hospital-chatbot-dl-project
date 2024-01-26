import time
from flask import Flask, render_template, request, jsonify
from chatbot import (
    fuzzy_match,
    predict_tag_v2,
    generate_response,
    update_context,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    current_context = ""

    if request.method == "GET":
        # Render the chat page initially
        return render_template("chat.html")

    elif request.method == "POST":
        if current_context is not None and len(current_context) > 2:
            tag = current_context
        else:
            # Handle the AJAX request for sending messages
            user_message = request.json.get("userMessage")
            fuzzy_check = fuzzy_match(user_message.lower())
            tag = predict_tag_v2(fuzzy_check)

        chatbot_response = generate_response(tag, current_context)
        update_context(tag)
        # current_context = current_context

        time.sleep(1)
        print(current_context)
        return jsonify(
            {"user_message": user_message, "chatbot_response": chatbot_response}
        )


if __name__ == "__main__":
    app.run(debug=True)
