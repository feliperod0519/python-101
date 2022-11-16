def main():
    print("Hello ¯\_(ツ)_/¯")
    dim = input("ingresa el dim matriz : ")
    n = int(dim)
    mtrxA = [[0 for x in range(0,int(n))] for y in range(int(n))]
    i = 0
    while (i<n):
        fi = input(f"ingresa la fila {i} matriz csv: ")
        l= fi.split(',')
        j=0
        while (j<len(l)):
            mtrxA[j][i] = int(l[j])
            j+=1
        i+=1
    mtrxB = [[0 for x in range(0,int(n))] for y in range(int(n))]
    i=0
    while (i<n):
        j=0
        while(j<n):
            mtrxA[j][i],mtrxB[i][j]= mtrxB[i][j],mtrxA[j][i]
            j+=1
        i+=1
    for i in range(0,n):
        s=""
        for j in range(0,n):
            if (j!=n-1):
                s+=str(mtrxB[j][i])+","
            else:
                s+=str(mtrxB[j][i])
        print(s)


if __name__ == '__main__':
    main()

