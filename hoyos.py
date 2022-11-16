def subMatrix(mtrx,t,v):
    m = len(mtrx)
    n = len(mtrx[0])
    f,c = t[0],t[1]
    minN,maxN = 0,0
    minM,maxM = 0,0
    v.append(mtrx[c][f])
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

def calcularHoyo(mtrx,t,v):
    f,c = t[0],t[1]
    subM = subMatrix(mtrx,t,v)
    m,n = len(subM),len(subM[0]) # m:col n:fil
    for i in range(0,m):
        for j in range(0,n):
            if (subM[i][j]!='X'):
                if (subM[i][j]<v[0]):
                    return list()
    return t

def printMatrix(mtrx):
    n = len(mtrx[0])#f
    m = len(mtrx)#c
    for i in range(0,m):
        linea = ""
        for j in range(0,n):
            linea += str(mtrx[i][j]) + ","
        linea = linea[0:len(linea)-1]
        print(linea)

def matriz(m,n):
    matriz = []
    for i in range(m):
        linea = input().split(",")
        matriz.append(linea)
    for i in range(m):
        for j in range(n):
            matriz[i][j] = int(matriz[i][j])
    return matriz

def trans(mtrxA):
    m= len(mtrxA) #5
    n= len(mtrxA[0]) #4
    mtrxB = [[0 for x in range(0,m)] for y in range(n)]
    i=0
    while (i<n):
        j=0
        while(j<m):
            mtrxB[i][j] = mtrxA[j][i]
            j+=1
        i+=1
    return mtrxB

def main():
    print("Hello ¯\_(ツ)_/¯ Hoyos") 
    m_n=(input("Ingresa tamaño de la matriz: ")).split(",")
    fil_col=list(map(int,m_n))
    mat=matriz(fil_col[0],fil_col[1])  
    mtrx = trans(mat) #[[15,7,6,7,3,2],[12,8,3,8,6,4],[10,12,5,9,9,5],[9,11,7,10,12,6]]
    v=[-1]
    n = len(mtrx[0])#f
    m = len(mtrx)#c
    mtrxR = []
    for i in range(0,m):
        for j in range(0,n):
            v = []
            hoyo= calcularHoyo(mtrx,tuple([j,i]),v)
            if (len(hoyo)>0):
                mtrxR.append([v[0],hoyo[0],hoyo[1]])
    print("Resultado:")
    printMatrix(mtrxR[::-1])

if __name__ == '__main__':
    main() 


"""
def matriz(m,n):
    matriz = []
    for i in range(m):
        linea = input().split(",")
        matriz.append(linea)
    for i in range(m):
        for j in range(n):
            matriz[i][j] = int(matriz[i][j])
    return matriz
m_n=(input("Ingresa tamaño de la matriz: ")).split(",")
    fil_col=list(map(int,m_n))
    mat=matriz(fil_col[0],fil_col[1])

"""