from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "thisisoursecret"
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# you can also create a user login and relate their todos to specific users

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(250), nullable=False)

class DoneTodos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(250), nullable=False)


db.create_all()


class Form(FlaskForm):
    todo = StringField(label="todo", validators=[DataRequired()])
    submit = SubmitField(label="add todo")


@app.route("/")
def home():
    all_todos = db.session.query(Todos).all()
    done_todos = db.session.query(DoneTodos).all()
    return render_template('index.html', todos=all_todos, done_todos=done_todos)


@app.route("/add-todo", methods=['GET', 'POST'])
def add_todo():
    form = Form()
    if request.method == 'POST':
        if form.validate_on_submit():
            todo = form.todo.data
            new_todo = Todos(item=todo)
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('form.html', form=form)


@app.route("/delete-todo/<int:id>")
def delete_todo(id):
    del_todo = Todos.query.get(id)
    db.session.delete(del_todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/done-todo/<int:id>")
def done_todo(id):
    item = Todos.query.get(id)
    name = item.item
    done = DoneTodos(item=name)
    db.session.add(done)
    db.session.commit()
    return redirect(url_for('delete_todo', id=id))


if __name__ == "__main__":
    app.run(debug=True)
