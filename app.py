from flask import Flask, request

app = Flask(__name__)

@app.before_request
def setup_before_request():
    if request.endpoint == 'home':
        print("Running setup before the first request.")

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

