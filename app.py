from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "🎨 Interior Design App"


@app.route('/about')
def about():
    return "Hi, I'm Victoria! and I love interior Design and also I'm learning Flask."


if __name__ == '__main__':
    app.run(debug=True)
