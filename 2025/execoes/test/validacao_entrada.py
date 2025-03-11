def pedir_numero():
    while True:
        try:
            # Solicita que o usuário insira um número
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            # Se o usuário digitar algo que não pode ser convertido para número, exibe uma mensagem de erro
            print("Erro: Por favor, digite um número válido.")

# Chama a função e exibe o número digitado
numero = pedir_numero()
print(f"O número digitado foi: {numero}")

