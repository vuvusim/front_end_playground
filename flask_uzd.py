from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Labas rytas!"

@app.route("/labas")
def labas():
    return render_template("labas.html")

if __name__ == "__main__":
    app.run(debug=True)