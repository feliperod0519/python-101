
def genList(mtrx,z):
    n = len(mtrx[0])
    l = []
    for i in range(0,n):
        l.append(mtrx[i][z])
    return l

def numVals(l,v):
    return len(list(filter(lambda i:i==v,l)))

def main():
    print("Hello ¯\_(ツ)_/¯")
    dim = input("ingresa el dim matriz : ")
    n = int(dim)
    vals = input(f"ingresa los {n*n} valores (T/F) separados por espacio: ")
    mtrx = [[False for x in range(0,int(n))] for y in range(int(n))]
    arr = vals.upper().split(" ")
    l= [True if s=="T" else False for s in arr]
    if n==1:
        print("Hadamard")
    elif len(l)!= n*n or n%2!=0:
        print("Imposible")
    else:
        y = n/2
        j=0
        while (j<int(len(l)/n)):
            k=0
            while(k<int(len(l)/n)):
                z = int(len(l)/n)
                mtrx[j][k] = l[(z*j)+k]
                k+=1                                
            j+=1
        i=0
        hadamard = True
        while (i<n-1 and hadamard==True):
            lst = genList(mtrx,i)
            lst1 = genList(mtrx,i+1)
            t,f = numVals(lst,True),numVals(lst,False)
            t1,f1 = numVals(lst1,True),numVals(lst1,False)
            #print(f"t:{t} f:{f} t1:{t1} f1:{f1}")
            max = int(n/2)
            if (abs(t-t1) == max and abs(f-f1) <= max) :
                hadamard = True
            elif (abs(t-t1) == 0 and abs(f-f1) <= 0) :
                hadamard = True
            else:
                hadamard = False
            i+=1
        if (hadamard):
            print("Hadamard")
        else:
            print("No Hadamard")

if __name__ == '__main__':
    main()