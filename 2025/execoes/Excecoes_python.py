
#1.Erro Simples
try:   
    print(minha_variavel)
except NameError as e:
    print(f"Ocorreu um erro: {e}. A variável 'minha_variavel' não foi definida.")



#2.Divisão Segura
def divisao_segura(numerador, denominador):
    try:
     
        resultado = numerador / denominador
    except ZeroDivisionError:

        return "Erro: Divisão por zero não é permitida."
    else:

        return resultado

num1 = 10
num2 = 0


print(divisao_segura(num1, num2)) 

num2 = 2
print(divisao_segura(num1, num2))  



#3.Validação de Entrada
def pedir_numero():
    while True:
        try:

            numero = float(input("Digite um número: "))
            return numero
        except ValueError:

            print("Erro: Por favor, digite um número válido.")


numero = pedir_numero()
print(f"O número digitado foi: {numero}")



#4.Erro Personalizado
class ErroIdadeInvalida(Exception):
    def __init__(self, mensagem):
        
        super().__init__(mensagem)

def validar_idade(idade):
    if idade < 0 or idade > 120:
       
        raise ErroIdadeInvalida("Idade inválida! A idade deve estar entre 0 e 120.")
    return f"A idade {idade} é válida."


try:
    idade = int(input("Digite a sua idade: "))
    
    resultado = validar_idade(idade)
    print(resultado)
except ErroIdadeInvalida as e:

    print(f"Erro: {e}")
except ValueError:

    print("Erro: Por favor, digite um número inteiro válido.")



