
class Auto():
    def __init__(self,marca,min,max):
        self.marca = marca
        self.min = min
        self.max = max
    
    def VerificarPrecio(self,p):
        if p>self.min and p<self.max:
            return True
        return False

class BaseDeDatos():
    db = []

    def __init__(self):
        self.db = []
    
    def adicionarEntrada(self,auto:Auto):
        self.db.append(auto)

    def queryPrecio(self,p):
        resultadoStr=""
        q = list(filter(lambda i:i.VerificarPrecio(p),self.db))
        if len(q)==0:
            resultadoStr="UNDETERMINED"
        else:
            for i in range(0,len(q)):
                if i==(len(q)-1):
                    resultadoStr+=q[i].marca
                else:
                    resultadoStr+=q[i].marca + ","
        return resultadoStr

def main():
    print("Hello ¯\_(ツ)_/¯ ACM")
    print("1")
    inpt = input("ingresa el numero de carros: ")
    n = int(inpt)
    db = BaseDeDatos()
    for i in range(0,n):
        inpCar = input(f"ingresa el carro {(i+1)}: ")
        lCarro = inpCar.split(" ")
        carro = Auto(lCarro[0],int(lCarro[1]),int(lCarro[2]))
        db.adicionarEntrada(carro)
    inpt = input("ingresa el numero de queries: ")
    m = int(inpt)
    lines = []
    for i in range(0,m):
        inpCar = input(f"ingresa el valor query {(i+1)}: ")
        line= db.queryPrecio(int(inpCar))
        lines.append(line)
    for s in lines:
        print(s)
    

if __name__ == '__main__':
    main()