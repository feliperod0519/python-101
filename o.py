from sys import stdin
def periferia(mtrx,t,i):
    n= len(mtrx)
    for j in range(t[0],n-i):
        mtrx[t[0]][j] = i+1
        mtrx[n-1-i][j] = i+1
        mtrx[j][t[1]] = i+1
        mtrx[j][n-1-i] = i+1
    
def format(l):
    s = "["
    for i in l:
        s+=str(i)+","
    s = s[0:len(s)-1]
    s+="]"
    return s

def main():
    print("Hello ¯\_(ツ)_/¯ OMatrix")
    n= int(stdin.readline())
    mtrx = [[0 for x in range(0,int(n))] for y in range(int(n))] 
    m=n//2
    if (n%2!=0):
        mtrx[n//2][n//2] = n//2+1
    for i in range(0,m):
        periferia(mtrx,tuple([i,i]),i)
    for i in range(0,n):
        print(format(mtrx[i]))

if __name__ == '__main__':
    main() 