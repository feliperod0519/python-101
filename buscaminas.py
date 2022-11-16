def subMatrix(mtrx,t):
    m = len(mtrx)
    n = len(mtrx[0])
    f,c = t[0],t[1]
    minN,maxN = 0,0
    minM,maxM = 0,0
    if f==0:
        minN = f
    else:
        minN = f-1
    if f==(n-1):
        maxN = f
    else:
        maxN = f+1 
    if c==0:
        minM = c
    else:
        minM = c-1
    if c==(m-1):
        maxM = c
    else:
        maxM = c+1
    subMtrx = []
    j=minM
    while (j<=maxM):
        col = []
        i=minN
        while (i<=maxN):
            if (j==c and i==f):
                col.append('X')
            else:
                col.append(mtrx[j][i])
            i+=1
        subMtrx.append(col)
        j+=1
    return subMtrx

def calcularValor(mtrx,t):
    f,c = t[0],t[1]
    if (mtrx[c][f]=='*'):
        return '*'
    else:
        subM = subMatrix(mtrx,t)
        m,n = len(subM),len(subM[0])
        star = 0
        for i in range(0,n):
            for j in range(0,m):
                if (subM[j][i]!='X' and subM[j][i]!='.'):
                    star+=1
                j+=1    
        i+=1
        return star

def main():
    print("Hello ¯\_(ツ)_/¯ BuscaMinas")
    dimNInput = input("ingresa el num de filas: ")
    dimMInput = input("ingresa el num de columnas : ")
    m= int(dimMInput)
    n= int(dimNInput)
    mtrxA = []
    for i in range(0,n):
        dimInput = input(f"ingresa la fila {i+1} sin caracter de separacion p.ej (**…): ")
        line = [i for i in dimInput]
        mtrxA.append(line)

    mtrxB = [['.' for x in range(0,n)] for y in range(m)]
    i=0
    while (i<n):
        j=0
        while(j<n):
            mtrxB[i][j]= mtrxA[j][i]
            j+=1
        i+=1
    m = len(mtrxB)
    n = len(mtrxB[0])
    for i in range(0,n):
        line = ""
        for j in range(0,m):
            line += str(calcularValor(mtrxB,tuple([i,j]))) + ","
        print(line[0:len(line)-1])

if __name__ == '__main__':
    main() 