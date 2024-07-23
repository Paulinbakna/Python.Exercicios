#Exiba uma lista de todos os arquivos e pastas no diretório atual
import os

arquivos=os.listdir()
cont=0
for i in arquivos:
    cont+=1
    print(f'{cont} = {i}')
    