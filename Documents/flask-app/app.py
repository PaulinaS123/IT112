from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
db = SQLAlchemy(app)

# Define the Song model


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)


# Create the database and tables
with app.app_context():
    db.create_all()

    # Populate database with songs if empty
    if Song.query.count() == 0:
        song1 = Song(title="Bohemian Rhapsody", artist="Queen", year=1975)
        song2 = Song(title="Imagine", artist="John Lennon", year=1971)
        song3 = Song(title="Billie Jean", artist="Michael Jackson", year=1982)
        song4 = Song(title="Like a Rolling Stone",
                     artist="Bob Dylan", year=1965)
        db.session.add_all([song1, song2, song3, song4])
        db.session.commit()

# Route to show all songs


@app.route('/')
def song_list():
    songs = Song.query.all()
    return render_template_string("""
        <h1>Song List</h1>
        <ul>
        {% for song in songs %}
            <li><a href="/songs/{{ song.id }}">{{ song.title }}</a> by {{ song.artist }}</li>
        {% endfor %}
        </ul>
    """, songs=songs)

# Route to show a song detail


@app.route('/songs/<int:song_id>')
def song_detail(song_id):
    song = Song.query.get_or_404(song_id)
    return render_template_string("""
        <h1>{{ song.title }}</h1>
        <p>Artist: {{ song.artist }}</p>
        <p>Year: {{ song.year }}</p>
        <a href="/">Back to list</a>
    """, song=song)


if __name__ == "__main__":
    app.run(debug=True)
