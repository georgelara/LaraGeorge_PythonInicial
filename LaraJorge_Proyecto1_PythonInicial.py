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
        print("\033[31mError: el nombre solo admite una letra S/N.\033[0m")
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
                    print("-- 1. Agregar producto")
                    productos.append(
                        [validaStr("ingrese Nombre del producto: ")
                        ,validaStr("Categoria del producto: "),
                        validaInt("Precio (solo numeros sin centavos): ",1)
                        ])
                    print("\033[93m\n\nDesea agregar otro producto?\033[0m")
                    if(validaChar("Ingrese S/N: ")== 'n'):break                    
            case 2:
                    print("-- 2. Mostrar productos")
                    if len(productos) == 0:print("\033[31mTodavia no hay productos cargados.\033[0m")
                    else:
                        for i in range(len(productos)): 
                            print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")
                    validaChar("\033[93mIngrese S/N para volver al Menú Principal: \033[0m")
            case 3:
                while True:
                    print("-- 3. Buscar producto")
                    if len(productos) == 0:
                        print("\033[31mTodavia no hay productos cargados.\033[0m")
                    else:
                        busqueda = validaStr("Nombre del producto a buscar: ")
                        encontrados=0
                        for i in range(len(productos)):
                            if busqueda in productos[i][0]:
                                print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}") 
                                encontrados+=1
                        if encontrados == 0:print("\033[31mNo se encontra ningun resultado.\033[0m")
                    print("\033[93m\n\nDesea Buscar Otro Producto?: \033[0m") 
                    if(validaChar("\033[93mIngrese S/N: \033[0m")=='n'):break
            case 4:
                while True:
                    print("-- 4. Eliminar producto")
                    if len(productos) == 0: print("\033[31mTodavia no hay productos cargados.\033[0m")
                    else:
                        for i in range(len(productos)):print(f"{i+1}. {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")
                        id_eliminar = validaInt("Numero de producto a eliminar o 0 Para Cancelar: ",1)
                        while(len(productos)<id_eliminar or id_eliminar<0):
                            print(f"\033[31mFavor de ingresar un nro entre 0 y {len(productos)}\033[0m")
                            id_eliminar = validaInt("Numero de producto a eliminar: ",1)
                        if(id_eliminar==0):break
                        posicion = id_eliminar - 1
                        eliminado = productos.pop(posicion)
                        print(f"se elimino el producto: {eliminado} ")

                    print("\033[93m\n\nDesea eliminar otro Producto?: \033[0m") 
                    if(validaChar("\033[93mIngrese S/N: \033[0m")=='n'):break
            case 5:
                print("-- 5. Salir")                        
                break
    else:
        print("\n\033[31m ingrese un nro de 1 a 5... lea el menu \033[0m")
        segundero(3)