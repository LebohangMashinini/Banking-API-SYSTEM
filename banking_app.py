from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder="./templates")
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

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        email = request.form.get("email")
        return f"Email recived: {email}"
    return render_template("create_account.html")

@app.route("/view_balance", methods=["GET", "POST"])
def view_balance():
    return render_template("view_balance.html")


if __name__ == "__main__":
    app.run(debug=True)