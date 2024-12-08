from flask import Flask
import random

app = Flask(__name__)

facts = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
        "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
        "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
        "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos"]

@app.route("/")
def index():
    return f'<h1>¡Bienvenido! En esta página encontrarás datos curiosos sobre dependencia tecnológica.</h1><a href="/random_fact">¡Ver un dato aleatorio!</a><a href="/secret">¡Cómo se creó!</a>'
    

@app.route("/random_fact")
def text():
    return f'<p>{random.choice(facts)}</p><a href="/random_fact/secret">¡Cómo se creó!</a>'

@app.route("/random_fact/secret")
def secret():
    return f'<p>¡Utilizé Flask para hacer este pequeño proyecto! Aquí hay un link para su documentación.</p><a href="https://flask.palletsprojects.com/en/stable">Link</a>'
app.run(debug=True)
