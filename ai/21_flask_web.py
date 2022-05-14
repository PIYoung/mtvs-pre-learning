from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
def index(name):
    return render_template("21_index.html", username=name)


@app.route("/wheather/<city>")
def weather(city):
    return city


if __name__ == "__main__":
    app.run(debug=True)  # 127.0.0.1:5000

