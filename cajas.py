from sys import stdin

def mover(l,i):
    if (i+1!=len(l)):
        if l[i+1] == 0 and l[i]==1:
           l[i+1]=1
           l[i]=0 
           return True
    return False

def matriz(m,n):
    matriz = []
    for i in range(m):
        linea = input().split(" ")
        matriz.append(linea)
    for i in range(m):
        for j in range(n):
            matriz[i][j] = int(matriz[i][j])
    return matriz

def format(l):
    s=""
    for i in l:
        s+=str(i) + " "
    return s.rstrip()

def gcdlike(p,q):
    print(f"p:{p} q:{q}")
    if q==0: return p==1
    return gcdlike(q,p%q)

# gdclike(p,q)=gdclike(q,p-q)

def main():
    gcdlike(270,112)
    print("_________________")
    gcdlike(112,270-112)
    print("Hello ¯\_(ツ)_/¯ Cajas")    
    m_n=(stdin.readline()).split(" ")
    fil_col=list(map(int,m_n))
    mat=matriz(fil_col[0],fil_col[1])
    for l in mat:
        i=0
        while i<len(l)-1:
            if l[i]==2:
                i=len(l)
            else:
                v = mover(l,i)
                if v:
                    i=0
                else:
                    i+=1
        print(format(l))    

if __name__ == '__main__':
    main() 