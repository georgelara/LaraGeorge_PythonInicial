import validadores, menu, inventario
inventario.crearDB()#menu del programador...Unica ejecucion o usar para autodestruccion.
while True:
    menu.pantallaPrincipal()
    match validadores.validaInt("Indique la tarea que desea realizar: ",-1,7):
        case 0:
            print("-- 0. Salir")                        
            break
        case 1:
            inventario.agregar_Producto()
        case 2:
            inventario.ver_Producto()
            validadores.validaSN("\033[93mIngrese S/N para volver al Menú Principal: \033[0m")
        case 3:
            inventario.actualizar_Producto()
        case 4:
            inventario.eliminar_Producto()
        case 5:
            inventario.buscar_Producto() 
        case 6:
            inventario.reporte_stock()
            validadores.validaSN("\033[93mIngrese S/N para volver al Menú Principal: \033[0m")



