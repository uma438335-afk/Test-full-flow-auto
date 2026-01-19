from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello IKEA now"

if __name__ == "__main__":
    app.run(port=8080)
