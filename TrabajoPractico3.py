#import de librerias
import random
#menu
def menu():
    for opcion in range(11):
        if opcion == 0:
            print(f"Si quiere terminar el programa ingrese el numero {opcion}")
        else:
            print(f"Si quiere realizar el ejercicio {opcion} ingrese el numero {opcion}")
#Funciones a reutilizar
def Pedir_numero() :
    numero = input("Ingrese un número: ")
    return numero
def IngresoDeNumeros(cantidad_numeros):
    Numeros=[]
    for i in range(cantidad_numeros):
        numero=Pedir_numero()
        Numeros.append(int(numero))
    return Numeros
def CalcularElNumeroMayor(numeros):
    numero_mayor=max(numeros)
    return numero_mayor
def mostrar_numero_maximo(numero_mayor):
    print(f"El numero mayor de tus numeros ingresados es : {numero_mayor}")
def carga_de_vectores(n,m):
    a=[]
    b=[]
    for i in range(n):
        a.append(random.randint(1,10))
    for i in range(m):
        b.append(random.randint(1,10))
    return a , b
def calcular_suma_del_vector(a,b):
    suma_a=sum(a)
    suma_b=sum(b)
    return suma_a , suma_b
def sumar_vectores(a,b):
    vectores=[a+b]
    return vectores
def pedir_horaciones():
    palabras=input("Ingrese una oracion: ").lower().split()
    return palabras
def contar_vocales(palabras):
    cantidad_vocales=0
    vocales="aeiou"
    for palabra in palabras:
        for letra in palabra:
            if letra in vocales:
                cantidad_vocales+=1
    return cantidad_vocales
def contar_consonantes(palabras):
    cantidad_consonantes=0
    consonantes="bcdfghjklmnpqrstvwxyz"
    for palabra in palabras:
        for letra in palabra:
            if letra in consonantes:
                cantidad_consonantes+=1
    return cantidad_consonantes
def min_menu():
    print("Ingrese el numero 1 si quiere sacar una potencia de un numero")
    print("Ingrese el numero 2 si quiere contar la cantidad de digitos de un numero")
    print("Ingrese el numero 3 si quiere saber si un numero es capicua")
    print("Ingrese cualquier otro caracter para salir")
def Pedir_potencia():
    k=int(input("Ingrese el valor de la potencia: "))
    return k
def calcular_potencia(numero,k):
    numero_potenciado=numero ** k
    print(f"El resultado de {numero} elevado a la potencia {k} es: {numero_potenciado}")
def contar_digitos(numero):
    print(f"El numero {numero} tiene {len(numero)} digitos")
def es_capicua(numero):
    if numero == numero[::-1]:
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} no es capicúa.")
def min_menu2():
    print("Ingrese el numero 1 si quiere sumar matrices")
    print("Ingrese el numero 2 si quiere multiplicar matrices")
    print("Ingrese cualquier otro caracter para salir")
def pedir_dimensiones():
    m=int(input("Ingrese la cantidad de filas: "))
    n=int(input("Ingrese la cantidad de columnas: "))
    return m,n
def cargar_matriz(m,n):
    matriz=[]
    for i in range(m):
        fila=[]
        for j in range(n):
            fila.append(random.randint(1,10))
        matriz.append(fila)
    return matriz
def sumar_matrices(matrizA, matrizB):
    matrizC =[]
    for i in range(len(matrizA)):
        fila=[]
        for j in range(len(matrizA[0])):
            fila.append(matrizA[i][j] + matrizB[i][j])
        matrizC.append(fila)
    return matrizC
def producto_matrices(matrizA, matrizB):
    matrizC= []
    for i in range ( len(matrizA)):
        fila=[]
        for j in range (len(matrizA[0])):
            fila.append(matrizA[i][j] * matrizB[i][j])
        matrizC.append(fila)
    return matrizC
def mostrar_matriz(matriz,nombre):
    print(f"La matriz {nombre} es:")
    for fila in matriz:
        print(fila)
#Ejercicios
def punto1():
    Numeros=IngresoDeNumeros(3)
    numero_mayor=CalcularElNumeroMayor(Numeros)
    mostrar_numero_maximo(numero_mayor)
def punto2():
    Numeros=IngresoDeNumeros(10)
    numero_mayor=CalcularElNumeroMayor(Numeros)
    mostrar_numero_maximo(numero_mayor)
def punto3():
    n , m = IngresoDeNumeros(2)
    a,b = carga_de_vectores(n,m)
    suma_a , suma_b=calcular_suma_del_vector(a,b)
    if suma_a == suma_b: 
        vectores= sumar_vectores(a,b)
        print(f"Los vectores son iguales aqui tenes la conbinacion de ambos: {vectores}")
    else : 
        print(f"La suma de los vectores: {a} y {b} , no son iguales. ")
def punto4():
    palabras=pedir_horaciones()
    cantidad_vocales=contar_vocales(palabras)
    cantidad_consonantes=contar_consonantes(palabras)
    print(f"La cantidad de vocales es: {cantidad_vocales} y las consonantes son: {cantidad_consonantes}")
def punto5():
    while True:
        min_menu()
        seleccion=Pedir_numero()
        if seleccion == "1":
            numero=Pedir_numero()
            k=Pedir_potencia()
            calcular_potencia(int(numero),k)
        elif seleccion == "2":
            numero=Pedir_numero()
            contar_digitos(numero)
        elif seleccion == "3":
            numero=Pedir_numero()
            es_capicua(numero)
        else:
            print("Opción no válida. Intente nuevamente.")
            break
def punto6():
    while True : 
        min_menu2()
        seleccion=Pedir_numero()
        if seleccion != "1" and seleccion != "2":
            break
        m,n= pedir_dimensiones()
        matrizA = cargar_matriz(m,n)
        mostrar_matriz(matrizA,"A")
        matrizB = cargar_matriz(m,n)
        mostrar_matriz(matrizB,"B")
        if seleccion == "1":
            matrizC = sumar_matrices(matrizA, matrizB)
            mostrar_matriz(matrizC,"C")
        elif seleccion == "2":
            matrizC = producto_matrices(matrizA , matrizB)
            mostrar_matriz(matrizC,"C")
def punto7():
    print("Ejercicio 7 no implementado")
def punto8():
    print("Ejercicio 8 no implementado")
def punto9():
    print("Ejercicio 9 no implementado")
def punto10():
    print("Ejercicio 10 no implementado")
if __name__ == "__main__":
    while True:
        menu()
        seleccion=Pedir_numero()
        if seleccion == "1":
            punto1()
        elif seleccion == "2":  
            punto2()
        elif seleccion == "3":
            punto3()
        elif seleccion == "4":
            punto4()
        elif seleccion == "5":
            punto5()
        elif seleccion == "6":
            punto6() 
        elif seleccion == "7":
            print("Ejercicio 7 no implementado")
        elif seleccion == "8": 
            print("Ejercicio 8 no implementado")     
        elif seleccion == "9":
            print("Ejercicio 9 no implementado")
        elif seleccion == "10":
            print("Ejercicio 10 no implementado")
        elif seleccion == "0":
            print("el programa ha finalizado")
            break
        else:
            print("Opción no válida. Intente nuevamente.")