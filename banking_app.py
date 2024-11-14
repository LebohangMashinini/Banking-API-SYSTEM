from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banking.db"
db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return '<Account %r, Balance %r>' % (self.id, self.balance)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_account/<int:id>", methods=["GET", "POST"])
def create_account(id):
    return ""



if __name__ == "__main__":
    app.run(debug=True)