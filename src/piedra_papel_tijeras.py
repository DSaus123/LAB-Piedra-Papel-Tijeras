import random

def ordenador_decide_jugada():
    '''
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ") 
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")   
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    print("-Nueva Ronda-")
    jugada_ordenador = ordenador_decide_jugada()
    jugada_usuario = usuario_decide_jugada()
    print(f"El ordenador eligió: {jugada_ordenador}")
    if determina_ganador(jugada_usuario, jugada_ordenador) == "Empate":
        return("Es un empate")
    elif determina_ganador(jugada_usuario, jugada_ordenador) == "Ganaste":
        return("Ganaste")
    else:
        return("Perdiste")
    
def jugar_torneo(n):
    print("Bienvenido al torneo de piedra, papel o tijeras")
    puntos_usuario, puntos_ordenador = 0, 0
    while (max(puntos_usuario, puntos_ordenador) != n):
        res = jugar()
        if res == "Ganaste":
            puntos_usuario += 1
        elif res == "Perdiste":
            puntos_ordenador += 1
        else:
            print("No cambian los puntos")
        print(f"\nResultado de la ronda: {puntos_usuario}-{puntos_ordenador} (usuario-ordenador)")

    print(f"\nResultado del torneo: {puntos_usuario}-{puntos_ordenador} (usuario-ordenador)")
    if puntos_usuario > puntos_ordenador:
        print("Felicidades, has ganado el torneo")
    elif puntos_usuario < puntos_ordenador:
        print("Has perdido el torneo")
    else:
        print("Se ha producido un empate")


if __name__ == "__main__":
    jugar_torneo(3)
