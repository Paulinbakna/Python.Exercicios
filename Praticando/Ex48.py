#Troque o diretório de trabalho para "diretorio_novo"
import os
novo_caminho=r'C:\Users\Paulin\Downloads'
os.chdir(novo_caminho)
os.rename('TESTE','diretorio_novo')
print('Diretorio Alterado')

