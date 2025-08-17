from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home/index.html")

@app.route("/cursos")
def cursos():
    return render_template("Cursos/index.html")

@app.route("/oportunidades")
def oportunidades():
    return render_template("Oportunidades/index.html")

@app.route("/perfil")
def perfil():
    return render_template("Perfil/index.html")

@app.route("/miscursos")
def miscursos():
    return render_template("MisCursos/index.html")

@app.route("/demo")
def demo():
    return render_template ("Demo/index.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
