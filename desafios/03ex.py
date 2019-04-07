'''
    Aluno: Rafael Makaha Gomes Ferreira
    Matrícula: 160142369

    Desafio 2.
    A sua tarefa é projetar um Autômato Finito 
    que aceita uma linguagem L com palavras pertencentes 
    ao alfabeto [A-Za-z\ ] tal que cada palavra w não 
    contenha letras maíusculas após uma minúscula.

    Solução:
        A solução consiste em um Autômato Finito contendo
        8 estados.
        O estado inicial fica em loop até chegar a letra Mm.
        Os estados 1 a 8 esperam a entrada da palavra maratona.
        Caso não sejam lidas todas as letras da palavra esperada,
        retorna-se para o estado inicial.
'''

def main():
    #Leitura da quantidade de estados
    estados = int(input())

    #Leitura do alfabeto e da quantidade de simbolos
    st = input()
    alfabeto = []
    i = 0
    while i < len(st):
        alfabeto.append(st[i])
        i = i + 2
    simbolos = int(alfabeto.pop(0))

    #Leitura da tabela de transição
    tabtran = {}
    i = 0
    for i in range(estados):
        tabtran[i] = {}
        for j in range(simbolos):
            #Leitura da posição atual, seu trigger 
            #e o destino na tabela de transição
            st = input()
            atual = int(st[0])
            trig = st[2]
            prox = int(st[4])
            tabtran[i][trig] = prox
    
    #Leitura do Estado Inicial
    inicial = int(input())

    #Leitura dos Estados Finais
    finais = [-1 for x in range(estados)]
    st = input().split(' ')
    st.pop(0)
    i = 0
    while i < len(st):
        finais[int(st[i])] = 1
        i = i + 1

    #Leitura e verificação da string a ser verificada
    atual = inicial
    buf = input()
    bpos = 0
    while atual != -1 and bpos < len(buf):
        atual = tabtran[atual][buf[bpos]]
        bpos = bpos + 1
    if atual != -1 and finais[atual] == 1:
        print('Aceito')
    else:
        print('Rejeito')


main()

