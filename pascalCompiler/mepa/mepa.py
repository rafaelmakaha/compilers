s = -1
M = []
i = 0
t = []

def INPP():
    global s
    global M
    s = -1

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
    if M[s] == 0:
        i = p
    else:
        i = i + 1
    M.pop()
    s = s - 1
    
def DSVS(p):
    global s
    global M
    i = p

def NADA():
    global s
    global M
    pass

def AMEM(n):
    global s
    global M 
    s = s + int(n)
    M = [i for i in range(int(n))]

def DMEM(n):
    global s
    global M
    s = s - int(n)
    if n > s:
        print('RunTime error. Stack underflow')
        exit()
    for i in range(int(n)):
        M.pop()
    
def CRVL(e,n):
    global s
    global M
    s = s + 1
    M.append(M[n])
    M[s] = M[n]
    
def ARMZ(e,n):
    global s
    global M
    M[n] = M[s]
    s = s - 1

def IMPR():
    global s
    global M
    print(M[s])
    s = s - 1

def LEIT(entrada):
    global s
    global M
    s = s + 1
    M[s] = entrada

def PARA():
    exit()

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
    }

if __name__ == "__main__":
    import sys
   
    with open(sys.argv[1],'r') as f:

        for j,line in enumerate(f):
            t = list(map(str,line.replace('\n','').replace(',','').split()))
            if len(t) == 1:
                func[t[0]]()
            elif len(t) == 2:
                func[t[0]](t[1])
            else:
                func[t[0]](t[1],t[2])
            print(t)
            print(M)
            print()
    print()