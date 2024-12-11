import pyautogui as pg
import time

# Obtener el tamaño de la pantalla
w, h = pg.size()
print(f"Screen size: {w}x{h}")
print("Running bot...")

imageOffset = 25
waitTime = 6

def salirDelCombate():
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
                  time.sleep(waitTime)
              else:
                  print("Botón de salir resultados no encontrado.")
          else:
              print("Botón de confirmación no encontrado.")
      else:
          print("Botón de salida de combate no encontrado.")
  except Exception as e:
      print(f"Error al intentar salir del combate: {e}")



def runningBot():

  def recogiendoTrebol1():
    try:
        pos = pg.locateOnScreen("./trebol1.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Trebol encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoTrebol1()
  

  def recogiendoMenta1():
    try:
        pos = pg.locateOnScreen("./menta1.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta encontrada, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Menta no encontrada")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoMenta1()  

  def recogiendoEdelweiss1():
    try:
        pos = pg.locateOnScreen("./edelweiss1.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Edelwiss encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoEdelweiss1()  

  def recogiendoOrquidea1():
    try:
        pos = pg.locateOnScreen("./orquidea1.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Orquidea encontrada, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoOrquidea1()  

  def recogiendoMenta2():
    try:
        pos = pg.locateOnScreen("./menta2.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Menta encontrada, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Menta no encontrada")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoMenta2()  

  def recogiendoTrebol2():
    try:
        pos = pg.locateOnScreen("./trebol2.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Trebol encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoTrebol2()  

  def recogiendoMenta3():
    try:
      pos = pg.locateOnScreen("./menta3.png", confidence=0.9)
      if pos is not None:
          # Calcula la posición del clic
          pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
          pg.click()
          print(f"Menta encontrada, recogiendo...")
          time.sleep(waitTime)
      else:
          print("Menta no encontrada")
    except Exception as e:
      print(f"An error occurred: {e}")
  recogiendoMenta3()  


  def recogiendoEdelweiss2():
    try:
        pos = pg.locateOnScreen("./edelweiss2.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Edelwiss encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoEdelweiss2()


  def recogiendoOrquidea2():
    try:
        pos = pg.locateOnScreen("./orquidea2.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Orquidea encontrada, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoOrquidea2()

  def recogiendoMenta4():
    try:
      pos = pg.locateOnScreen("./menta4.png", confidence=0.9)
      if pos is not None:
          # Calcula la posición del clic
          pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
          pg.click()
          print(f"Menta encontrada, recogiendo...")
          time.sleep(waitTime)
      else:
          print("Menta no encontrada")
    except Exception as e:
      print(f"An error occurred: {e}")
  recogiendoMenta4()  


  def recogiendoTrebol3():
    try:
        pos = pg.locateOnScreen("./trebol3.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Trebol encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoTrebol3()  

  def recogiendoOrquidea3():
    try:
        pos = pg.locateOnScreen("./orquidea3.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Orquidea encontrada, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoOrquidea3()

  def recogiendoEdelweiss3():
    try:
        pos = pg.locateOnScreen("./edelweiss3.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Edelwiss encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoEdelweiss3()

  def recogiendoTrebol4():
    try:
        pos = pg.locateOnScreen("./trebol4.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Trebol encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoTrebol4()  

  def recogiendoTrebol5():
    try:
        pos = pg.locateOnScreen("./trebol5.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Trebol encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoTrebol5()  

  def recogiendoEdelweiss4():
    try:
        pos = pg.locateOnScreen("./edelweiss4.png", confidence=0.9)
        if pos is not None:
            # Calcula la posición del clic
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            print(f"Edelwiss encontrado, recogiendo...")
            time.sleep(waitTime)
        else:
            print("Image not found on the screen")
    except Exception as e:
        print(f"An error occurred: {e}")
  recogiendoEdelweiss4()

while True:
  runningBot()
  salirDelCombate()
  print(f"Esperando 1 min y ejecutando nuevamente")
  time.sleep(60)
