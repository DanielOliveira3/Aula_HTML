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

@app.route("/numero", methods=['GET'])
def numero():

    numero = request.args.get('n', type=int)

    if numero is None:
        return "<h1>Página Número</h1><p>Por favor, forneça um número como parâmetro 'n'.</p>"
    
    if numero % 2 == 0:
        return f"<h1>Número: {numero}</h1><p>O número é par.</p>"
    
    else:
        return f"<h1>Número: {numero}</h1><p>O número é ímpar.</p>"
    
    
@app.route("/nome_sobrenome/<string:nome>/<string:sobrenome>", methods=['GET'])
def nome_sobrenome(nome, sobrenome):

    if not nome or not sobrenome:
        return "<h1>Erro</h1><p>Nome e sobrenome são necessários.</p>"

    return f"<h1>Resultado</h1><p>{sobrenome}, {nome}</p>"



@app.route("/area/<float:largura>/<float:comprimento>", methods=('GET',)) 
def area(largura: float, comprimento: float): 

    return f"""<h1>Página Área</h1>
    <ul><li><p>Comprimento= {comprimento}</p></li><li><p>Largura= {largura}</p></li><li><p>Área= {comprimento*largura}</p></li></ul>
    """ 

@app.route("/potencia/<float:n1>/<float:elevado>", methods=('GET',)) 
def potencial(n1: float, elevado: float): 

    return f"""<h1>Página Potencia</h1>
    <ul><li><p>Comprimento= {n1}</p></li><li><p>Largura= {elevado}</p></li><li><p>Área= {n1**elevado}</p></li></ul>
    """     
