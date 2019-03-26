# Ciração de Autômato generico
# Pode receber qualquer maquina de estados


def main():
    # Leitura da quantidade de estados
    estados = int(input())

    # Leitura do Tamanho do alfabeto
    alfabeto[]
    alfa_count = int(input())

    # Leitura do alfabeto
    for _ in range(alfa_count):
        albabeto.append(input())

    # tabela de transição
    tab_trans[estados]['z'+1]

    # Leitura de cada situação possivel na tabela
    for i in range(estados * alfa_count):
        origem = int(input())
        trig = input()
        dest = int(input())
        tab_trans[origem][trig] = dest

    estado_inicial = int(input())

    finais_count = ""
    int finais[estados]

    for i in range(estados):
        finais[i]= -1

    for i in range(finais_count):
        t = int(input())
        finais[t] = 1

    # char buffer[1000]
    # scan(%s, buff)

    atual = incial
    bpos = 0

    while buffer[bpos] != '\0' && atual != -1 :
        atual = tab_trans[atual][buffer[bpos++]]


    if atual != -1 && finais[atual] == 1 :
        print("Aceito")
    else:
        print("Rejeito")

    return 0

main()
