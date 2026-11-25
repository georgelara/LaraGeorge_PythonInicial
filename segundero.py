import time
def delay(tiempo):
    """
    Genera un retraso de tiempo
    Parameters:
        tiempo: Establece cuantos Segundos de delay
    Returns:
        Ninguno
    """
    for i in range(tiempo,0,-1):
        print(f"\r{i}", end="")
        time.sleep(1)