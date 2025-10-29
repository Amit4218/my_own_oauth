from flask import Flask, render_template, request
from utils.env_provider import DATABASE_URL, PORT
from flask_bcrypt import Bcrypt


app = Flask("__name__")
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL


@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/app-health")
def app_health():
    return {"status": "success"}


@app.route("/register", methods=["POST"])
def register():
    if request.method == "post":
        email: str = request.form["email"].strip()
        password: str = request.form["password"].strip()

        if not email or password:
            return "All feilds required!"

    # hash the password and store in db

    hash_password: str = bcrypt.generate_password_hash(password=password, rounds=10)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=PORT, debug=True)
