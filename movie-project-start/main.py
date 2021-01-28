from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '<the movie data base secret key>'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


# creating table

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


db.create_all()


# creating form

class EditForm(FlaskForm):
    rating = StringField(label='Your Rating out of 10', validators=[DataRequired()])
    review = StringField(label='Your Review')
    submit = SubmitField(label='Update')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    i = 10
    for movie in all_movies:
        movie.ranking = i
        i -= 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        movie = Movie.query.get(id)
        form = EditForm()
        return render_template('edit.html', movie=movie, form=form)
    if request.method == 'POST':
        new_rating = request.form['rating']
        new_review = request.form['review']
        movie_update = Movie.query.get(id)
        movie_update.rating = float(new_rating)
        if new_review != "":
            movie_update.review = new_review
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/delete/<id>")
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


# movie add form
class AddMovie(FlaskForm):
    title = StringField(label='Name of Movie', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


api = "<the movie database api>"
endpoint = "https://api.themoviedb.org/3/search/movie"


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        add_form = AddMovie()
        return render_template('add.html', form=add_form)
    if request.method == 'POST':
        name_of_movie = request.form['title']
        parameters = {
            'api_key': api,
            'query': name_of_movie
        }
        res = requests.get(endpoint, params=parameters)
        movies = res.json()['results']
        return render_template('select.html', movies=movies)
    return redirect(url_for('home'))


@app.route("/select/<id>")
def select(id):
    movie_endpoint = f"https://api.themoviedb.org/3/movie/{id}?api_key=<the movie databsae api_key>&language=en-US"
    data = requests.get(movie_endpoint).json()
    new_movie = Movie(
        id=id,
        title=data['original_title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=id))


if __name__ == '__main__':
    app.run(debug=True)
