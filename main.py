import validadores, menu, inventario

inventario.crearDB()
while True:
    menu.pantallaPrincipal()
    match validadores.validaInt("Indique la tarea que desea realizar: ",-1,7):
        case 0:
            print("-- 0. Salir")                        
            break
        case 1:
            print("-- 1. Agregar producto")
            inventario.agregar_Producto()
        case 2:
            print("-- 2. Mostrar productos")
            inventario.ver_Producto()
            validadores.validaChar("\033[93mIngrese S/N para volver al Menú Principal: \033[0m")
        case 3:
            print("-- 3. Actualizar producto")
            inventario.actualizar_Producto()
        case 4:
            print("-- 4. Eliminar producto")
            inventario.eliminar_Producto()
        #case 5:
        #    while True:
        #         if len(productos) == 0:
        #             print("\033[31mTodavia no hay productos cargsados.\033[0m")
        #         else:
        #             busqueda = validadores.validaStr("Nombre del producto a buscar: ")
        #             encontrados=0
        #             for i in range(len(productos)):
        #                 if busqueda in productos[i][0]:
        #                     print(f"ID:{i+1}\n-sNombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}") 
        #                     encontrados+=1
        #             if encontrados == 0:print("\033[31mNo se encontra ningun resultado.\033[0m")
        #         print("\033[93m\n\nDesea Buscar Otro Producto?: \033[0m") 
        #         if(validadores.validaChar("\033[93mIngrese S/N: \033[0m")=='n'):break
        case 6:
            print("-- 6. Reporte de Stock")
            inventario.reporte_stock()
            validadores.validaChar("\033[93mIngrese S/N para volver al Menú Principal: \033[0m")



