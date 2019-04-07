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
    alfabeto = [x for x in input().split(' ')]
    simbolos = alfabeto.pop(0)

    #Leitura da tabela de transição
    tabtran = {}
    for i in range(estados):
        for j in range(simbolos):
            #Leitura da posição atual, seu trigger e o destino na tabela de transição
            atual, trig, prox = input().split(' ')
            tabtran[i][trig] = int(prox)
    
    inicial = int(input())
    

main()

