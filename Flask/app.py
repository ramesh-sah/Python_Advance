from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import logging
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crud.db"

db = SQLAlchemy(app)


class book(db.Model):
    bookname = db.Column(db.String(80), unique=True,
                         nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title:{}>".format(self.bookname)


@app.route('/', methods=['GET', 'POST'])
def Add():
    logging.info("hello world")
    if request.method == 'POST':
        bookname = request.form.get('bookname')
        add = book(bookname=bookname)
        db.session.add(add)
        db.session.commit()
        logging.info(add)
    showbook = book.query_all()
    logging.info("hello")

    return render_template('home.html', books=showbook)


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
