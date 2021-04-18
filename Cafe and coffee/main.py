from flask import Flask, request, render_template, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.secret_key = 'ourlittlesecret'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)




class AddCafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Location on map", validators=[DataRequired(), URL()])
    img_url = StringField("Image", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = BooleanField("Has Sockets")
    has_toilet = BooleanField("Has Toilet")
    has_wifi = BooleanField("Has WIFI")
    can_take_calls = BooleanField("Can take calls")
    seats = StringField("Number of seats", validators=[DataRequired()])
    coffee_price = StringField("Price of Coffee", validators=[DataRequired()])
    submit = SubmitField("Add my cafe")


@app.route("/")
def home():
    all_cafes = db.session.query(Cafe).all()
    print(all_cafes)
    return render_template('index.html', all_cafes=all_cafes)

@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    form = AddCafeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            map_url = form.map_url.data
            img_url = form.img_url.data
            location = form.location.data
            has_sockets = form.has_sockets.data
            has_toilet = form.has_toilet.data
            has_wifi = form.has_wifi.data
            can_take_calls = form.can_take_calls.data
            seats = form.seats.data
            coffee_price = form.coffee_price.data
            print(name, map_url, has_wifi, can_take_calls, seats, coffee_price)
            new_cafe = Cafe(name=name, map_url=map_url, img_url=img_url, location=location, has_toilet=has_toilet,
                     has_sockets=has_sockets, has_wifi=has_wifi, can_take_calls=can_take_calls, seats=seats,
                            coffee_price=coffee_price)
            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for('home  '))
        else:
            print('code not working')
    return render_template('add.html', form=form)

@app.route("/delete")
def delete_cafe():
    del_id = request.args.get('id')
    cafe_to_delete = Cafe.query.get(del_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)