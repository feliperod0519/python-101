def genVal(l1,l2):
    s = 0
    for i in range(0,len(l1)):
        s+=l1[i]*l2[i]
    return s

def main():
    print("Hello ¯\_(ツ)_/¯")
    dimAInput = input("ingresa el dim matriz 1: ")
    dimA = dimAInput.split(',')
    n= int(dimA[0]) #2
    m= int(dimA[1]) #3
    mtrxA = [[0 for x in range(0,int(n))] for y in range(int(m))]
    i = 0
    while (i<n):
        fi = input(f"ingresa la fila {i} matriz 1 csv: ")
        l= fi.split(',')
        j=0
        while (j<len(l)):
            mtrxA[j][i] = int(l[j])
            j+=1
        i+=1
    dimBInput = input("ingresa el dim matriz 2: ")
    dimB = dimBInput.split(',')
    o= int(dimB[0]) #3
    p= int(dimB[1]) #5
    mtrxB = [[0 for x in range(0,int(o))] for y in range(int(p))]
    i = 0
    while (i<o):
        fi = input(f"ingresa la fila {i} matriz 2 csv: ")
        l= fi.split(',')
        j=0
        while (j<len(l)):
            mtrxB[j][i] = int(l[j])
            j+=1
        i+=1
    
    mtrxC = [[]]
    if m!=o:
        print("Imposible")
    else:
        mtrxC = [[0 for x in range(0,int(n))] for y in range(int(p))]  
        i=0
        while (i<n):
            l = list()
            j=0
            while(j<m):
                l.append(mtrxA[j][i])
                j+=1
            k=0
            while(k<p):
                x = genVal(l,mtrxB[k])
                mtrxC[k][i]=x
                k+=1
            i+=1
        print(mtrxC)
        for i in range(0,n):
            s=""
            for j in range(0,p):
                if (j!=p-1):
                    s+=str(mtrxC[j][i])+","
                else:
                    s+=str(mtrxC[j][i])
            print(s)




if __name__ == '__main__':
    main()