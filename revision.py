
def main():
    print("Hello ¯\_(ツ)_/¯")
    n= 5 #float(input("ingresa el num filas: "))
    m= 4 #float(input("ingresa el num col: "))
    mtrx = [[0 for x in range(0,int(n))] for y in range(int(m))]  
    mtrx[0][0] = ' '
    mtrx[0][1] = 'A'
    mtrx[0][2] = ' '
    mtrx[0][3] = 'T'
    mtrx[0][4] = 'A'  
    mtrx[1][0] = 'U'
    mtrx[1][1] = 'O'
    mtrx[1][2] = 'Q'
    mtrx[1][3] = ' '
    mtrx[1][4] = 'R'
    mtrx[2][0] = 'C'
    mtrx[2][1] = 'E'
    mtrx[2][2] = 'L'
    mtrx[2][3] = 'A'
    mtrx[2][4] = 'L'
    mtrx[3][0] = 'O'
    mtrx[3][1] = 'G'
    mtrx[3][2] = 'E'
    mtrx[3][3] = '.'
    mtrx[3][4] = 'L'

    f = open('mensaje.txt')
    lines = f.readlines()
    print(lines)
    col = 0
    for l in lines:
        vals = l.split(',')
        for i in range(0,len(vals)):
            mtrx[col][i] = vals[i][0]
        col+=1
    
    print("---------")
    mt = [[c[0] for c in l.split(',')] for l in lines] 
    print(mt)
    print("-----------")

    filas = [2,4,0,2,0,1,3,0,4,4,2,1,2,0,3,1,4,1,3,3]
    columnas = [3,2,0,1,1,2,1,2,0,3,2,0,0,3,0,1,1,3,2,3]
    print(mtrx)
    print(filas)
    print(columnas)

    mensaje = []
    for i in range(0,len(columnas)):
        mensaje.append(mtrx[columnas[i]][filas[i]])
    print(mensaje)


if __name__ == '__main__':
    main()