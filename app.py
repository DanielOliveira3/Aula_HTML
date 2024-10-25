from flask import (Flask, render_template, request) # Importa o flask

app = Flask(__name__) # Cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota

def index(): # Função responsável pela página

    nome = request.args.get ('nome')

     # HTML retornado
    return f"""<h1>Página inicial</h1><p>Olá {nome}, que nome bonito!</p>
        <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """ 


@app.route("/galeria", methods=('GET',)) 
def galeria(): 
    return """<h1>Galeria</h1><p>Página da Galeria</p>
        <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>""" 


@app.route("/contato", methods=('GET',)) 
def contato():
    return """<h1>Contato </h1><p>Página de Contato</p>
        <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>"""


@app.route("/sobre", methods=('GET',)) 
def sobre(): 
    return """<h1>Sobre</h1><p>Página sobre</p>
        <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>"""

@app.route("/numero", methods=['GET'])
def numero():

    numero = request.args.get('n', type=int)

    if numero is None:
        return """<h1>Página Número</h1><p>Por favor, forneça um número como parâmetro 'n'.</p>
            <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>"""
    
    if numero % 2 == 0:
        return f"""<h1>Número: {numero}</h1><p>O número é par.</p>
            <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>"""
    
    else:
        return f"""<h1>Número: {numero}</h1><p>O número é ímpar.</p>
            <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>"""
    
    
@app.route("/nome_sobrenome", methods=['GET'])
def nome_sobrenome():

    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')

    if not nome or not sobrenome:
        return """<h1>Erro</h1><p>Nome e sobrenome são necessários.</p>
            <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>"""

    return f"""<h1>Resultado</h1><p>{sobrenome}, {nome}</p>
        <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>"""



@app.route("/area/<float:largura>/<float:comprimento>", methods=('GET',)) 
def area(largura: float, comprimento: float): 

    return f"""<h1>Página Área</h1>
    <ul><li><p>Comprimento= {comprimento}</p></li><li><p>Largura= {largura}</p></li><li><p>Área= {comprimento*largura}</p></li></ul>
        <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """ 

@app.route("/potencia/<float:n1>/<float:elevado>", methods=('GET',)) 
def potencial(n1: float, elevado: float): 

    return f"""<h1>Página Potencia</h1>
    <ul><li><p>Número= {n1}</p></li><li><p>Elevado por= {elevado}</p></li><li><p>Potencia= {n1**elevado}</p></li></ul>
        <ul><h3>MENU</h3>
        <li><a href="/">Index</a></li>
        <li><a href="/contato">Contato</a></li>
        <li><a href="/sobre">Sobre</a></li>
        <li><a href="/tabuada">Tabuada</a></li>
        <li><a href="/galeria">Galeria</a></li>
        <li><a href="/area/10.0/5.0">Área</a></li>
        <li><a href="/numero">Número</a></li>
        <li><a href="/nome_sobrenome">Nome e Sobrenome</a></li>
        <li><a href="/potencia/10.0/2.0">Potencia</a></li>
        <li><a href="/juros">Juros</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """     

@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada(numero = None):
   
  if 'numero' in request.args: 
    numero = request.args.get('numero')
    numero = int(request.args.get('numero'))
         
  return render_template('tabuada.html', numero=numero)

@app.route("/juros")
@app.route("/juros/<numero>", methods=("GET", ))
def juros(juros = None , capital= None , tempo= None , deposito= None):
   
  if 'juros'and 'capital' and 'tempo' and 'deposito' in request.args: 
    
    juros = int(request.args.get('juros'))
    capital = int(request.args.get('juros'))
    tempo = int(request.args.get('juros'))
    deposito = int(request.args.get('juros'))
    
         
  return render_template('juros.html', juros=juros , capital=capital , tempo=tempo , deposito=deposito)

@app.route("/login", methods=("GET",))
def login(email=None, senha=None):
  
  if "email" and "senha" in request.args:
    email = request.args.get("email")
    senha = request.args.get("senha")

  return render_template("login.html", email=email, senha=senha)

@app.route("/imc", methods=("GET",))
def imc(peso = None, altura= None):
  if "peso" and "altura" in request.args:
    peso =float(request.args.get('peso')) 
    altura=float(request.args.get('altura'))
  return render_template("imc.html", peso=peso, altura=altura)