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


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        subject = request.form["subject"]

        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, subject=subject)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")
        except:
            return "Error registering user."

    else:
        tasks = User.query.order_by(User.date_created).all()
        return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
