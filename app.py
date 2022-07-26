from flask import Flask, render_template  # do módulo flask, importar a classe Flask


app = Flask ("hello") # por convenção, o nome da variável é app

# todos os recursos usados vão partir da variável. Ex.: app.route

@app.route("/")
@app.route("/hello")

def hello():
    return "Hello World"

#nova rota:

@app.route("/meucontato")
def meuContato():
    return render_template('index.html')
    
