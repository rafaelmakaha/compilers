def foo(atual, buf, bpos, tabtran, finais, alfabeto):
    if bpos == len(buf) and finais[atual] == 1:
        return True
    elif bpos == len(buf) or len(tabtran[atual][buf[bpos]]) == 0 or not(buf[bpos] in alfabeto):
        return False
    else:
        for i in range(len(tabtran[atual][buf[bpos]])):
            if foo(tabtran[atual][buf[bpos]][i], buf, bpos+1, tabtran, finais, alfabeto):
                return True
     

def main():
    #Leitura da quantidade de estados
    estados = int(input())

    #Leitura do alfabeto e da quantidade de simbolos
    alfabeto = [x for x in input().split(' ')]
    simbolos = int(alfabeto.pop(0))

    #Leitura da tabela de transição
    tabtran = {}
    # possibilidades = estados * simbolos
    i = 0
    for i in range(estados):
        tabtran[i] = {}
        for j in range(simbolos):
            #Leitura da posição atual, seu trigger
            #e o destino na tabela de transição
            st = input().split(' ')
            atual = st[0]
            trig = st[1]
            if not int(st[2]):
                prox = []
            else:
                prox = list(map(int,st[3:]))

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

    if foo(atual, buf, bpos, tabtran, finais, alfabeto):
        print('Aceito')
    else:
        print('Rejeito')


main()
