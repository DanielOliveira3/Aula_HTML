def divisao_segura(numerador, denominador):
    try:
        # Tentando realizar a divisão
        resultado = numerador / denominador
    except ZeroDivisionError:
        # Tratando o erro caso o denominador seja zero
        return "Erro: Divisão por zero não é permitida."
    else:
        # Retornando o resultado caso a divisão seja realizada com sucesso
        return resultado

# Exemplo de uso da função
num1 = 10
num2 = 0

# Chama a função e exibe o resultado
print(divisao_segura(num1, num2))  # Adivinha que vai dar erro aqui!

num2 = 2
print(divisao_segura(num1, num2))  # Aqui a divisão deve ocorrer normalmente
