from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Solo el nombre del archivo

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
