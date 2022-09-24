# Guilherme Wilson Vieira dos Santos - Tecnólogo em Análise e Desenvolvimento de Sistemas
import random

lista_cerebros = []
cerebro_total = 0
ganhou = 0


def jogadores():
    tiro = 0
    passo = 0
    cerebro = 0
    cont_verde = 0
    cont_amarelo = 0
    cont_vermelho = 0
    lista_dados_sorteados = []
    tcerebros = 0
    ttiros = 0
    return [tiro, passo, cerebro, cont_verde, cont_amarelo, cont_vermelho, lista_dados_sorteados, tcerebros, ttiros]


def todos_dados():
    lista_todos_dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    return lista_todos_dados


def tipo_dados():
    verde = 0
    amarelo = 0
    vermelho = 0
    contadores[3] = 0
    contadores[4] = 0
    contadores[5] = 0
    for fs in sorteados:
        if fs <= 6:
            verde += 1
            contadores[3] += 1
        elif 7 <= fs <= 10:
            amarelo += 1
            contadores[4] += 1
        else:
            vermelho += 1
            contadores[5] += 1
    return [verde, amarelo, vermelho, contadores[3], contadores[4], contadores[5]]


def tipo_face():
    cerebro = 0
    passo = 0
    tiro = 0
    verde_passo = 0
    amarelo_passo = 0
    vermelho_passo = 0
    for d in range(cores[0]):
        face = random.randint(0, 5)
        if face == 0 or face == 2 or face == 5:
            cerebro += 1
        elif face == 1 or face == 4:
            passo += 1
            verde_passo += 1
        else:
            tiro += 1
    for d in range(cores[1]):
        face = random.randint(0, 5)
        if face == 2 or face == 5:
            cerebro += 1
        elif face == 1 or face == 4:
            passo += 1
            amarelo_passo += 1
        else:
            tiro += 1
    for d in range(cores[2]):
        face = random.randint(0, 5)
        if face == 3:
            cerebro += 1
        elif face == 1 or face == 4:
            passo += 1
            vermelho_passo += 1
        else:
            tiro += 1
    contadores[7] += cerebro
    contadores[8] += tiro
    return [cerebro, passo, tiro, contadores[7], contadores[8], verde_passo, amarelo_passo, vermelho_passo]


def retorno_passo():
    retorno_verde = 0
    retorno_amarelo = 0
    retorno_vermelho = 0
    if acao[1] != 0:
        print(f'Os {acao[1]} dados de PASSO voltaram ao copo!')
        for k in range(acao[1]):
            if acao[5] != 0:
                for t in range(acao[5]):
                    for v in sorteados:
                        if v == 1 or v == 2 or v == 3 or v == 4 or v == 5 or v == 6:
                            sorteados.remove(v)
                            dados.append(v)
                            retorno_verde += 1
            if acao[6] != 0:
                for t in range(acao[6]):
                    for v in sorteados:
                        if v == 7 or v == 8 or v == 9 or v == 10:
                            sorteados.remove(v)
                            dados.append(v)
                            retorno_amarelo += 1
            if acao[7] != 0:
                for t in range(acao[7]):
                    for v in sorteados:
                        if v == 11 or v == 12 or v == 13:
                            sorteados.remove(v)
                            dados.append(v)
                            retorno_vermelho += 1
    return [retorno_verde, retorno_amarelo, retorno_vermelho]


def condicoes():
    roda = 0
    if lista_cerebros[cont] >= 13:
        print(f'PARABÉNS {lista_nomes[cont]} VOCÊ VENCEU O JOGO!!!')
        roda = 3
    elif len(dados) <= 2:
        print('Seus dados acabaram!')
        roda = 1
    elif acao[4] >= 3:
        print('Você perdeu a sua vez!')
        roda += 1
    elif acao[4] != 3:
        d = str(input('Você deseja continuar jogando? [S/N] ')).upper().strip()[0]
        while d not in 'SsNn':
            print('Digite somente S ou N!!!')
            d = str(input('Você deseja continuar jogando? [S/N] ')).upper().strip()[0]
        if d in 'N':
            print('O seu turno acabou!')
            roda = 1
        else:
            roda = 2
    return [roda]


print('~*~' * 10)
print(f'{"~> ZOMBIE DICE <~":^30}')
print('~*~' * 10)

while True:
    try:
        n_j = int(input('Digite o número de Jogadores: '))
        if n_j < 2:
            print('O número mínimo de Jogadores é 2!')
        else:
            break
    except ValueError:
        print('Por favor, insira somente números!')

lista_nomes = []
for c in range(n_j):
    nome = str(input(f'Digite o nome do {c+1}º Jogador: '))
    lista_nomes.append(nome)

for z in range(0, n_j):
    lista_cerebros.append(0)

while True:
    for cont in range(0, n_j):
        print(f'\nÉ a vez do jogador {lista_nomes[cont]}')
        contadores = jogadores()
        dados = todos_dados()
        cerebro_total = lista_cerebros[cont]
        verde_copo = 6
        amarelo_copo = 4
        vermelho_copo = 3
        while True:
            sorteados = (random.sample(dados, 3))
            for n in sorteados:
                if n in sorteados:
                    dados.remove(n)
            cores = tipo_dados()
            print(f'Você tirou {cores[3]} dados VERDES!')
            print(f'Você tirou {cores[4]} dados AMARELOS!')
            print(f'Você tirou {cores[5]} dados VERMELHOS!')
            acao = tipo_face()
            cerebro_total += acao[0]
            del lista_cerebros[cont]
            lista_cerebros.insert(cont, cerebro_total)
            print(f'Você tirou {acao[0]} cérebros!')
            print(f'Você tirou {acao[1]} passos!')
            print(f'Você tirou {acao[2]} tiros!')
            if acao[3] != 0:
                print(f'Você avançou {acao[0]} casas!')
            else:
                print(f'Você não avançou casas nesta rodada!')
            print(f'{lista_nomes[cont]} você já avançou {lista_cerebros[cont]} casas!')
            print(f'{lista_nomes[cont]} você está com {acao[4]} tiros!!')
            retorno = retorno_passo()
            verde_copo = verde_copo - cores[3] + retorno[0]
            amarelo_copo = amarelo_copo - cores[4] + retorno[1]
            vermelho_copo = vermelho_copo - cores[5] + retorno[2]
            print(f'Sobraram {verde_copo + amarelo_copo + vermelho_copo} dados: ')
            print(f'    -> {verde_copo} dados VERDES '
                  f'\n    -> {amarelo_copo} dados AMARELOS '
                  f'\n    -> {vermelho_copo} dados VERMELHOS')
            cond = condicoes()
            if cond[0] == 1:
                break
            elif cond[0] == 2:
                continue
            elif cond[0] == 3:
                ganhou = 100
                break
        if ganhou == 100:
            break
    if ganhou == 100:
        break
