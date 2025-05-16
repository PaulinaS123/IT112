from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return "🎨 Interior Design App"


@app.route('/about')
def about():
    return "Hi, I'm Victoria! and I love interior design. I'm also learning Flask."


@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        number = request.form['number']

        fortunes = {
            ('red', '1'): "You will have a week full of surprises.",
            ('blue', '2'): "Someone will make you smile soon.",
            ('green', '3'): "An unexpected opportunity is coming.",
            ('yellow', '4'): "Someone new will come into your life soon.",
            ('red', '5'): "You will have good luck today.",
        }

        fortune_text = fortunes.get(
            (color, number), "Good things are heading your way!")

        return render_template('fortune_result.html', name=name, color=color, number=number, fortune=fortune_text)

    return render_template('fortune_form.html')


if __name__ == '__main__':
    app.run(debug=True)
