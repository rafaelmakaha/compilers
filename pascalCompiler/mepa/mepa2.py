# -*- coding: utf-8 -*-

s = -1
k = 0
M = []
D = {}
comandos = []
listaRotulos = {}
cmd = []
j = 0
m = 0

def INPP():
    global s
    global M
    global D
    s = -1
    D['0'] = 0

def CRCT(k):
    global s
    global M
    s = s + 1
    M.append(int(k))

def SOMA():
    global s
    global M
    M[s-1] = M[s-1] + M[s]
    M.pop()
    s = s - 1

def MULT():
    global s
    global M
    M[s-1] = M[s-1] * M[s]
    M.pop()
    s = s - 1

def SUBT():
    global s
    global M
    M[s-1] = M[s-1] - M[s]
    M.pop()
    s = s - 1

def DIVI():
    global s
    global M
    if M[s] != 0:
        M[s-1] = M[s-1] / M[s]
    M.pop()
    s = s - 1

def INVR():
    global s
    global M
    M[s] = -M[s]

def NEGA():
    global s
    global M
    M[s] = 1 - M[s]

def CONJ():
    global s
    global M
    if M[s-1] == 1 and M[s] == 1:
        M[s-1] = 1
    else:
        M[s-1] = 0
    M.pop()
    s = s - 1

def DISJ():
    global s
    global M
    if M[s-1] == 1 or M[s] == 1:
        M[s-1] = 1
    else:
        M[s-1] = 0
    M.pop()
    s = s - 1

def CMME():
    global s
    global M
    if M[s-1] < M[s]:
        M[s-1] = 1
    else:
        M[s-1] = 0
    M.pop()
    s = s - 1

def CMMA():
    global s
    global M
    if M[s-1] > M[s]:
        M[s-1] = 1
    else:
        M[s-1] = 0
    M.pop()
    s = s - 1

def CMIG():
    global s
    global M
    if M[s-1] == M[s]:
        M[s-1] = 1
    else:
        M[s-1] = 0
    M.pop()
    s = s - 1

def CMDG():
    global s
    global M
    if M[s-1] != M[s]:
        M[s-1] = 1
    else:
        M[s-1] = 0
    M.pop()
    s = s - 1

def CMAG():
    global s
    global M
    if M[s-1] >= M[s]:
        M[s-1] = 1
    else:
        M[s-1] = 0
    M.pop()
    s = s - 1

def CMEG():
    global s
    global M
    if M[s-1] <=  M[s]:
        M[s-1] = 1
    else:
        M[s-1] = 0
    M.pop()
    s = s - 1

def DSVF(p):
    global s
    global M
    if not(p in listaRotulos.keys()):
        print('Linha '+str(j+1)+': RunTime error rotulo ' + str(p) + ' invalido')
        exit()
    
    if M[s] == 0:
        M.pop()
        s = s - 1
        return listaRotulos[p]
    else:
        M.pop()
        s = s - 1
        return j
    
def DSVS(p):
    global s
    global M
    global j
    if p in listaRotulos:
        return listaRotulos[p]
    else:
        print('Linha '+str(j+1)+': RunTime error rotulo ' + str(p) + ' invalido')
        exit()

def NADA():
    global s
    global M
    pass

def AMEM(n):
    global s
    global M 
    s = s + int(n)
    for k in range(int(n)):
        M.append(k)
    # M = [i for i in range(int(n))]

def DMEM(n):
    global s
    global M
    global j
    s = s - int(n)
    if s < -1:
        print('Linha '+str(j+1)+': RunTime error. Stack underflow')
        exit()
    for i in range(int(n)):
        M.pop()
    
def CRVL(m,n):
    global s
    global M
    if int(m) > 0:
        M.append(M[D[str(m)] + int(n)-1])
    else:
        M.append(M[D[str(m)] + int(n)])
    s = s + 1
    # M[s] = M[int(n)]
    
def ARMZ(m,n):
    global s
    global M
    if int(m) > 0:
        M[D[str(m)] + int(n)-1] = M[s]
    else:
        M[D[str(m)] + int(n)] = M[s]
    M.pop()
    s = s - 1

def IMPR():
    global s
    global M
    print(M[s])
    M.pop()
    s = s - 1

def LEIT():
    global s
    global M
    s = s + 1
    M.append(int(input()))

def PARA():
    exit()

def ARMI(m,n):
    global M
    global s
    global D
    M[M[D[str(m)]+int(n)]] = M[s]
    M.pop()
    s = s - 1

def CHPR(p,m):
    global M
    global s
    global D
    M.append(j+1)
    M.append(int(m))
    # D[str(m)] = s
    s += 2
    if p in listaRotulos.keys():
        return listaRotulos[p]
    else:
        print('Linha '+str(j+1)+': RunTime error rotulo ' + str(p) + ' invalido')
        exit()
    
def CREN(m,n):
    global s
    global M
    global D
    s = s + 1
    M.append(int(D[str(m)]) + int(n))

def ENPR(k):
    global s
    global M
    global D
    s = s + 1
    D[str(k)] = s + 1
    M.append(D[str(int(k)-1)])
    

def RTPR(k,n):
    global s
    global M
    D[str(k)] = M[s]
    aux = M[s-2]
    for _ in range(int(n+3)):
        M.pop()
    s = s - (int(n)+3)
    return aux # i = M[s-1]

func = {
        'INPP': INPP,
        'CRCT': CRCT,
        'SOMA': SOMA,
        'MULT': MULT,
        'SUBT': SUBT,
        'DIVI': DIVI,
        'INVR': INVR,
        'NEGA': NEGA,
        'CONJ': CONJ,
        'DISJ': DISJ,
        'CMME': CMME,
        'CMMA': CMMA,
        'CMIG': CMIG,
        'CMDG': CMDG,
        'CMAG': CMAG,
        'CMEG': CMEG,
        'DSVF': DSVF,
        'DSVS': DSVS,
        'NADA': NADA,
        'AMEM': AMEM,
        'DMEM': DMEM,
        'CRVL': CRVL,
        'ARMZ': ARMZ,
        'IMPR': IMPR,
        'LEIT': LEIT,
        'PARA': PARA,
        'ARMI': ARMI,
        'CHPR': CHPR,
        'CREN': CREN,
        'ENPR': ENPR,
        'RTPR': RTPR,
    }

if __name__ == "__main__":
    import sys
    
    with open(sys.argv[1],'r') as f:
        # Mapeamento de todos os comandos e rotulos
        for index,line in enumerate(f):
            # Formata a linha com comandos
            cmd = list(map(str,line.replace('\n','').replace(',','').split()))
            # Caso seja um rótulo, adiciona na lista de rotulos
            if ':' in cmd[0]:
                listaRotulos[cmd[0].replace(':','')] = index
        
            cmd[0] = cmd[0].replace(':','')
            # Adiciona na lista de comandos
            comandos.append(cmd)

        # print(comandos)
        while j < len(comandos):
            print('comando: ' , comandos[j])
            print('mem: ' , M)
            print('rot: ' , listaRotulos)
            print('D: ', D)
            print('j: ', j)
            print('s: ', s)
            print()
            
            # Se for um rotulo, executar seu comando
            if comandos[j][0] in listaRotulos.keys():
                if len(comandos[j]) == 2:
                    func[comandos[j][1]]()
                elif len(comandos[j]) == 3:
                    func[comandos[j][1]](comandos[j][2])
                j += 1
                continue

            # Verifica a quantidade de parâmetros no comando a ser executado
            if len(comandos[j]) == 1:
                func[comandos[j][0]]()
            elif len(comandos[j]) == 2:
                # Caso seja um desvio, altera o fluxo do loop
                if comandos[j][0] == 'DSVF' or comandos[j][0] == 'DSVS':
                    j = func[comandos[j][0]](comandos[j][1])
                    j += 1
                    continue
                else:
                    func[comandos[j][0]](comandos[j][1])

            else:
                if comandos[j][0] == 'CHPR' or comandos[j][0] == 'RTPR':
                    j = func[comandos[j][0]](comandos[j][1],int(comandos[j][2]))
                    # j += 1
                    continue
                else:
                    func[comandos[j][0]](comandos[j][1],comandos[j][2])
            
            # incremento do loop
            j += 1
