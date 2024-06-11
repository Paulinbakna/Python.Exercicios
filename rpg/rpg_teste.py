from time import sleep
import random
from colorama import Fore, Style, init

init()
#funções e status do personagem
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.ataque = 10
        self.moedas = 50
        self.nivel = 1
        self.alcance = 5
        self.magia = 5
        self.defesa = 5
        self.xp = 0
        self.xp_para_proximo_nivel = 100

    def esquivar(self):
        print(f'{Fore.GREEN}{self.nome} conseguiu se esquivar do ataque!{Style.RESET_ALL}')

    def ganhar_xp(self, xp):
        self.xp += xp
        print(f'{Fore.GREEN}{self.nome} ganhou {xp} XP! | XP Atual: {self.xp}{Style.RESET_ALL}')
        print()
        if self.xp >= self.xp_para_proximo_nivel:
            self.subir_de_nivel()

    def ganhar_moedas(self, moedas):
        self.moedas += moedas
        print(f'{Fore.YELLOW}{self.nome} ganhou {moedas} moedas!{Style.RESET_ALL} | Total de moedas atual:{Fore.YELLOW} {self.moedas}{Style.RESET_ALL}')

    def subir_de_nivel(self):
        self.xp -= self.xp_para_proximo_nivel
        self.xp_para_proximo_nivel *= 1.5
        self.nivel += 1
        self.ataque += 5
        print(f'{Fore.GREEN}{self.nome} subiu de nível!\nNível atual: {self.nivel}{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}XP necessário para o próximo nível: {self.xp_para_proximo_nivel}{Style.RESET_ALL}')

    def comprar_item(self, item):
        if self.moedas >= item.custo:
            self.moedas -= item.custo
            print(f'{Fore.GREEN}{self.nome} comprou {item.nome}!{Style.RESET_ALL}')
            item.usar(self)
        else:
            print(f'{Fore.RED}Moedas insuficientes para comprar {item.nome}{Style.RESET_ALL}')
    def explorar(self):
        sleep(2)
        print('-'*50)
        print(f'{Fore.LIGHTBLUE_EX}{self.nome} voltou a explorar o mundo....{Style.RESET_ALL}')
        sleep(3)


#classe guerreiro  e funções da classe
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.ataque += 5
        self.alcance -= 3
        self.defesa += 5

    def usar_espada(self):
        print(f'{self.nome} usou a espada!')

#classe mago e funções da classe
class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.ataque += 3
        self.alcance += 4
        self.defesa -= 2

    def usar_magia(self):
        print(f'{self.nome} usou a magia bola de fogo!')
        
#classe arqueiro e funções da classe
class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.ataque += 3
        self.alcance += 7
        self.defesa -= 2

    def usar_arco(self):
        print(f'{self.nome} usou o arco e jogou uma flecha!')
        
#classe  curandeiro e funções da classe
class Curandeiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.defesa += 5
        self.alcance -= 1
        self.ataque -= 1

    def curar(self, alvo: Personagem):
        alvo.vida += 10
        print(f'{self.nome} curou {alvo.nome}')
#classe para criar o inimgo e algumas funções como atacar, e sofrer dano do jogador
class Inimigo:
    def __init__(self, nome, ataque, xp, moedas):
        self.nome = nome
        self.vida = 100
        self.ataque = ataque
        self.xp = xp
        self.moedas = moedas

    def atacar(self, alvo: Personagem):
        chance_de_esquivar = random.randint(1, 100)
        if chance_de_esquivar <= 30:
            alvo.esquivar()
        else:
            dano = self.ataque - alvo.defesa
            dano = max(dano, 0)
            alvo.vida -= dano
            print(f'{Fore.RED}{self.nome} atacou {alvo.nome}!{Style.RESET_ALL}\n{Fore.RED}{alvo.nome} recebeu {dano} de dano de {self.nome}{Style.RESET_ALL} | {Fore.GREEN}Vida Atual: {alvo.vida}{Style.RESET_ALL}')
            

    def sofrer_dano(self, dano):
        self.vida -= dano
        print(f'{Fore.RED}{self.nome} sofreu {dano} de dano! | Vida Atual: {self.vida}{Style.RESET_ALL}')
        print()
        if self.vida <= 0:
            return True
        return False

#classe para criar um Boss no jogo e algumas funções como atacar e sofrer dano  do player
class Boss:
    def __init__(self, nome, ataque, xp, moedas):
        self.nome = nome
        self.vida = 1000
        self.ataque = ataque
        self.xp = xp
        self.moedas = moedas

    def atacar(self, alvo: Personagem):
        chance_de_esquivar = random.randint(1, 100)
        if chance_de_esquivar <= 20:
            alvo.esquivar()
        else:
            dano = self.ataque - alvo.defesa
            dano = max(dano, 0)
            alvo.vida -= dano
            print(f'{Fore.RED}{self.nome} acertou o {alvo.nome}!{Style.RESET_ALL}\n{Fore.RED}{alvo.nome} recebeu {dano} de dano de {self.nome}{Style.RESET_ALL}')
            print(f'{Fore.GREEN}Vida Atual: {alvo.vida}{Style.RESET_ALL}')

    def sofrer_dano(self, dano):
        self.vida -= dano
        print(f'{Fore.MAGENTA}{self.nome} {Style.RESET_ALL} sofreu {Fore.RED}{dano} {Style.RESET_ALL}de dano! |  Vida Atual: {self.vida}{Style.RESET_ALL}')
        if self.vida <= 0:
            return True
        return False

#classe para criar o item que sera armazenado na lojinha do jogo
class Item:
    def __init__(self, nome, custo, efeito):
        self.nome = nome
        self.custo = custo
        self.efeito = efeito

    def usar(self, personagem: Personagem):
        raise NotImplementedError('Use a subclasse específica do item')
    
#classe para criar a poção e funçoes de adicionar vida
class PocaoDeVida(Item):
    def __init__(self):
        super().__init__('Poção De Vida', 10, 'Restaura 20 pontos de vida')

    def usar(self, personagem: Personagem):
        personagem.vida += 20
        print(f'{Fore.GREEN}{personagem.nome} restaurou 20 pontos de vida!{Style.RESET_ALL}')

#classe para criar a espada e funções  de adicionar ataque ao player
class Nichirin(Item):
    def __init__(self):
        super().__init__('Nichirin', 20, '+25 ataque')

    def usar(self, personagem: Personagem):
        personagem.ataque += 25
        print(f'{Fore.GREEN}{personagem.nome} equipou Nichirin e aumentou seu ataque em 25 pontos!{Style.RESET_ALL}')

#classe para criar a espada mais forte e funções de adicionar ataque ao player
class KatanaWakizashi(Item):
    def __init__(self):
        super().__init__('Katana Wakizashi', 300, '+100 ataque')

    def usar(self, personagem: Personagem):
        personagem.ataque += 100
        print(f'{Fore.GREEN}{personagem.nome} equipou Katana Wakizashi e aumentou seu ataque em 100 pontos!{Style.RESET_ALL}')

#classe para criar o esscudo e funções de adicionar defesa ao player
class EscudoBasico(Item):
    def __init__(self):
        super().__init__('Escudo Básico', 20, '+15 Defesa')

    def usar(self, personagem: Personagem):
        personagem.defesa += 15
        print(f'{Fore.GREEN}{personagem.nome} equipou o Escudo Básico e aumentou sua defesa em 15 pontos!{Style.RESET_ALL}')

#classe para criar o escudo e funções de adicionar magia ao player
class AmuletoDeMagia(Item):
    def __init__(self):
        super().__init__('Amuleto De Magia', 20, '+15 magia')

    def usar(self, personagem: Personagem):
        personagem.magia += 15
        print(f'{Fore.GREEN}{personagem.nome} equipou o Amuleto De Magia e aumentou sua magia em 15 pontos!{Style.RESET_ALL}')

#classe para criar botas e funções de adicionar alcance ao player
class BotasDeAgilidade(Item):
    def __init__(self):
        super().__init__('Botas De Agilidade', 20, '+5 alcance')

    def usar(self, personagem: Personagem):
        personagem.alcance += 5
        print(f'{Fore.GREEN}{personagem.nome} equipou as Botas De Agilidade e aumentou seu alcance em 5 pontos!{Style.RESET_ALL}')

#classe para mostrar a lojinha ao player e os itens que foram criados
class Loja:
    def __init__(self):
        self.itens = [
            PocaoDeVida(),
            Nichirin(),
            KatanaWakizashi(),
            EscudoBasico(),
            AmuletoDeMagia(),
            BotasDeAgilidade()
        ]

    def mostrar_itens(self,personagem: Personagem):
        # Definindo larguras para alinhamento
        nome_width = 18
        custo_width = 10
        efeito_width = 20
        print('-'*50)
        loja_bem_vindo= f'{Fore.MAGENTA}Bem-vindo à loja!{Style.RESET_ALL}'
        centralizando_loja_bem_vindo=loja_bem_vindo.center(50)
        print(centralizando_loja_bem_vindo)
        print('-'*50)
        print(f'Você tem {Fore.YELLOW}{personagem.moedas} moedas.{Style.RESET_ALL}')
        print('-'*80)
        
        for i, item in enumerate(self.itens, 1):
            nome = item.nome.ljust(nome_width)
            custo = f'{Fore.YELLOW}{item.custo} moedas{Style.RESET_ALL}'.ljust(custo_width + len(Fore.YELLOW) + len(Style.RESET_ALL))
            efeito = f'{Fore.GREEN}{item.efeito}{Style.RESET_ALL}'.ljust(efeito_width + len(Fore.GREEN) + len(Style.RESET_ALL))
            print(f'{i}. {nome} - Custo: {custo} - Efeito: {efeito}')
        print('0. Sair da loja')
        print('-'*80)

            
    def comprar(self, personagem: Personagem, escolha: int):
        if escolha == 0:
            print(f'{Fore.CYAN}Você saiu da loja.{Style.RESET_ALL}')
        elif 1 <= escolha <= len(self.itens):
            item = self.itens[escolha - 1]
            personagem.comprar_item(item)
        else:
            print(f'{Fore.RED}Escolha inválida.{Style.RESET_ALL}')

#classe para facilitar ao criar um inimigo 
class Arena:
    def __init__(self, personagem):
        self.personagem = personagem

    def batalha(self, inimigo):
        print('-'*50)
        print(f'{Fore.CYAN}Você encontrou um {inimigo.nome}! O que deseja fazer?{Style.RESET_ALL}')
        while inimigo.vida > 0 and self.personagem.vida > 0:
            print('-'*50)
            print(f'{Fore.LIGHTGREEN_EX}    [A] Atacar     {Style.RESET_ALL}|{Fore.LIGHTRED_EX}     [B] Fugir {Style.RESET_ALL}')
            print('-'*50)
            acao = input(f'{Fore.LIGHTCYAN_EX}=>>{Style.RESET_ALL}').upper()
            print('-'*50)
            if acao == 'A':
                dano = self.personagem.ataque
                if inimigo.sofrer_dano(dano):
                    print('-'*50)
                    print(f'{Fore.GREEN}{inimigo.nome} foi derrotado!{Style.RESET_ALL}')
                    self.personagem.ganhar_xp(inimigo.xp)
                    self.personagem.ganhar_moedas(inimigo.moedas)
                    break
            elif acao == 'B':
                print(f'{Fore.CYAN}{self.personagem.nome} fugiu do {inimigo.nome}.{Style.RESET_ALL}')
                break

            if inimigo.vida > 0:
                if random.choice([True, False]):
                    inimigo.atacar(self.personagem)

        if self.personagem.vida <= 0:
            print(f'{Fore.RED}{self.personagem.nome} foi derrotado!{Style.RESET_ALL}')
            print('-- FIM DO JOGO --')

def loja_mundo():
    personagem.explorar()
    print('-'*50)
    print(f'{Fore.GREEN}Você encontrou uma lojinha!{Style.RESET_ALL}')
    print('-'*50)
    print(f'{Fore.LIGHTCYAN_EX}Entrando na loja.....{Style.RESET_ALL}')
    sleep(2)
    loja = Loja()
    while True:
        loja.mostrar_itens(personagem)
        escolha_item = int(input('Digite o número do item que deseja comprar: '))
        print('-'*50)
        if escolha_item == 0:
            print('Saindo da Loja.......')
            break
        loja.comprar(personagem, escolha_item)
        print('-'*50)
def bosses():
    bosses = [
    Boss('Ogro', 25, 300, 200),
    Boss('Malenia', 24, 500, 250),
    Boss('Hydra', 30, 600, 300),
    Boss('Ciclope', 30, 200, 150),

]
        
    mensagem= f'{Fore.RED}!!! BOSS !!!{Style.RESET_ALL}'
    centro= mensagem.center(50)
    print(centro)
    boss=random.choice(bosses)
    arena=Arena(personagem)
    arena.batalha(boss)
    sleep(2)
    

def inimigos():
    inimigos = [
    Inimigo('Goblin', 8, 20, 10),
    Inimigo('Troll', 12, 40, 20),
    Inimigo('Lobo', 15, 50, 25),
    Inimigo('Dragão', 30, 200, 70),
    Inimigo('Esqueleto', 20, 75, 35),
    Inimigo('Goblin atirador', 15, 50, 25),
    Inimigo('Batedor de Argila', 35, 250, 100)
]
    inimigo=random.choice(inimigos)
    sleep(2) 
    arena=Arena(personagem)
    arena.batalha(inimigo)
    
#pedido ao jogador para criar o seu persongem
while True:
    print(f'{Fore.BLUE}={Style.RESET_ALL}' * 80)
    texto_bem_vindo= f'{Fore.LIGHTBLUE_EX}-- Bem vindo ao PYTHON RPG -- {Style.RESET_ALL}'
    centralizando_texto=texto_bem_vindo.center(80)
    print(centralizando_texto)
    print(f'{Fore.BLUE}={Style.RESET_ALL}' * 80)
    sleep(1)
    nome = str(input('Para começar, crie um nome para o seu personagem: '))
    print('-'*80)
    print(f'Certo {nome}, agora escolha uma classe para seu personagem:')
    sleep(1)
    print('=' * 80)
    print(f'1. Guerreiro:  Buffs: {Fore.GREEN}+5 ataque, +5 defesa{Style.RESET_ALL}      | Debuffs: {Fore.RED}-3 alcance{Style.RESET_ALL}')
    print(f'2. Mago:       Buffs: {Fore.GREEN}+3 ataque, +4 alcance{Style.RESET_ALL}     | Debuffs: {Fore.RED}-2 defesa{Style.RESET_ALL}')
    print(f'3. Arqueiro:   Buffs: {Fore.GREEN}+3 ataque, +7 alcance{Style.RESET_ALL}     | Debuffs: {Fore.RED}-2 defesa{Style.RESET_ALL}')
    print(f'4. Curandeiro: Buffs: {Fore.GREEN}+5 defesa{Style.RESET_ALL}                 | Debuffs: {Fore.RED}-1 alcance, -1 ataque{Style.RESET_ALL}')
    print('=' * 80)
    escolha = int(input(f'Digite o número da classe escolhida\n{Fore.LIGHTCYAN_EX}=>>{Style.RESET_ALL}'))

    if escolha == 1:
        personagem = Guerreiro(nome)
    elif escolha == 2:
        personagem = Mago(nome)
    elif escolha == 3:
        personagem = Arqueiro(nome)
    elif escolha == 4:
        personagem = Curandeiro(nome)
    else:
        print(f'Não consegui identificar a classe selecionada!\nPor favor, digite novamente.')
        continue
    print('-'*80)    
    print(f'Parabéns, você criou um personagem com a classe: {personagem.__class__.__name__} e que se chama: {personagem.nome}')
    break
print('-'*50)
print(f'{Fore.LIGHTBLUE_EX}{personagem.nome} está explorando o mundo agora...{Style.RESET_ALL}')
print('-'*50)


while True:
    if personagem.vida > 0:
        ini=inimigos()
        loja=loja_mundo()
        boss=bosses()
        random.choice(ini,loja,boss)
        
    elif personagem.vida <=0:
        print('-'*50)
        centro_fim='{Fore.LIGHTMAGENTA_EX} -- FIM DO JOGO -- {Style.RESET_ALL}'
        fim=centro_fim.center(50)
        print(fim)
        break