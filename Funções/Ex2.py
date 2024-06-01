def palindromo(pala):
    contrario= pala[::-1]
    if contrario == pala:
        print(f'A palavra {pala} ao contrario fica {contrario} então é um palindromo')
    else:
        print(f'A palavra {pala} ao contrario fica {contrario} então ela nao é um palindromo')

palavra=input('Digite uma palavra: ')
palindromo(palavra)
