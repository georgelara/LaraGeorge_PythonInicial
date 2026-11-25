import segundero
def validaStr(fraseIngreso:str, nuloAdmitido:int):
    """
        Valida que el usuario ingrese unicamente Texto
        Parameters:
            fraseIngreo: Frase para mostrar al user
            nuloAdmitido: Booleano que define si se admite nulos
        Returns:
            Ninguno
        """
    while True:
        temp_Str = input(fraseIngreso)
        if nuloAdmitido:
            while not temp_Str.replace(" ", "").isalnum()  and not temp_Str=="":
                print("\033[31mError: el nombre solo admite letras, numeros o vacio.\033[0m")
                segundero.delay(3)
                print("")
                temp_Str = input(fraseIngreso).strip().lower()
            if temp_Str == "": return None
            else: return temp_Str
        else:
            while not temp_Str.replace(" ", "").isalnum():
                print("\033[31mError: el nombre solo admite letras y numeros.\033[0m")
                segundero.delay(3)
                print("")
                temp_Str = input(fraseIngreso).strip().lower()
            return temp_Str.lower() 
    
def validaSN(fraseIngreso:str):
    """
    Valida que el usuario ingrese unicamente S o N, para confirmar actividad"
    Parameters:
        fraseIngreso: Frase para mostrar al user
    Returns:
        Ninguno
    """
    tempChar = input(fraseIngreso).strip().lower()
    while (tempChar!='s' and tempChar!='n'):
        print("\033[31mError: el nombre solo admite una letra S/N.\033[0m")
        tempChar = input(fraseIngreso).strip().lower()
    return tempChar.strip().lower()

def validaInt(fraseIngreso:str, minimo:int, maximo:int=0):
    """
    Valida que el usuario ingrese enteros positivos, para confirmar actividad"
    Parameters:
        fraseIngreso: Frase para mostrar al user
        minimo: entero que se establece como minimo
        maximo: entero (opcional) que se establece maximo 
    Returns:
        Ninguno
    """
    while True:
        temp_Str = input(fraseIngreso).strip().lower()
        try :
            if (maximo==0):
                if (minimo<int(temp_Str)): break
                else:  print(f"\033[31mError: solo se admiten numeros mayores a {minimo}.\033[0m")
                segundero.delay(3)
            else:
                if (minimo<int(temp_Str)<maximo): break
                else: print(f"\033[31mError: Ingrese numeros entre {minimo} y {maximo}\033[0m")
                segundero.delay(3)
        except ValueError:
            print("\033[31mError: solo se admiten numeros.\033[0m")
            segundero.delay(3)
            print("")
    return int(temp_Str)

def validaFloat(fraseIngreso:str, minimo:int):
    """
    Valida que el usuario ingrese enteros positivos, para confirmar actividad"
    Parameters:
        fraseIngreso: Frase para mostrar al user
        minimo: Entero que se establece como minimo
    Returns:
        Ninguno
    """
    while True:
        temp_Str = input(fraseIngreso).strip().lower()
        try :
            if (float(temp_Str)>minimo): break
            else: print(f"\033[31mError: solo se admiten numeros mayores a {minimo}.\033[0m")
        except ValueError:
            print(f"\033[31mError: solo se admiten numeros.\033[0m")
            segundero.delay(3)
            print("")
    return float(temp_Str)
