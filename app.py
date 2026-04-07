from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Cloud computing is just someone else's computer.",
    "Why did the server crash? Too many requests.",
    "I told my app to scale, it went vertical."
]

@app.route("/")
def home():
    return random.choice(jokes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
