from flask import Flask, render_template, request, redirect, url_for
from data_fetch import search_word

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        word = request.form.get('word')
        data = search_word(word)
        return render_template('index.html', data=data)
    return render_template('index.html', data=[])


if __name__ == "__main__":
    app.run(debug=True)
