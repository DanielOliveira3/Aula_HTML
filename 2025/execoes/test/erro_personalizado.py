# Definindo a classe de exceção personalizada
class ErroIdadeInvalida(Exception):
    def __init__(self, mensagem):
        # Inicializa a exceção com uma mensagem
        super().__init__(mensagem)

def validar_idade(idade):
    if idade < 0 or idade > 120:
        # Lança a exceção personalizada se a idade for inválida
        raise ErroIdadeInvalida("Idade inválida! A idade deve estar entre 0 e 120.")
    return f"A idade {idade} é válida."

# Solicita ao usuário a idade
try:
    idade = int(input("Digite a sua idade: "))
    # Tenta validar a idade
    resultado = validar_idade(idade)
    print(resultado)
except ErroIdadeInvalida as e:
    # Captura e exibe a mensagem de erro personalizada
    print(f"Erro: {e}")
except ValueError:
    # Captura erros caso o usuário digite algo que não seja um número inteiro
    print("Erro: Por favor, digite um número inteiro válido.")
