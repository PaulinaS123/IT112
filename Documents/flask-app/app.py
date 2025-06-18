
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


from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Song model


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f'<Song {self.title} by {self.artist}>'


# Create DB tables if they don't exist
with app.app_context():
    db.create_all()

# 📤 Route: Return all items as JSON (API)


@app.route('/api/items', methods=['GET'])
def get_items():
    songs = Song.query.all()
    items_list = [{'id': song.id, 'title': song.title,
                   'artist': song.artist, 'year': song.year} for song in songs]
    response = jsonify(items_list)
    response.headers['Content-Type'] = 'application/json'
    return response, 200

# 📥 Route: Insert a new item from POST JSON (API)


@app.route('/api/items', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        new_song = Song(title=data['title'],
                        artist=data['artist'], year=data['year'])
        db.session.add(new_song)
        db.session.commit()
        return jsonify({'message': 'Song added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ✅ Route: Homepage with song list (Web)


@app.route('/')
def index():
    songs = Song.query.all()
    return render_template('index.html', songs=songs)

# ✅ Route: Song detail page (Web)


@app.route('/songs/<int:id>')
def song_detail(id):
    song = Song.query.get_or_404(id)
    return render_template('detail.html', song=song)


# Run the app

if __name__ == '__main__':
    app.run(debug=True)
