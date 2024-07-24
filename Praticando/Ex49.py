#Crie a estrutura de diretórios "diretorio1/diretorio2/diretorio3"
import os 
os.chdir(r'C:\Users\Paulin\Downloads\diretorio_novo')
caminho=r'C:\Users\Paulin\Downloads\diretorio_novo\diretorio1\diretorio2\diretorio3'
os.makedirs(caminho)
print(f'Estrutura de diretorios criadas')
