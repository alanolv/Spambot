import pyautogui
import pyautogui as pg
import webbrowser as web
from time import sleep
print("Bienvenido al bot de mensajes")
print("Escoja la resolucion de su pantalla")
print("1)_1920X1080")
print("2)_1280X720")
# Escojer en la pantalla que se encuentra el ususario
pantalla = int(input("Selecione el numero de su resolucion\n"))
# Introducir el mensaje a mandar
msj = input("¿Cual es tu mensaje?\n")
# Escribir el numero de destino
num = input("Escriba el numero de destino con su lada (+52XXXXXXXXXX)\n")
# Escribir el numero de mensajes a mandar
numMsj = int(input("¿Cuantas veces desea enviar el mensaje?\n"))
match pantalla:
    case 1:
        web.open('https://web.whatsapp.com/send?phone='+num)
        sleep(10)
        pg.click(847, 971)
        sleep(1)
        for i in range(numMsj):
            pyautogui.typewrite(msj)
            pyautogui.press('enter')
    case 2:
        web.open('https://web.whatsapp.com/send?phone='+num)
        sleep(10)
        pg.click(618, 647)
        sleep(1)
        for i in range(numMsj):
            pyautogui.typewrite(msj)
            pyautogui.press('enter')
    case _:
        print("Resolucion no encontrada")
