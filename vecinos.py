def convMatrix(mtrx):
    n = len(mtrx[0])
    for i in range(0,n):
        for j in range(0,n):
            mtrx[j][i] = int(mtrx[j][i])

def magicSquare(mtrx):
    n = len(mtrx[0])
    horizontal = []
    for i in range(0,n):
        sum=0
        for j in range(0,n):
            sum += mtrx[j][i]
        horizontal.append(sum)
    vertical = []
    for i in range(0,n):
        sum = 0
        for j in range(0,n):
            sum += mtrx[i][j]
        vertical.append(sum)
    print(horizontal)
    print(vertical)
    diagonal1=[]
    sumDiag1 = 0
    for i in range(0,n):
        sumDiag1 += mtrx[i][i]
    print(sumDiag1)
    sumDiag2 = 0
    for i in range(n-1,-1,-1):
        sumDiag2+=mtrx[i][n-1-i]
    print(sumDiag2)
    if sumDiag1==sumDiag2:
        lH = list(filter(lambda i:i==sumDiag1,horizontal))
        print(lH)
        lV = list(filter(lambda i:i==sumDiag1,vertical))
        print(lV)
        if (len(lH)==len(lV) and len(lH)==n):
            return True
        else:
            return False
    else:
        return False

def subVecinos(mtrx,p):
    x,y = p[0],p[1]
    izq,der,arriba,abajo,nw,ne,sw,se = 0,0,0,0,0,0,0,0
    if y>=1:
        izq = mtrx[y-1][x]
    if y<len(mtrx[0])-1:
        der = mtrx[y+1][x]
    if x>=1:
        arriba = mtrx[y][x-1]
    if x<len(mtrx[0])-1:
        abajo = mtrx[y][x+1]
    if x>=1 and y>=1:
        nw = mtrx[y-1][x-1]
    if x>=1 and y<len(mtrx[0])-1:
        ne = mtrx[y+1][x-1]
    if x<len(mtrx[0])-1 and y>=1:
        sw = mtrx[y-1][x+1]
    if x<len(mtrx[0])-1 and y<len(mtrx[0])-1:
        se = mtrx[y+1][x+1]
    return izq+der+arriba+abajo+nw+ne+sw+se

def llenadoIncompleto(mtrx,m,f,c):
    for i in range(c,m):
        mtrx[i][f]=i+1    

def llenadoCompleto(mtrx,m,f):
    for i in range(0,m):
        mtrx[i][f]=i+1

def imprimirMatrix(mtrx,m): #m es el numero de columnas
    for i in range(0,len(mtrx[0])):
        s=""
        for j in range(0,m):
            if j==m-1:
                s+=str(mtrx[j][i])
            else:
                s+=str(mtrx[j][i]) + ","
        print(s)

def main():
    print("Hello ¯\_(ツ)_/¯")
    n=2
    m=3

    mtrx = [[0 for x in range(0,int(n))] for y in range(int(m))]
    print(mtrx)
    v = 3
    t = (1,0)
    for i in range(t[0],len(mtrx[0])):
        if i==t[0]:
            llenadoIncompleto(mtrx,m,t[0],t[1])
        else:
            llenadoCompleto(mtrx,m,t[0])
    print(mtrx)

    #llenadoIncompleto(mtrx,m,1,0)
    #print(mtrx)
    #llenadoCompleto(mtrx,m,0)
    #print(mtrx)

    m= [[2,9,4],[7,5,3],[6,1,8]]
    imprimirMatrix(m,3)

    esMagicSquare = magicSquare(m)
    print(esMagicSquare)

    dimInput = input("ingresa el dim matriz y num de posiciones en csv: ")
    dim = dimInput.split(',')
    n= int(dim[0]) #4
    p= int(dim[1]) #3
    mtrx = [[0 for x in range(0,int(n))] for y in range(int(n))]
    i = 0
    while (i<n):
        fi = input(f"ingresa la fila {i+1} matriz csv: ")
        l= fi.split(',')
        j=0
        while (j<len(l)):
            mtrx[j][i] = int(l[j])
            j+=1
        i+=1
    print(mtrx)
    l=[]
    for i in range(0,p):
        dimPosInput = input(f"ingresa la posicion {i+1} en csv: ")
        dim = dimPosInput.split(',')
        l.append((int(dim[0]),int(dim[1])))
    s = 0
    for i in l:
        s+=subVecinos(mtrx,i)
    print(s)

if __name__ == '__main__':
    main()