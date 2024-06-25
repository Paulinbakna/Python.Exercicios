import random
class Jogo:
    def __init__(self,min_num,max_num):
        self.min_num=min_num
        self.max_num=max_num
        self.numero_secreto=random.randint(min_num,max_num)
        self.tentativas=0
    
    def tentar_adivinhar(self,palpite):
        self.tentativas+=1
        if palpite < self.numero_secreto:
            print('Tente um numero maior')
        elif palpite > self.numero_secreto:
            print('Tente um numero menor')
        else:
            print('Parabêns! Você acertou o numero!')
    
    def reiniciar_jogo(self):
        self.numero_secreto=random.randint(self.min_num,self.max_num)
        self.tentativas=0
    
class Jogador:
    def __init__(self,nome):
        self.nome=nome
        self.pontuacao=0
    
    def incrementar_pontuacao(self):
        self.pontuacao+=1
        