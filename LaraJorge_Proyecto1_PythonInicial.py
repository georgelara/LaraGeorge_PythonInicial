import os,time
iteracciones=1
productos = []
productos.append(["nombre","categoria",123])
productos.append(["producto","cat",456])
productos.append(["nombre","cat",789])

def segundero(tiempo):
    for i in range(tiempo,0,-1):
        print(f"\r{i}", end="")
        time.sleep(1)

def validaStr(fraseIngreso):
    temp_Str = input(fraseIngreso).strip().lower()
    while not temp_Str.isalpha():
        print("\033[31mError: el nombre solo admite letras.\033[0m")
        segundero(3)
        print("")
        temp_Str = input(fraseIngreso).strip().lower()
    return temp_Str.lower()

def validaChar(fraseIngreso):
    tempChar = input(fraseIngreso).strip().lower()
    while (tempChar!='s' and tempChar!='n'):
        print("\033[31mError: el nombre solo admite una letra.\033[0m")
        tempChar = input(fraseIngreso).strip().lower()
    return tempChar.lower()

def validaInt(fraseIngreso, nivelMenu):
    temp_Str = input(fraseIngreso).strip().lower()
    while not temp_Str.isdigit():
            print("\033[31mError: solo se admiten numeros.\033[0m")
            segundero(3)
            print("")
            if(nivelMenu==0):pantallaPrincipal()
            temp_Str = input(fraseIngreso).strip().lower()
    return int(temp_Str)

def pantallaPrincipal():
    os.system('cls')
    print("="*40) # <-  ==================================
    print("Sistema de getion de productos")
    print("="*40) # <-  ==================================
    print("\n")
    print("-"*30)
    print("-- 1. Agregar producto")
    print("-- 2. Mostrar productos")
    print("-- 3. Buscar producto")
    print("-- 4. Eliminar producto")
    print("-- 5. Salir")
    print("-"*30)
    print("\n\n")

while True:
    pantallaPrincipal()
    seleccion=validaInt("Indique la tarea que desea realizar: ",0)
    if 0 < seleccion < 6:
        match seleccion:
            case 0:
                print("\n\033[31m ingrese un nro de 1 a 5... lea el menu \033[0m")
                segundero(3)
            case 1:
                while True:
                    print("-- 1. Agregar producto") #OPCION 1
                    productos.append(
                        [validaStr("ingrese Nombre del producto: ")
                        ,validaStr("Categoria del producto: "),
                        validaInt("Precio (solo numeros sin centavos): ",1)
                        ])
                    print("\n\nDesea agregar otro producto?")
                    if(validaChar("Ingrese S/N: ")== 'n'):break                    
            case 2:
                    print("-- 2. Mostrar productos")
                    if len(productos) == 0:print("Todavia no hay productos cargados.")
                    else:
                        for i in range(len(productos)): 
                            print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")
                    validaChar("Ingrese S/N para volver al Menú Principal: ")
            case 3:
                while True:
                    print("-- 3. Buscar producto")
                    if len(productos) == 0:
                        print("Todavia no hay productos cargados.")
                    else:
                        busqueda = validaStr("Nombre del producto a buscar: ")
                        encontrados=0
                        for i in range(len(productos)):
                            if busqueda in productos[i][0]:
                                print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}") 
                                encontrados+1
                        if encontrados == 0:print("No se encontra ningun resultado.")
                    print("\n\nDesea Buscar Otro Producto?: ") 
                    if(validaChar("Ingrese S/N: ")=='n'):break
            case 4:
                while True:
                    print("-- 4. Eliminar producto")
                    if len(productos) == 0: print("Todavia no hay productos cargados.")
                    else:
                        for i in range(len(productos)):print(f"{i+1}. {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")
                        id_eliminar = validaInt("Numero de producto a eliminar: ",1)
                        posicion = id_eliminar - 1
                        eliminado = productos.pop(posicion)
                        print(f"se elimino el producto: {eliminado} ") 

                    print("\n\nDesea eliminar otro Producto?: ") 
                    if(validaChar("Ingrese S/N: ")=='n'):break
            case 5:
                print("-- 5. Salir")                        
                break
    else:
        print("\n\033[31m ingrese un nro de 1 a 5... lea el menu \033[0m")
        segundero(3)
