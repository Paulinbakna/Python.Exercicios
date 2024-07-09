def verificar_senha(nova_senha):
    if len(nova_senha) > 6 :
        print(f'Senha {nova_senha} Válida')
    else:
        print(f'Senha {nova_senha} invalida!')
        