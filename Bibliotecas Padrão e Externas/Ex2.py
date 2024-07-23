#Ex2= Utilize a biblioteca `os` para listar todos os arquivos em um diretório especificado.

import os

caminho=r'F:'
os.chdir(caminho)
listar=os.listdir()
cont=-1
for i in listar:
    cont+=1
    print(f'{cont} = {i}')
