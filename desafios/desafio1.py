'''
    Aluno: Rafael Makaha Gomes Ferreira
    Matrícula: 160142369

    A sua tarefa é projetar um Autômato Finito 
    que aceita uma linguagem L com palavras 
    pertencentes ao alfabeto [A-Za-z\ ] tal que 
    cada palavra w não contenha letras maíusculas 
    após uma minúscula.


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
    possibilidades = 3
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
        # Verifica se o char atual é maiúsculo, minúsculo ou espaço
        if buf[bpos] in alfabeto:
            if buf[bpos].isupper():
                atual = tabtran[atual]['M']
            elif buf[bpos].islower():
                atual = tabtran[atual]['m']
            else:
                atual = tabtran[atual][' ']
            bpos = bpos + 1
        else:
            atual = -1
        
        
    if atual != -1 and finais[atual] == 1:
        print('Aceito')
    else:
        print('Rejeito')


main()

