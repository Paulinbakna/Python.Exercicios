from datetime import datetime

class Aluno:
    def __init__(self,nome,matricula):
        self.nome=nome
        self.matricula=matricula
    
    def __str__(self):
        return f'Nome do Aluno: {self.nome} | Numero da matricula: {self.matricula}'

class Turma:
    def __init__(self,disciplina):
        self.disciplina=disciplina
        self.alunos=[]
    
    def adicionar_alunos(self,aluno):
        print(f'Aluno {aluno.nome} adicionado a turma de {self.disciplina}')
        self.alunos.append(aluno)
        
    def remover(self,matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                print(f'Aluno {aluno.nome} foi removido da turma de {self.disciplina}')
                return
        print(f'Aluno: {matricula} não foi encontrado no sistema')
        
    def listar_alunos(self):
        return '\n'.join(str(aluno) for aluno in self.alunos)

class RegistroPresenca:
    def __init__(self):
        self.registros={}
    
    def registrar_presenca(self,turma,data=None):
        if data is None:
            data=datetime.now().strftime('%Y-%m-%d')
        if turma is not self.registros:
            self.registros[turma]={}
        self.registros[turma][data]=[aluno.matricula for aluno in turma.alunos]
        print(f'Presença registraeda para a turma de {turma.disciplina} na data {data}')
    
    def exibir_registro(self,turma,data):
        if turma in self.registros and data in self.registros[turma]:
            return f'Verificando Registros...\nRegistro de presença para a turma de {turma.disciplina} na data {data}:\n' + '\n'.join(str(aluno) for aluno in turma.alunos if aluno.matricula in self.registros[turma][data])
        return f'Nenhum registro de presença encontrado para a turma de {turma.disciplina} na data {data}'


print('-'*40)
men='Colegio Python'
men.center(40)
print(men)
print('-'*40)
alunos = [
        Aluno('João Silva'      , '123'),
        Aluno('Maria Oliveira'  , '124'),
        Aluno('Carlos Pereira'  , '125'),
        Aluno('Ana Grabiele'    , '126'),
        Aluno('Marcos Vinicios' , '127')
    ]

turma1=Turma('Matematica')
turma2=Turma('História')
turma3=Turma('Português')
turma4=Turma('Ingles')
turma5=Turma('Biologia')
registro=RegistroPresenca()
        
while True:
    while True:
        for i,aluno in enumerate(alunos,start=1):
            print(f'{i}.{aluno}')
        print('-'*40)
        
        escolha=input('Digite o numero do aluno:\n-->>')
        escolha_num=int(escolha)
        if  escolha_num < 0 or escolha_num>= len(alunos):
            print('Escolha invalida!')
            continue
        aluno_escolhido=alunos[escolha_num-1]
            
        print('-'*40)
        print('Certo o que deseja fazer agora?')
        print('-'*40)
        print('[ 1 ] Adicionar a uma turma')    
        print('[ 2 ] Remover de uma turma')    
        print('[ 3 ] Registrar presença')
        print('[ 4 ] Exibir Registro')
        print('[ 5 ] Sair')
        print('-'*40)
        n=input('-->>')
        if n == '1':
            print('-'*40)
            print(f'Para qual turma você deseja mandar o aluno: ')
            print('-'*40)
            print('[ 1 ] Matematica')
            print('[ 2 ] História')
            print('[ 3 ] Portugues')
            print('[ 4 ] Ingles')
            print('[ 5 ] Biologia')
            print('-'*40)
            resp=input('-->>')
            if resp == '1' :
                print('-'*40)
                turma1.adicionar_alunos(aluno_escolhido)
                print('-'*40)
            elif resp == '2' :
                print('-'*40)
                turma2.adicionar_alunos(aluno_escolhido)
                print('-'*40)
            elif resp == '3' :
                print('-'*40)
                turma3.adicionar_alunos(aluno_escolhido)
                print('-'*40)
            elif resp == '4' :
                print('-'*40)
                turma4.adicionar_alunos(aluno_escolhido)
                print('-'*40)
            elif resp == '5' :
                print('-'*40)
                turma5.adicionar_alunos(aluno_escolhido)
                print('-'*40)
            else:
                print(f'Opção invalida! Tente novamente')
        if n == '2':
            print('-'*40)
            print(f'De qual turma você deseja remover o aluno:')
            print('-'*40)
            print('[ 1 ] Matematica')
            print('[ 2 ] História')
            print('[ 3 ] Portugues')
            print('[ 4 ] Ingles')
            print('[ 5 ] Biologia')
            resp=input('-->>')
            
            if resp == '1' :
                print('-'*40)
                turma1.remover(aluno_escolhido.matricula)
                print('-'*40)
            
            elif resp == '2' :
                print('-'*40)
                turma2.remover(aluno_escolhido.matricula)
                print('-'*40)

            elif resp == '3' :
                print('-'*40)
                turma3.remover(aluno_escolhido.matricula)
                print('-'*40)

            elif resp == '4' :
                print('-'*40)
                turma4.remover(aluno_escolhido.matricula)
                print('-'*40)

            elif resp == '5' :
                print('-'*40)
                turma5.remover(aluno_escolhido.matricula)
                print('-'*40)
            else:
                print('-'*40)
                print(f'Opção invalida! Tente novamente')    
                print('-'*40)
        if n == '3':
            print('-'*40)
            print(f'Para qual turma você deseja registrar presença:')
            print('-'*40)
            print('[ 1 ] Matematica')
            print('[ 2 ] História')
            print('[ 3 ] Portugues')
            print('[ 4 ] Ingles')
            print('[ 5 ] Biologia')
            resp=input('-->>')
            
            if resp == '1' :
                print('-'*40)
                registro.registrar_presenca(turma1)
                print('-'*40)
            elif resp == '2' :
                print('-'*40)
                registro.registrar_presenca(turma2)
                print('-'*40)
            elif resp == '3' :
                print('-'*40)
                registro.registrar_presenca(turma3)
                print('-'*40)
            elif resp == '4' :
                registro.registrar_presenca(turma4)
                print('-'*40)
            elif resp == '5' :
                print('-'*40)
                registro.registrar_presenca(turma5)
                print('-'*40)
            else:
                print('-'*40)
                print(f'Opção invalida! Tente novamente')
                print('-'*40)
        if n == '4':
            print('-'*40)
            print(f'Para qual turma você deseja verificar o registro:')
            print('-'*40)
            print('[ 1 ] Matematica')
            print('[ 2 ] História')
            print('[ 3 ] Portugues')
            print('[ 4 ] Ingles')
            print('[ 5 ] Biologia')
            resp=input('-->>')
            data=input(f'Qual a data que você quer verificar o registro?(ano-mes-dia):\n-->>')
            
            if resp == '1' :
                print('-'*40)
                print(registro.exibir_registro(turma1,data))
                print('-'*40)
            elif resp == '2' :
                print('-'*40)
                print(registro.exibir_registro(turma2,data))
                print('-'*40)
            elif resp == '3' :
                print('-'*40)
                print(registro.exibir_registro(turma3,data))
                print('-'*40)
            elif resp == '4':
                print('-'*40)
                print(registro.exibir_registro(turma4,data))
                print('-'*40)
            elif resp == '5' :
                print('-'*40)
                print(registro.exibir_registro(turma5,data))
                print('-'*40)
            else:
                print('-'*40)
                print(f'Opção invalida! Tente novamente')
                print('-'*40)
        if n == '5':
            print('Saindo....')
            break
    print('Programa Encerrado!')
    break
