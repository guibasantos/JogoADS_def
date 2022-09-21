# Guilherme Wilson Vieira dos Santos - Tecnólogo em Análise e Desenvolvimento de Sistemas

import random
#Tela Inicial
print('~' * 50)
print(f'{"~> ZOMBIE DICE <~":^50}')
print('~' * 50)

#Looping para regra de no mínimo dois jogadores
n_j = int(input('Digite o número de Jogadores: '))
while n_j < 2:
    print('São necessários no mínimo 2 jogadores!')
    n_j = int(input('Digite o número de Jogadores: '))

#Armazenamento dos nomes dos jogadores
lista_nomes = []
if n_j >= 2:
    for c in range(n_j):
        nome = str(input(f'Digite o nome do {c+1}º Jogador: '))
        lista_nomes.append(nome)

#Definição dos treze dados
#(1-6 Verde/7-10 Amarelo/ 11-13 Vermelho)
lista_dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lista_verde = ["C", "P", "C", "T", "P", "C"]
lista_amarelo = ["T", "P", "C", "T", "P", "C"]
lista_vermelho = ["T", "P", "T", "C", "P", "T"]

#Contadores
verde = 0
amarelo = 0
vermelho = 0
passo = 0
tiro = 0
cerebro = 0

#Turno do jogador
while True:
    for cont in range(0, n_j):
        print(f'É a vez do jogador {lista_nomes[cont]}')
        tiro = 0
        passo = 0
        cerebro = 0
        lista_dados_sorteados = []

        #Sorteio dos três dados e suas respectivas cores
        while True:
            lista_dados_sorteados = (random.sample(lista_dados, 3))
            for ns in lista_dados_sorteados:
                if ns <= 6:
                    verde += 1
                elif 7 <= ns <= 10:
                    amarelo += 1
                else:
                    vermelho += 1
                for n in lista_dados:
                    if n == ns:
                        lista_dados.remove(n)
            print(f'Você retirou {verde} dados VERDE')
            print(f'Você retirou {amarelo} dados AMARELO')
            print(f'Você retirou {vermelho} dados VERMELHOS')

            #Sorteio das faces de cada um dos dados
            for d in range(verde):
                face = random.randint(0, 5)
                if face == 0 or 2 or 5:
                    cerebro += 1
                elif face == 1 or 4:
                    passo += 1
                else:
                    tiro += 1
            for d in range(amarelo):
                face = random.randint(0, 5)
                if face == 2 or 5:
                    cerebro += 1
                elif face == 1 or 4:
                    passo += 1
                else:
                    tiro += 1
            for d in range(vermelho):
                face = random.randint(0, 5)
                if face == 3:
                    cerebro += 1
                elif face == 1 or 4:
                    passo += 1
                else:
                    tiro += 1
            print(f'{lista_nomes[cont]} você teve {cerebro} cerebros e {tiro} tiros')
            print(f'{lista_nomes[cont]} você avançou {cerebro - tiro} casas')

            #Condições de termino da rodada e do jogo
            if tiro == 3:
                print('Você perdeu a sua vez!')
                verde = 0
                amarelo = 0
                vermelho = 0
                lista_dados = lista_dados
                break
            elif tiro != 3:
                deci = str(input('Você deseja continuar jogando? [S/N] ')).upper().strip()[0]
                if deci in 'N':
                    print(f'{lista_nomes[cont]} o seu turno acabou!')
                    verde = 0
                    amarelo = 0
                    vermelho = 0
                    lista_dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                    break
                else:
                    verde = 0
                    amarelo = 0
                    vermelho = 0
        if cerebro == 13:
            print(f'Parabéns {lista_nomes[cont]} você venceu o jogo!')
            break