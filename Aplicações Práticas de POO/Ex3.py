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
                print(f'Aluno {aluno.nome} removido da turma de {self.disciplina}')
                return
        print(f'Aluno com a matricula {matricula} não foi encontrado no sistema')
        
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
            return f'Registro de presença para a turma de {turma.disciplina} na data {data}:\n' + '\n'.join(str(aluno) for aluno in turma.alunos if aluno.matricula in self.registros[turma][data])
        return f'Nenhum registro de presença encontrado para a turma de {turma.disciplina} na data {data}'
    