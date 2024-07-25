import sys

#mostra o diretorio onde esta sendo executado o codigo, e mostra no terminal o argumentos que foram digitados 

print(f"Diretorio onde esta localizado: {sys.argv[0]}")
print(f'Argumentos: {sys.argv[1:]}')

#======================================================

#Finaliza a execução de um programa, odendo fornecer ums mensagem de erro ou um status de como o codigo esta 

#Saida com sucesso
sys.exit(0)

#Saida com erro:
sys.exit(1)

#Saida com mensagem
sys.exit('Ocorreu algum erro!')

#======================================================

#Encontra caminhos de biblioteca que deseja importar ou um arquivo que esta localizado em outro diretorio

import sys
sys.path.append('/meu/diretorio/de/modulos')
import meu_modulo_personalizado

#======================================================

#Mostra a versão que o python esta 

print("Versão do Python:", sys.version)

#======================================================

#Mostra qual sistema operacional o Python esta sendo executado

print("Plataforma:", sys.platform)

#======================================================

#sys.stdin = Usado para ler dados da entrada padrão (geralmente o teclado).
Exemplo: input() #lê da sys.stdin.

#sys.stdout = Usado para imprimir dados na saida padrão (geralmente a tela)
Exemplo: print() #escreve na sys.stdout.
sys.stdout.write("Isto é uma saída padrão.\n")

#sys.stderr = Usado para imprimir mensagens de erri ba sauda oadrão de erro (geralmente a tela)

sys.stderr.write("Isto é uma mensagem de erro.\n")

#======================================================

#Retorna o tamanho em bytes de um objeto

my_list = [1, 2, 3]
print("Tamanho da lista em bytes:", sys.getsizeof(my_list))

#======================================================

#Verifica se uma biblioteca em python foi carregada

print("Módulos carregados:", sys.modules.keys())

#======================================================

#Mostra o maior numero inteiro que o python pode manipular

max_val = sys.maxsize
print(f"O maior valor inteiro suportado é: {max_val}")

#======================================================