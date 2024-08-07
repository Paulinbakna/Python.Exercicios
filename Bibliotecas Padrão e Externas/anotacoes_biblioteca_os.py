#importando a biblioteca
import os

#============================================================================

#o environ mostra as variaveis de ambiente, no caso os dados do sistema
sistema=os.environ
print(sistema)

#============================================================================

#mostrar uma variavel de ambientes especifica
print(sistema['USERNAME'])

#============================================================================

#mostra o caminho(local), mostra o caminho para a  pasta onde esta o codigo
print(os.getcwd())

#============================================================================

#mudar de caminho(local)
novo_caminho=r'C:\Users\Paulin\Downloads\TESTE'
os.chdir(novo_caminho)                                                                                          
print(os.getcwd())

#============================================================================

#Cria uma pasta no local especificado pelo chdir
os.mkdir('TESTE') 

#============================================================================

#lista tudo oq esta no caminho especificado
print(os.listdir())

#============================================================================

#Cria varias pastas nrcessitando so do local que elas serao armazenadas
caminho=r'C:\Users\Paulin\Downloads\TESTE\Testando\Testando2\Testando3'
os.makedirs(caminho)
print(os.listdir())

#============================================================================

#exclui pastas porem somente se elas estiverem vazias
os.rmdir(r'C:\Users\Paulin\Downloads\TESTE\Testando')

#============================================================================

#Abri arquivos passando o diretorio e o nome do arquivo que deseja abrir
os.startfile(r'C:\Users\Paulin\Downloads\TESTE\arquivo.txt')

#============================================================================

#Renomeia o nome de um arquivo
os.chdir(r'C:\Users\Paulin\Downloads\TESTE')
os.rename('arquivo.txt','apenas_um_teste.txt')

#============================================================================

#Remove um arquivo
os.remove('apenas_um_teste.txt')

#============================================================================

#mostra o caminho, diretorio(pastas) e arquivos 
for caminho,diretorio,arquivos in os.walk(os.getcwd()):
    print(caminho)
    print(diretorio)
    print(arquivos)
    
#============================================================================

#mostra o nome da pasta que voce esta
print(os.path.basename(os.getcwd()))

#============================================================================

#mostra o caminho que e sempre comum de aparecer 
caminho1=r'C:\Users\Paulin\Downloads\TESTE'
caminho2=r'C:\Users\Paulin\Downloads'
os.path.commonpath([caminho1,caminho2])

#============================================================================

#motra o caminho que e sempre comum de aparecer mais o prefixo 
print(os.path.commonprefix([caminho1,caminho2]))

#============================================================================

#mostra o caminho da penultima pasta 
print(os.path.dirname(caminho1))

#============================================================================

#Cria um caminho personalizado
drive='C:'
usuario='Paulin'
pasta_base='Downloads'
caminho_personalizado=os.path.join(drive,r'\Users',usuario,pasta_base)

#============================================================================

#A função os.path.join junta os caminhos de diretórios e arquivos, criando um caminho completo.Verifique o exercicio 50 para melhor entendimento