import os

def pantallaPrincipal():
    """Muestra de Menu Principal
    Parameters:
        Ninguno
    Returns:
        Ninguno
    """    
    os.system('cls')
    print("="*40) # <-  ==================================
    print(#Fore.CYAN + 
        "Sistema de getion de productos")
    print("="*40) # <-  ==================================
    #print("-"*30)
    print("-- 1. Agregar producto")
    print("-- 2. Mostrar productos")
    print("-- 3. Actualizar producto")
    print("-- 4. Eliminar producto")
    print("-- 5. Buscar producto")
    print("-- 6. Reporte Stock")
    print("-- 0. Salir")
    print("-"*30)

def campos():
    """Muestra de Menu Principal
    Parameters:
        Ninguno
    Returns:
        Ninguno
    """    
    os.system('cls')
    print("="*40) # <-  ==================================
    print(#Fore.CYAN + 
        "Seleccione que Dato desea trabajar")
    print("="*40) # <-  ==================================
    #print("-"*30)
    print("-- 1. Nombre. ")
    print("-- 2. Descripcion. ")
    print("-- 3. Cantidad. ")
    print("-- 4. Precio. ")
    print("-- 5. Categoria. ")        
    print("-- 0. Salir. ")
    print("-"*30)