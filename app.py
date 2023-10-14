from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, unique=True)
    subject = db.Column(db.String(50), nullable=False)
    is_student = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}"


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    review = db.Column(db.String(20000), nullable=False)
    
    def __repr__(self):
        return f"<Review {self.first_name} {self.last_name} {self.review}"


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")
    
# >>> from app import db, User
# >>> db.create_all()
# >>> user = User(first_name="gabe", last_name="gabe", email="gabe@gabe.gabe", password="gabe123", subject="GABE", is_student=1)
#                                                               >>> db.session.add(user)
# >>> db.session.commit()
@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        subject = request.form["subject"]
        
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, subject=subject.upper(), is_student=0)

        db.session.add(new_user)
        db.session.commit()
        return redirect("/signup")
        
    else:
        return render_template("signup.html")

@app.route('/signin', methods=["POST", "GET"])
def signin():
    return render_template("signin.html")

@app.route('/submit_review', methods=["POST"])
def submit_review():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        review = request.form["review"]

        new_review = Review(first_name=first_name, last_name=last_name, email=email, review=review)

        db.session.add(new_review)
        db.session.commit()
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
