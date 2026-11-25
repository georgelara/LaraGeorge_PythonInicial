import validadores,segundero,sqlite3, menu, os
def crearDB():
    """Creacion de la Tabla Productos en invertario.db
    Parameters:
        Ninguno
    Returns:
        Ninguno
   """
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    os.system('cls')
    print("="*40) # <-  ==================================
    print("Inicio de Sistema")
    print("="*40) # <-  ==================================
    #print("-"*30)
    print("\033[93m\n\nDesea CREAR LA BASE DE DATOS?: \033[0m") 
    if(validadores.validaChar("\033[93mIngrese S/N: \033[0m")=='s'):
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT)
        ''')
        conexion.commit()
        print("se creo la table productos en la base inventario.db")
        segundero.delay(5)

        productos = []
        productos.append(["producto","descripcion",20,15000,"categoria"])
        productos.append(["Lavarropas Drean 11kg","Lavarropas",5,1000000,"Linea Blanca"])
        productos.append(["Calular Iphone 15","Celular",8,1500000,"Telefonia Movil"])
        productos.append(["Cocina Whirlpool 4 hornallas","Cocina",3,1200000,"Linea Blanca"])
        productos.append(["Heladera Whirlpool 270 litros","Heladera",6,1400000,"Linea Blanca"])
        productos.append(["Calular Samsung s23+","Celular",12,1800000,"Telefonia Movil"])
        productos.append(["Monitor LG 256","Monitor",25,800000,"Computacion"])

        cursor.execute("""DELETE FROM productos""")
        conexion.commit()
        
        for a,b,c,d,e in productos:
            cursor.execute('''
                INSERT INTO productos (nombre,descripcion,cantidad,precio,categoria)
                VALUES (?,?,?,?,?)
                ''', (a,b,c,d,e))
            conexion.commit()
    conexion.close()
        
def ver_Producto():
    """
    Muestra productos de la DB
    Parameters:
        Ninguno
    Returns:
        Ninguno
    """
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    if len(productos) == 0: print("\033[31mTodavia no hay productos cargados.\033[0m")
    else:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoria: {producto[5]}")
    conexion.close()

def agregar_Producto():
    """
    Elimina un producto de la DB
    Parameters:
        Ninguno
    Returns:
        Ninguno
    """
    os.system('cls')
    conexion = sqlite3.connect("inventario.db")
    while True:
        cursor = conexion.cursor()
        cursor.execute(
            '''INSERT INTO productos (nombre,descripcion,cantidad,precio,categoria) VALUES (?,?,?,?,?)''', 
            (
                validadores.validaStr("Ingrese Nombre del producto: ",False)
                ,validadores.validaStr("Ingrese Descripcion del producto: ", True)
                ,validadores.validaInt("Ingrese Cantidad: ",0)
                ,validadores.validaFloat("Precio (solo numeros sin centavos): ",0)
                ,validadores.validaStr("Ingrese Categoria del producto: ", True)
            )
        )
        conexion.commit()
        print("\033[93m\n\nDesea agregar otro producto?\033[0m")
        if(validadores.validaChar("Ingrese S/N: ")== 'n'):break
    conexion.close()

def actualizar_Producto():
    """
    Edita un producto de la DB
    Parameters:
        Ninguno
    Returns:
        Ninguno
    """
    os.system('cls')
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    while True:
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        if len(productos) == 0: print("\033[31mTodavia no hay productos cargados.\033[0m")
        else:
            ver_Producto()
            print(f"\033[93m\nFavor de ingresar un nro de los ID mostrados o ingrese 0 para Cancelar\033[0m")
            id_actualizar = validadores.validaInt("Numero de producto: ",-1)
            index=0
            for producto in productos:
                if id_actualizar == producto[0]:
                    print(f"Desde continuar editando ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoria: {producto[5]}")
                    index+=1         
            if index == 0: print("\033[31mERROR: Cancelado o No se encuentra el ID\031[0m")
            else:
                menu.Edicion()
                match validadores.validaInt("Indique la tarea que desea realizar: ",-1,6): 
                    case 0:
                        print("-- 0. Salir")                        
                        break
                    case 1:
                        print("-- 1. Nombre")
                        aux=validadores.validaStr("Ingrese Nombre del producto: ",False)                               
                        cursor.execute('UPDATE productos SET nombre = ? WHERE id = ?',(aux,id_actualizar))
                    case 2:
                        print("-- 2. Descripcion")
                        aux=validadores.validaStr("Ingrese Descripcion del producto: ", True)                        
                        cursor.execute('UPDATE productos SET descripcion = ? WHERE id = ?',(aux,id_actualizar))
                    case 3:
                        print("-- 3. Cantidad")
                        aux=validadores.validaInt("Ingrese Cantidad: ",0)
                        cursor.execute('UPDATE productos SET cantidad = ? WHERE id = ?',(aux,id_actualizar))
                    case 4:
                        print("-- 4. Precio")
                        aux=validadores.validaFloat("Precio (solo numeros sin centavos): ",0)
                        cursor.execute('UPDATE productos SET precio = ? WHERE id = ?',(aux,id_actualizar))
                    case 5:
                        print("-- 5. Categoria")
                        aux=validadores.validaStr("Ingrese Categoria del producto: ", True)
                        cursor.execute('UPDATE productos SET categoria = ? WHERE id = ?',(aux,id_actualizar))
                #conexion.commit()
                #cursor.execute('UPDATE productos SET ? = ? WHERE id = ?', (columna,aux,id_actualizar))
                conexion.commit()

        print("\033[93m\n\nDesea continuar editando?: \033[0m")
        if(validadores.validaChar("\033[93mIngrese S/N: \033[0m")=='n'): break
    conexion.close()

def eliminar_Producto():
    """
    Elimina un producto de la DB
    Parameters:
        Ninguno
    Returns:
        Ninguno
    """
    os.system('cls')
    conexion = sqlite3.connect("inventario.db")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    while True:
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        if len(productos) == 0: print("\033[31mTodavia no hay productos cargados.\033[0m")
        else:
            ver_Producto()
            print(f"\033[93m\nFavor de ingresar un nro de los ID mostrados o ingrese 0 para Cancelar\033[0m")
            id_eliminar = validadores.validaInt("Numero de producto a eliminar: ",-1)
            index=0
            for producto in productos:
                if id_eliminar == producto[0]:
                    print(f"se elimina ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoria: {producto[5]}")
                    index+=1         
            if index == 0: print("\033[31mERROR: Cancelado o No se encuentra el ID\031[0m")
            else:
                cursor.execute('DELETE FROM productos WHERE id=?', (id_eliminar,))
                conexion.commit()
        print("\033[93m\n\nDesea eliminar otro Producto?: \033[0m")
        if(validadores.validaChar("\033[93mIngrese S/N: \033[0m")=='n'): 
            break
    conexion.close()
            
def reporte_stock():
    """
    Muestra productos con stock por debajo de lo ingresado de la DB
    Parameters:
        Ninguno
    Returns:
        Ninguno
    """
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cantidad=validadores.validaInt("Ingrese la cantidad que desea Reportar: ",0)
    cursor.execute('SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad DESC', (cantidad,))
    productos = cursor.fetchall()
    if len(productos) == 0: print("\033[31mNo hay productos con el menores a la cantidad indicada.\033[0m")
    else:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoria: {producto[5]}")
    conexion.close()
#cursor.execute(f'''
#CREATE TABLE IF NOT EXISTS productos (
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#nombre TEXT NOT NULL,
#descripcion TEXT,
#cantidad INTEGER NOT NULL,
#precio REAL NOT NULL,
#categoria TEXT)
#''')