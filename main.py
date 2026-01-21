from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello IKEA "

if __name__ == "__main__":
    app.run(port=8080)
