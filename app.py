from flask import Flask, render_template

app = Flask(__name__)


# Index.html
@app.route("/")
def index():
    return render_template("index.html")


# Inicio.html
@app.route("/inicio")
def inicio():
    return render_template("inicio.html")


if __name__ == "__main__":
    app.run(debug=True)
