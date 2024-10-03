from flask import (Flask, request) # Importa o flask

app = Flask(__name__) # Cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota

def index(): # Função responsável pela página

    nome = request.args.get ('nome')

     # HTML retornado
    return f"""<h1>Página inicial</h1><p>Olá {nome}, que nome bonito!</p>""" 


@app.route("/galeria", methods=('GET',)) 
def galeria(): 
    return "<h1>Galeria</h1><p>Página da Galeria</p>" 


@app.route("/contato", methods=('GET',)) 
def contato():
    return "<h1>Contato </h1><p>Página de Contato</p>"


@app.route("/sobre", methods=('GET',)) 
def sobre(): 
    return "<h1>Sobre</h1><p>Página sobre</p>" 



