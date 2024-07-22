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
#os.mkdir('TESTE') (comentado pois toda vez que execuatar ira criar uma pasta)

#============================================================================

#lista tudo oq esta no caminho especificado
print(os.listdir())

#============================================================================

#Cria varias pastas nrcessitando so do local que elas serao armazenadas
#(Comentado para evitar a criação de varias pastas)
#caminho=r'C:\Users\Paulin\Downloads\TESTE\Testando\Testando2\Testando3'
#os.makedirs(caminho)
#print(os.listdir())

#============================================================================

#exclui pastas porem somente se elas estiverem vazias
#Comentado para evitar erros
#os.rmdir(r'C:\Users\Paulin\Downloads\TESTE\Testando')

#============================================================================

#Abri arquivos passando o diretorio e o nome do arquivo que deseja abrir
#Comentado para evitar erros
#os.startfile(r'C:\Users\Paulin\Downloads\TESTE\arquivo.txt')

#============================================================================

#Renomeia o nome de um arquivo
#Comentado para evitar erros
os.chdir(r'C:\Users\Paulin\Downloads\TESTE')                                                                                          
#os.rename('arquivo.txt','apenas_um_teste.txt')

#============================================================================

#Remove um arquivo
#Comentado para evitar erros
#os.remove('apenas_um_teste.txt')

#============================================================================

#mostra o caminho, diretorio(pastas) e arquivos 
for caminho,diretorio,arquivos in os.walk(os.getcwd()):
    print(caminho)
    print(diretorio)
    print(arquivos)
    