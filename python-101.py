from importlib.resources import contents
from unittest import skip

def bubbleSort_1(a):
    for _ in range(len(a)): # [0,1....6]
        #print(_)
        for i in range(1,len(a)):  #[1..6]
            #print(f"{a[i]} {a[i-1]} ")
            if (a[i]<a[i-1]):
                temp=a[i]
                a[i]=a[i-1]
                a[i-1]=temp
                #print(a)

def bubbleSort_2(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if (a[i]<a[i-1]):
                a[i-1],a[i]=a[i],a[i-1]

def main():
    mystr = "abcdefghijklmnopqrstuvwz"
    #[p:l:s]
    print(mystr[2:])
    print(mystr[:3])
    print(mystr[::2])
    print(mystr[-1:])

    #Inmutabilidad
    name="Juan Andres"
    print(name[0])
    print(type(name))
    #name[0]='j'

    
    name = 'j' + name[1:]
    print(name)

    
    hello = "HELLO WORLD"
    print(hello.lower())
    print(hello.upper())
    print(hello.split(" "))

    print('This is a string {} {}'.format("Juan","Andres"))
    print("El {} {} {}".format("zorro","rojo", "salta"))
    print("El {c} {b} {a} {d}".format(a="zorro",b="rojo", c="salta",d="alto"))
    
    name = "Juan Andres"
    print(f"Hello, my name is {name}")
    
    #lists
    myList = []
    myList1 = list()
    myList = [1,2,3]
    myList = ["hello",1,2]
    print(myList[1:])
    anotherList = [5,6]
    print(myList + anotherList)
    
    newList = myList + anotherList
    x = newList.pop()#(myList + anotherList).pop()
    print(x)
    print(newList)
    
    L= myList + anotherList
    print(L.pop(0))
    
    new_List= ['a','e','i','o','u']
    new_List2 = [10,3,99,4,2]
    new_List.sort()
    new_List2.sort()
    print(new_List)
    print(new_List2)
    print(type(new_List))
    
    new_list3 = []
    new_list3.append(3)
    new_list3.append(4)
    new_list3.append(5)
    #del new_list3
    del new_list3[2:]
    print(new_list3)

    
    new_list3.clear()
    print(len(new_list3))
    print(new_list3)
    
    #dictionarios
    mydict = {'k1':'v1','k2':'v2'}
    print(mydict['k1'])
    d= {'k1':123,'k2':[0,1,2,3], 'k3':{'ik':100}}
    print(d['k2'][3])
    print(d['k3']['ik'])
    
    d['k1'] = 300
    print(d.keys())
    print(d.values())
    print(len(d))
 
    #tuples
    t= (1,2,3)
    t1 = tuple((1,2,3))
    l= [1,2,3]
    print(t)
    print(l)
    print(t[-1])

    print(t[0])
    print(len(t))
    print(t.count(2))
    print(t.index(3))
    
    #t[0]=99  #No funciona porque la tupla es inmutable

    print("sets")
    #sets
    myset = set()
    myset.add(1)
    myset.add(2)
    print(myset)

    myListSet = [1,1,1,1,2,2,2,3,3,3,3,3,3,3,4,5,6,6,7]
    myset = set(myListSet)
    print(myset)
    print(myset.pop())
    print(myset)

    print("--------------")
    #i/o
    f = open('ipsum.txt')
    s= f.read()
    print(s)
    print("--------------")
    f.seek(0)
    str = f.read()
    print(str)
    f.seek(0)
    print("--------------")
    lines = f.readlines()
    print(lines)
    print("--------------")

    #'\\n' #carry return ---verbatim
    with open('ipsum.txt') as my_bacon_file:
       contents = my_bacon_file.readlines()
    print(contents) 
    print("------------------------")


    #Comparaciones

    print('Bye'=='bye')
    print(2.0==2)
    print('x' in [1,2,3])
    print('1' in 'wert12u')

    #if-elif-else
    x=45
    if (x==21):
        pass
    elif (x==67):
        pass
    else:
        pass
   
    #loops
    myList=list(range(10,20))
    print(myList)
    
    j=0
    while (j<len(myList)):
        print(myList[j])
        j+=1

    for i in myList:
        print(i)
    
    myString = "Juan Andres"
    for letter in myString:
        print(letter)

    for _ in 'FelipeRod':
        print(_)

    t= tuple([1,2,3,4])
    for item in t:
        print(item)

    myNewTupleList = [(1,2),(3,4),(5,6),(7,8),(9,10)]
    for _ in myNewTupleList:
        print(_)
    
    for (a,b) in myNewTupleList:
        print(f"{a} {b}")
    
    d= {'k1':1,'k2':2,'k3':3}
    for i in d:
        print(i) #k1,k2,k3 porque la coleccion por defecto es keys
    
    for i in d.keys():
        print(i)
    
    for k,v in d.items():
        print(f"{k} {v}")

    for v in d.values():
        print(v)

    a= [1,4,3,9,0,99,77]
    print("----")
    print(a)
    bubbleSort_1(a)
    print(a)
    
    #Enumerate
    word="abcdefghijabc"
    for i in enumerate(word):
        print(i)
    print(enumerate(word))

    for i,v in enumerate(word):
        print("{} {}".format(i,v))
    
    print("........................")
    #Zip
    myL1= [1,2,3]
    myL2= ['a','b','c']

    for i in zip(myL1,myL2):
        print(i)
    
    myL1= [1,2,3]
    myL2= ['a','b','c']
    myL3= [':)','(:',';)']

    for i in zip(myL1,myL2,myL3):
        print(i)

    print('k1' in {'k3':3,'k1':'hola'})
    print('hola' in {'k3':3,'k1':'hola'})
    print('hola' in {'k3':3,'k1':'hola'}.values())
    
    myL = [1,2,3,4,5]
    myL2 = [78,2,3,0]
    
    print(max(myL2))
    print(min(myL))

    from random import shuffle
    shuffle(myL)
    print(myL)

    
    from random import randint
    print(randint(3,99))
    
    #List comprehension
    myString = "Hola soy Juan Andres"
    lst = list()
    for l in myString:
        lst.append(l.upper())

    myList = [l.upper() for l in myString] # [1,2,3,3] #list(range(0,5))
    print(myList)

    myList = [x**2 for x in range(0,10)]
    print(myList)
    
    myList = [x for x in range(0,10) if x%2==0]
    print(myList)

    celcius = [0,10,20,34.5,-30]
    # farenheit = 9/5 temp + 32
    myList = [(9/5)*t+32 for t in celcius]
    print(myList)

    myList = [x if x%2==0 else 'impar:' for x in range(0,11)]
    print(myList)

    myList = ['par' if x%2==0 else 'impar:' for x in range(0,11)]
    print(myList)

    myList=[]
    for x in [2,4,6]:
        for y in [100,200,300]:
            myList.append(x*y)
    print(myList)

    myList = [x*y for x in [2,4,6] for y in [100,200,300]]
    print(myList)

    #item-3
    print("Item-3")
    a= b'h\x65llo'
    print(list(a))
    print(a)
  
    print(repr([1,2,3])) #repr is more precise but it's used for debugging
    bytes_or_str = b'Juan Andres'
    if isinstance(bytes_or_str,bytes):
        print(bytes_or_str.decode('utf-8'))
    else:
        print(bytes_or_str)
     
    if isinstance(bytes_or_str,type("")):
        print(repr(bytes_or_str.encode('utf-8')))
    else:
        print(bytes_or_str)
    print(b'one' + b'two')
    #print(b'one'+'two') #error types are incompatible

    assert b'red'>b'blue', 'byte vs byte cannot be compared'
    #assert b'red'>'blue','byte vs str cannot be compared'
 
    #item-6
    #prefer multiple assignment unpacking over indexing

    d_snacks = {'papitas':140,'popcorn':80,'chitos':100}  
    items = tuple(d_snacks.items())
    print(items)
    print(items[0])
    
    nom,cal = items[0]
    print(f"{nom}:{cal}")
    for i,v in items:
        print(f"{i}:{v}")

    names = ['Juan Andres','Felipe','Carolina','Sandrita','Manchitas','Enri','Pedrito']
    print(names)
    bubbleSort_1(names)
    print(names)
    bubbleSort_2(names)
    print(names)
    

if __name__ == '__main__':
    main()

#int, float, string, bool
#list, dict, tup, set ---> collections
#i/o
#operadores de comparacion
#if/elif/else
#loop/while
#range/enumerate/zip
#package-1
#list comprehesion





