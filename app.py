from flask import Flask, render_template  
from datetime import datetime

app = Flask ("hello") 

# lista de dicionários:
posts = [
    {
        "title": "O meu primeiro post",
        "body": "Aqui é o texto do post",
        "author": "Feulo",
        "created": datetime(2022, 7, 25)
    },
     {
        "title": "O meu segundo post",
        "body": "Aqui é o texto do post",
        "author": "Danilo",
        "created": datetime(2022, 7, 26)
    }
]

@app.route("/")
def index(): #padrão de nomear esse tipo de função
    return render_template("index.html", posts = posts) #vai ter uma variável posts no html 
    #que recebe posts daqui

