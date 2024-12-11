import pyautogui as pg
import time

contador_vueltas = 0
contador_mentas = 0
contador_batallas = 0
imageOffset = 25
waitTime = 6

# Obtener el tamaño de la pantalla
w, h = pg.size()

print("Iniciando Bot Isla Zanahowia!")

def runningBot():
    recogiendoMenta1()
    recogiendoMenta2()
    recogiendoMenta3()
    recogiendoMenta4()
    recogiendoMenta5()
    recogiendoMenta6()
    recogiendoMenta7()
    recogiendoMenta8()


def recogiendoMenta1():
    global contador_mentas
    try:
        pos = pg.locateOnScreen("./menta1.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta 1 encontrada!")
            contador_mentas += 1 
            time.sleep(waitTime)
        else:
            print("Imagen no encontrada en la pantalla.")
    except Exception as e:
        print(f"Menta 1 no disponible.")

def recogiendoMenta2():
    global contador_mentas
    try:
        pos = pg.locateOnScreen("./menta2.png", confidence=0.99)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta 2 encontrada!")
            contador_mentas += 1 
            time.sleep(waitTime)
        else:
            print("Imagen no encontrada en la pantalla.")
    except Exception as e:
        print(f"Menta 2 no disponible.")

def recogiendoMenta3():
    global contador_mentas
    try:
        pos = pg.locateOnScreen("./menta3.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta 3 encontrada!")
            contador_mentas += 1 
            time.sleep(waitTime)
        else:
            print("Imagen no encontrada en la pantalla.")
    except Exception as e:
        print(f"Menta 3 no disponible.")

def recogiendoMenta4():
    global contador_mentas
    try:
        pos = pg.locateOnScreen("./menta4.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta 4 encontrada!")
            contador_mentas += 1 
            time.sleep(waitTime)
        else:
            print("Imagen no encontrada en la pantalla.")
    except Exception as e:
        print(f"Menta 4 no disponible.")

def recogiendoMenta5():
    global contador_mentas
    try:
        pos = pg.locateOnScreen("./menta5.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta 5 encontrada!")
            contador_mentas += 1 
            time.sleep(waitTime)
        else:
            print("Imagen no encontrada en la pantalla.")
    except Exception as e:
        print(f"Menta 5 no disponible.")

def recogiendoMenta6():
    global contador_mentas
    try:
        pos = pg.locateOnScreen("./menta6.png", confidence=0.99)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta 6 encontrada!")
            contador_mentas += 1 
            time.sleep(waitTime)
        else:
            print("Imagen no encontrada en la pantalla.")
    except Exception as e:
        print(f"Menta 6 no disponible.")

def recogiendoMenta7():
    global contador_mentas
    try:
        pos = pg.locateOnScreen("./menta7.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta 7 encontrada!")
            contador_mentas += 1 
            time.sleep(waitTime)
        else:
            print("Imagen no encontrada en la pantalla.")
    except Exception as e:
        print(f"Menta 7 no disponible.")

def recogiendoMenta8():
    global contador_mentas
    try:
        pos = pg.locateOnScreen("./menta8.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta 8 encontrada!")
            contador_mentas += 1 
            time.sleep(waitTime)
        else:
            print("Imagen no encontrada en la pantalla.")
    except Exception as e:
        print(f"Menta 8 no disponible.")


def salirDelCombate():
    global contador_batallas
    try:
        print("Intentando salir del combate...")
      
        # Buscar el botón de salir del combate
        salidaCombate = pg.locateOnScreen("./salida.png", confidence=0.8)
        if salidaCombate:
            # Mover y hacer clic en el botón de salir del combate
            pg.moveTo(salidaCombate.left + imageOffset, salidaCombate.top + imageOffset)
            pg.click()
            print("Botón de salida de combate encontrado y clickeado.")
            time.sleep(waitTime)
            
            # Buscar el botón de confirmación
            confirmacion = pg.locateOnScreen("./confirmacion.png", confidence=0.8)
            if confirmacion:
                pg.moveTo(confirmacion.left + imageOffset, confirmacion.top + imageOffset)
                pg.click()
                print("Botón de confirmación encontrado y clickeado.")
                time.sleep(waitTime)
                
                # Buscar el botón de salir resultados
                salirResultados = pg.locateOnScreen("./salirResultados.png", confidence=0.8)
                if salirResultados:
                    pg.moveTo(salirResultados.left + imageOffset, salirResultados.top + imageOffset)
                    pg.click()
                    print("Botón de salir resultados encontrado y clickeado.")
                    contador_batallas += 1
                    time.sleep(waitTime)
                else:
                    print("Botón de salir resultados no encontrado.")
            else:
                print("Botón de confirmación no encontrado.")
        else:
            print("Botón de salida de combate no encontrado.")
    except Exception as e:
        print(f"No hay combate")

while True:
    contador_vueltas += 1 
    print(f"Iniciando vuelta número: {contador_vueltas}")
    runningBot()
    salirDelCombate()
    print(f"Total de mentas encontradas: {contador_mentas}")
    print(f"Total de batallas cerradas: {contador_batallas}")
    print(f"Esperando 1 min y ejecutando nuevamente")
    print(f"----------------------------------------")
    time.sleep(60)
