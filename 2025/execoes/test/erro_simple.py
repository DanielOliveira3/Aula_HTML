try:
    # Tentando acessar uma variável não definida
    print(minha_variavel)
except NameError as e:
    # Exibe uma mensagem personalizada quando a variável não está definida
    print(f"Ocorreu um erro: {e}. A variável 'minha_variavel' não foi definida.")
