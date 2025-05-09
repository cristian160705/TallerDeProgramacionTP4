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
def cargar_matriz_num(m,n):
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
def sumar_diagonal_principal(matriz):
    suma=0
    for i in range(len(matriz)):
        suma+=matriz[i][i]
    print(f"La suma de la diagonal principal es: {suma}")
    return suma
def factoria_mayor_suma(matriz ,suma_diagonal_principal):
    vectorK=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            factorial = 1
            for k in range(1, (matriz[i][j] + 1)):
                factorial *= k
            if factorial >= suma_diagonal_principal:
                vectorK.append(matriz[i][j])
    print (f"El vector con los numeros cuyo factorial es mayor a la suma de la diagonal principal es: {vectorK}")
    return vectorK
def eliminar_duplicados(vectorK):
    vectorK=list(set(vectorK))
    print(f"El vector sin duplicados es: {vectorK}")
    return vectorK
def min_menu3():
    print("Ingrese el numero 1 si quiere cargar un producto")
    print("Ingrese el numero 2 si quiere mostrar el producto con menor precio")
    print("Ingrese el numero 3 si quiere mostrar los numeros con stock positivo")
    print("Ingrese 0 para salir")
def cargar_matriz(matriz):
    nombre= input("Ingrese el nombre del producto: ")
    proveedor= input("Ingrese el nombre del proveedor: ")
    precio= float(input("Ingrese el precio del producto: "))
    cantidad= int(input("Ingrese la cantidad del producto: "))
    fila=[nombre,proveedor,str(precio),str(cantidad)]
    matriz.append(fila)
    return matriz
def mostrar_producto_menor_precio(matriz):
    precio_menor=float(matriz[0][2])
    nombre=matriz[0][0]
    for fila in range(len(matriz)):
        if float(matriz[fila][2]) < precio_menor:
            precio_menor=float(matriz[fila][2])
            nombre=matriz[fila][0]
    print(f"El producto con menor precio es: {nombre} y su precio es: {precio_menor}$")
def mostrar_numeros_con_stock_positivo(matriz):
    print("Los productos con stock positivo son:")
    for fila in matriz:
        if int(fila[3]) > 0:
            print(f"Nombre: {fila[0]}, Proveedor: {fila[1]}, Precio: {fila[2]}, Cantidad: {fila[3]}")
def min_menu4():
    print("Ingrese el numero 1 para agregar un nuevo paciente a la lista de espera")
    print("Ingrese el numero 2 para determinar el paciente a ser atendido y eliminarlo de la lista de espera")
    print("Ingrese el numero 3 para atender a un pacinte de urgencia y arreglar la lista de espera")
    print("Ingrese el numero 4 para determinar cuantos pacientes faltan para atender a un paciente en particular")
    print("Ingrese el numero 5 para mostrar la lista de espera")
    print("Ingrese el numero 0 para terminar programa")
def agregar_paciente(lista_de_espera):
    nombre=input("Ingrese el nombre del paciente para agregarlo a la lista de espera: ")
    lista_de_espera.append(nombre)
    print(f"Se agrego a {nombre} a la lista de espera")
    return lista_de_espera
def paciente_a_ser_atendido(lista_de_espera):
    if len(lista_de_espera) > 0:
        paciente = lista_de_espera.pop(0)
        print(f"Se atendio al paciente {paciente}")
    else:
        print("No hay pacientes en la lista de espera.")
    return lista_de_espera
def paciente_a_ser_atendido_urgencia(lista_de_espera):
    nombre=input("Ingrese el nombre del paciente para atenderlo de urgencia: ")
    if nombre in lista_de_espera:
        lista_de_espera.remove(nombre)
        print(f"Se atendio al paciente {nombre} de urgencia")
    else:
        print(f"El paciente {nombre} no se encuentra en la lista de espera.")
    return lista_de_espera
def turnos_restantes(lista_de_espera):
    paciente=input("Ingrese el nombre del paciente para saber cuántos turnos faltan para atenderlo: ")
    if paciente in lista_de_espera:
        posicion=lista_de_espera.index(paciente)
        turnos_faltantes=posicion
        print(f"Faltan {turnos_faltantes} turnos para atender al paciente {paciente}")
def min_menu5():
    print("Ingrese el numero 1 para girar los rodillos")
    print("Ingrese el numero 2 para ver los premios acomulados")
    print("Ingrese el numero 0 para terminar el programa")
def mostrar_rodillos(rodillos):
    for i in range(len(rodillos)):
        print(f"Rodillo {i+1}: {rodillos[i]}")
def sacar_rotaciones():
    rotaciones=[]
    for i in range(3):
        numero=random.randint(1,9)
        rotaciones.append(numero)
    print(f"Las rotaciones son: {rotaciones}")
    return rotaciones
def rotar_rodillo(rodillos,rotaciones):
    for i in range(len(rodillos)):
        rodillos[i] = rodillos[i][-rotaciones[i]:] + rodillos[i][:-rotaciones[i]]
    mostrar_rodillos(rodillos)
    return rodillos
def premiacion(rodillos,fichas): 
    if rodillos[0][0]=="X" and rodillos[1][0]=="X" and rodillos[2][0]=="X":
        print("Gano 10 fichas")
        fichas+= 10
    elif rodillos[0][0]=="O" and rodillos[1][0]=="O" and rodillos[2][0]=="O":
        print("Gano 100 fichas")
        fichas+= 100
    elif rodillos[0][0]=="7" and rodillos[1][0]=="7" and rodillos[2][0]=="7":
        print("Gano 1000 fichas")
        fichas+= 1000
    else: 
        print( "No gano nada")
    return fichas
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
        matrizA = cargar_matriz_num(m,n)
        mostrar_matriz(matrizA,"A")
        matrizB = cargar_matriz_num(m,n)
        mostrar_matriz(matrizB,"B")
        if seleccion == "1":
            matrizC = sumar_matrices(matrizA, matrizB)
            mostrar_matriz(matrizC,"C")
        elif seleccion == "2":
            matrizC = producto_matrices(matrizA , matrizB)
            mostrar_matriz(matrizC,"C")
def punto7():
    print("ingrese la dimension de su matriz cuadrada")
    m=Pedir_numero()
    matriz=cargar_matriz_num(int(m),int(m))
    mostrar_matriz(matriz,"cuadrada")
    suma_diagonal_principal=sumar_diagonal_principal(matriz)
    vectorK=factoria_mayor_suma(matriz,suma_diagonal_principal)
    vectorK=eliminar_duplicados(vectorK)
    vectorK.sort()
    print(f"El vector ordenado es: {vectorK}")
def punto8():
    matriz=[]
    while True:
        min_menu3()
        seleccion=Pedir_numero()
        if seleccion == "1":
            matriz = cargar_matriz(matriz)
        elif seleccion == "2":
            mostrar_producto_menor_precio(matriz)
        elif seleccion == "3":
            mostrar_numeros_con_stock_positivo(matriz)
        elif seleccion == "0":
            print("El programa ha finalizado")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
def punto9():
    lista_de_espera=[]
    while True: 
        min_menu4()
        selseccion=Pedir_numero()
        if selseccion == "1":
            lista_de_espera=agregar_paciente(lista_de_espera)
        elif selseccion == "2":
            lista_de_espera=paciente_a_ser_atendido(lista_de_espera)
        elif selseccion == "3":
            lista_de_espera=paciente_a_ser_atendido_urgencia(lista_de_espera)
        elif selseccion == "4":
            turnos_restantes(lista_de_espera)
        elif selseccion == "5":
            print(f"La lista de espera es: {lista_de_espera}")
        elif selseccion == "0":
            print("El programa ha finalizado")
            break
        else:
            print("Opción no válida, intente de nuevo.")
def punto10():
    rodillos=[
        ["X","O","7","X","O","7","X","O","7"],
        ["X","O","7","X","O","7","X","O","7"],
        ["X","O","7","X","O","7","X","O","7"]]
    fichas=0
    print("Rodillos iniciales")
    mostrar_rodillos(rodillos)
    while True:
        min_menu5()
        seleccion=Pedir_numero()
        if seleccion == "1":
            rotaciones=sacar_rotaciones()
            rodillos=rotar_rodillo(rodillos,rotaciones)
            fichas= premiacion(rodillos,fichas)
        elif seleccion == "2":
            print(f"Usted lleva un total de {fichas} acomuladas")
        elif seleccion == "0":
            print("El programa ha terminado")
            break
        else: 
            print("Opcion incorrecta")
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
            punto7()
        elif seleccion == "8": 
            punto8()   
        elif seleccion == "9":
            punto9()
        elif seleccion == "10":
            punto10()
        elif seleccion == "0":
            print("el programa ha finalizado")
            break
        else:
            print("Opción no válida. Intente nuevamente.")