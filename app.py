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


@app.route("/area", methods=('GET',)) 
def area(): 

    Comprimento = float (request.args.get('c'))
    Largura = float (request.args.get('l'))
    

    return f"""<h1>Página Área</h1>
    <ul><li><p>Comprimento= {Comprimento}</p></li><li><p>Largura= {Largura}</p></li><li><p>Área= {Comprimento*Largura}</p></li></ul>
    """ 

@app.route("/numero", methods=['GET'])
def numero():

    numero = request.args.get('n', type=int)

    if numero is None:
        return "<h1>Página Número</h1><p>Por favor, forneça um número como parâmetro 'n'.</p>"
    
    if numero % 2 == 0:
        return f"<h1>Número: {numero}</h1><p>O número é par.</p>"
    
    else:
        return f"<h1>Número: {numero}</h1><p>O número é ímpar.</p>"
    
    
@app.route("/nome_sobrenome", methods=['GET'])
def nome_sobrenome():

    nome = request.args.get('nome')

    sobrenome = request.args.get('sobrenome')

    if not nome or not sobrenome:
        return "<h1>Erro</h1><p>Nome e sobrenome são necessários.</p>"

    return f"<h1>Resultado</h1><p>{sobrenome}, {nome}</p>"
