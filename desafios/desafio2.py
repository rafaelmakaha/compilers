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
        9 estados.
        O estado inicial fica em loop até chegar a letra 'm'.
        Os estados 1 a 8 esperam a entrada da palavra maratona.
        Caso não sejam lidas todas as letras da palavra esperada,
        retorna-se para o estado inicial.
        Caso seja lida a palavra 'maratona', o estado final 8
        fica em loop até o final da leitura da string de entrada.

        Sobre as entradas...
        1. Fazer as entradas dos estados com os chars que esperamos.
        2. Fazer as entradas dos estados com os 
            chars que não esperamos, mas chamar eles 
            de uma variável só, tipo '$'.

        Quando estivermos verifiando a string alvo...
        1. Verificar se o char atual é o esperado.
        2. Fazer uma das duas possibilidades já salvas no dicionário/matriz.

    O código feito em sala de aula foi adaptado para python.

    Entrada.
    9
    53 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z  
    0 m 1
    0 $ 0
    1 a 2
    1 $ 0
    2 r 3
    2 $ 0
    3 a 4
    3 $ 0
    4 t 5
    4 $ 0
    5 o 6
    5 $ 0
    6 n 7
    6 $ 0
    7 a 8
    7 $ 0
    8 $ 8
    8 $ 8
    0
    1 8
    Minha alegria eh fazer AFDs
'''

def main():
    #Leitura da quantidade de estados
    estados = int(input())

    #Leitura do alfabeto e da quantidade de simbolos
    alfabeto = [x for x in input().split(' ')]
    simbolos = int(alfabeto.pop(0))
    alfabeto.pop(-1)
    alfabeto[-1] = ' '

    #Leitura da tabela de transição
    tabtran = {}
    possibilidades = 2
    i = 0
    for i in range(estados):
        tabtran[i] = {}
        for j in range(possibilidades):
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
        # Verifica se o char atual é o esperado para
        # se avançar um estado
        if buf[bpos] in alfabeto:
            if buf[bpos] in tabtran[atual]:
                atual = tabtran[atual][buf[bpos]]
            else:
                atual = tabtran[atual]['$']
            bpos = bpos + 1
        else:
            atual = -1
        
    if atual != -1 and finais[atual] == 1:
        print('Aceito')
    else:
        print('Rejeito')


main()

