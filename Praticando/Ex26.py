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
            return'Tente um numero maior...'
        elif palpite > self.numero_secreto:
            return 'Tente um numero menor...'
        else:
            return 'Parabêns você acertou o numero secreto!'
    
    def reiniciar_jogo(self):
        self.numero_secreto=random.randint(self.min_num,self.max_num)
        self.tentativas=0
    
class Jogador:
    def __init__(self,nome):
        self.nome=nome
        self.pontuacao=0
    
    def incrementar_pontuacao(self):
        self.pontuacao+=1
        
    

nome=input('Digite o seu nome:')
jogador=Jogador(nome)
jogo=Jogo(1,100)
print('-'*40)
print(f'Certo {nome} agora tente adivinhar o numero...')
while True:
    try:
        palpite=int(input('-->'))
        resultado=jogo.tentar_adivinhar(palpite)
        print(resultado)
        
        if palpite == jogo.numero_secreto:
            print('-'*40)
            jogador.incrementar_pontuacao()
            print(f'Pontuação do jogador: {jogador.pontuacao}')
            print('-'*40)
            resp=input('Quer Continuar o jogo?[S/N]:').lower()
            if resp == 's':
                print('Iniciando o jogo...')
                jogo.reiniciar_jogo()
            else:
                print(f'Obrigado por jogar!\nEncerrando o programa....')
                break
    except ValueError :
        print('Digite um numero valido!')
        