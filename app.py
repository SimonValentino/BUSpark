from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    subject = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}"


@app.route('/', methods=["ID", "FIRSTNAME", "LASTNAME", "EMAIL", "SUBJECT"])
def index():
    if request.method == "ID":
        pass
    
    elif request.method == "FIRSTNAME":
        pass
    
    elif request.method == "LASTNAME":
        pass
    
    elif request.method == "EMAIL":
        pass
    
    elif request.method == "SUBJECT":
        pass
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
