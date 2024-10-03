from flask import Flask # Importa o flask

app = Flask(__name__) # Cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota

def index(): # Função responsável pela página
    return "<h1>Página inicial</h1><p>Eu sou fulano</p>" # HTML retornado


@app.route("/galeria", methods=('GET',)) 
def galeria(): 
    return "<h1>Galeria</h1><p>Página da Galeria</p>" 


@app.route("/contato", methods=('GET',)) 
def contato():
    return "<h1>Contato </h1><p>Página de Contato</p>"


@app.route("/sobre", methods=('GET',)) 
def sobre(): 
    return "<h1>Sobre</h1><p>Página sobre</p>" 



