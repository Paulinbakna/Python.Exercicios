def ler_numeros_arquivo(caminho):
    numeros=[]
    try:
        with open (caminho,'r',encoding='utf-8') as arquivo:
            linhas=arquivo.readlines()
            if not linhas:
                raise ValueError ('O arquivo está vazio')
            for linha in linhas:
                try:
                    numero=float(linha.strip())
                    numeros.append(numero)
                except ValueError:
                    return f'-->> ERROR! {linha.strip()} Não é um numero valido! <<--'
    except FileNotFoundError:
        return f'-->> ERROR! Arquivo: "{caminho}" Não encontrado! <<--'
    except IOError:
        return f'-->> Não foi possivel ler o arquivo: "{caminho}" <<--'
    except ValueError as e:
        return f'Error! {e}'
    else:
        print('Numeros lidos do arquivo:')
        for numero in numeros:
            print(numero)
    finally:
        print('-->> Função de Leitura de arquivo chamada! <<--')

caminho=r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Tratamento de Erros\Ex2_Numeros.txt'
numeros_lidos=ler_numeros_arquivo(caminho)

print(numeros_lidos)
