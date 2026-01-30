from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello IKEA NEW "

if __name__ == "__main__":
    app.run(port=8080)
