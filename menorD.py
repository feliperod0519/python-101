from math import sqrt
import sys

def distancia(p1,p2):
    x=p1[0]-p2[0]
    y=p1[1]-p2[1]
    return sqrt(x**2+y**2)

def main():
    print("Hello ¯\_(ツ)_/¯ Ejercicio-1")
    x= float(input("ingresa el eje x a evaluar (ej:2.0): "))
    y= float(input("ingresa el eje y a evaluar (ej:3.5): "))
    x_values = input("ingresa los valores del eje x separados por coma (ej: 3.1,2.8,-3.5,6.0,-1.0): ")
    x_values = "3.1,2.8,-3.5,6.0,-1.0"
    y_values = input("ingresa los valores del eje y separados por coma (ej: 4.5,-1.0,-5.2,5.0,1.0): ")
    y_values = "4.5,-1.0,-5.2,5.0,1.0"
    x_list = x_values.split(",")
    y_list = y_values.split(",")
    d = sys.maxsize
    px = sys.maxsize
    py = sys.maxsize
    if (len(x_list)==len(y_list)):
        j = 0
        for i in x_list:
            di = distancia((x,y),(float(i),float(y_list[j])))
            if (di < d):
                d= di
                px= i
                py= y_list[j]
            j+=1
    print(f"La distancia menor es {d:.2f}")
    print(f"Punto: ({px},{py})")


if __name__ == '__main__':
    main()