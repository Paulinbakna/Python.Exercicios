#Copie o arquivo "arquivo.txt" para o diretório "diretorio_destino"
import os 
import shutil

arquivo_origem=r'C:\Users\Paulin\Downloads\diretorio_novo\arquivo.txt'
diretorio_destino=r'C:\Users\Paulin\Downloads\diretorio_novo\diretorio_destino'

os.makedirs(diretorio_destino,exist_ok=True)

arquivo_destino=os.path.join(diretorio_destino,os.path.basename(arquivo_origem))

try:
  shutil.copy(arquivo_origem,arquivo_destino)
  print("Arquivo copiado com sucesso!")
except Exception as e:
  print(f"Erro ao copiar o arquivo: {e}")

