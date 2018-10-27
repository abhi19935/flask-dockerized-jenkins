from flask import Flask
app = Flask(__name__)
@app.route("/hi")
def hello():
    print("hurray")
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
