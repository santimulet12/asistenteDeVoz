from ast import While
from asyncore import write
from dataclasses import replace
from gzip import WRITE
from logging.config import listen
from msilib.schema import TextStyle
from time import sleep
from cgitb import text
from re import T
from unicodedata import name
from unittest import TextTestResult
from urllib.request import HTTPPasswordMgrWithDefaultRealm
import webbrowser
from xml.sax.saxutils import prepare_input_source
import speech_recognition as sr
import pyttsx3
import pywhatkit
from pywhatkit.remotekit import start_server
from flask import Flask, request
from datetime import date, time, datetime
import chistesESP as c
import pyautogui
import keyboard
from googletrans import Translator

r= sr.Recognizer()

nombre='santiago'

dt = datetime.now()
hora = dt.strftime('%H:%M')

chiste = c.get_random_chiste()

engine=pyttsx3.init()
engine.say('Hola yo soy tu asistente '+nombre)
engine.runAndWait()

voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

def maquina(texto):
    engine.say(texto)
    engine.runAndWait()

traductor=Translator()
texto_trad= 0

def program():
        while True:
            try:
                with sr.Microphone() as source:
                    print('Escuchando...')
                    audio=r.listen(source)
                    text=r.recognize_google(audio, language="es-ES")
                    text=text.lower()
                    print('Has dicho: {}'.format(text))
                    
                    if nombre in text:
                        text=text.replace(nombre, '')
                        if 'reproduce' in text:
                            text = text.replace('reproduce', '')
                            text = text.replace('play', '')
                            musica=text
                            maquina('Reproduciendo'+text)
                            pywhatkit.playonyt(musica)
                        elif 'detener' in text:
                                keyboard.press_and_release('space')
                        elif 'hora' in text:
                            try:
                                maquina('Son las '+hora)
                            except:
                                print('Hubo un error en la condición chiste')
                        elif 'chiste' in text:
                            maquina(chiste+'JAJAJAJAJA ESTÁ RE BUENO JAJAJAJAJAJA')
                        elif 'mensaje' in text:
                            try:
                                print('Diga lentamente el numero de la presona a la cual quiere enviarle el mensaje:')
                                maquina('Diga lentamente el numero de la presona a la cual quiere enviarle el mensaje:')
                                
                                with sr.Microphone() as numero:
                                    audio2=r.listen(numero)
                                    number=r.recognize_google(audio2, language="es-ES")
                                    print('Has dicho: {}'.format(number))

                                print('Diga lentamente el mensaje que quiere enviar:')
                                maquina('Diga lentamente el mensaje que quiere enviar:')
                                
                                with sr.Microphone() as mensaje:
                                    audio3=r.listen(mensaje)
                                    msj=r.recognize_google(audio3, language="es-ES")
                                
                                webbrowser.open('https://web.whatsapp.com/send?phone=+549261'+number)
                                sleep(15)
                                pyautogui.write(msj)
                                pyautogui.press('enter')
                            except:
                                print('Hubo un error en la condición mensaje')
                        elif 'busca' in text:
                            text = text.replace('busca', '')
                            maquina('Buscando '+text)
                            webbrowser.open('https://www.google.com/search?q='+text)
                        elif 'cambiar de ventana' in text:
                            keyboard.press_and_release('alt + tab')
                        elif 'quiero que digas' in text:
                            try:
                                text = text.replace('quiero que digas', '')
                                maquina(text)
                            except:
                                print('Hubo un error en la condición repetir')
                        elif 'cómo se dice' in text:
                            text = text.replace('cómo se dice', '')
                            if 'inglés' in text:
                                text=text.replace('en inglés', '')
                                texto_trad = traductor.translate(text, dest='en')
                                maquina(f'se dice {texto_trad.text}')
                            if 'francés' in text:
                                text=text.replace('en francés', '')
                                texto_trad = traductor.translate(text, dest='fr')
                                maquina(f'se dice {texto_trad.text}')
                            if 'portugués' in text:
                                text=text.replace('en portugués', '')
                                texto_trad = traductor.translate(text, dest='pt')
                                maquina(f'se dice {texto_trad.text}')
                            if 'alemán' in text:
                                text=text.replace('en alemán', '')
                                texto_trad = traductor.translate(text, dest='de')
                                maquina(f'se dice {texto_trad.text}')
                        elif 'abrir' in text:
                            text=text.replace('abrir', '')
                            if 'youtube' in text:
                                maquina(f'abriendo {text}')
                                webbrowser.open('https://www.youtube.com')
                            if 'whatsapp' in text:
                                maquina(f'abriendo {text}')
                                webbrowser.open('https://web.whatsapp.com')
                            if 'instagram' in text:
                                maquina(f'abriendo {text}')
                                webbrowser.open('https://www.instagram.com')
                            if 'facebook' in text:
                                maquina(f'abriendo {text}')
                                webbrowser.open('https://www.facebook.com')
                            if 'discord' in text:
                                maquina(f'abriendo {text}')
                                keyboard.press_and_release('win')
                                sleep(3)
                                keyboard.write('discord')
                                sleep(5)
                                keyboard.press_and_release('enter')
                            if 'pseudocódigo' in text:
                                maquina(f'abriendo {text}')
                                keyboard.press_and_release('win')
                                sleep(3)
                                keyboard.write('pseint')
                                sleep(5)
                                keyboard.press_and_release('enter')
                            if 'counter' in text:
                                maquina(f'abriendo {text}')
                                keyboard.press_and_release('win')
                                sleep(3)
                                keyboard.write('Counter')
                                sleep(5)
                                keyboard.press_and_release('enter')
                            if 'minecraft' in text:
                                maquina(f'abriendo {text}')
                                keyboard.press_and_release('win')
                                sleep(3)
                                keyboard.write('TLauncher')
                                sleep(5)
                                keyboard.press_and_release('enter')
                            if 'cal of duti' in text:
                                maquina(f'abriendo {text}')
                                keyboard.press_and_release('win')
                                sleep(3)
                                keyboard.write('Call of Duty Black Ops III')
                                sleep(5)
                                keyboard.press_and_release('enter')
                            if 'visual studio code' in text:
                                maquina(f'abriendo {text}')
                                keyboard.press_and_release('win')
                                sleep(3)
                                keyboard.write('visual studio code')
                                sleep(5)
                                keyboard.press_and_release('enter')
                        elif 'no escuches' in text:
                            maquina('okey dime solo el lapso de tiempo en segundos por el que no quieres que escuche')
                            with sr.Microphone() as no_esc:
                                audio2=r.listen(no_esc)
                                no_list=r.recognize_google(audio2, language="es-ES")
                            no_list = no_list.replace('segundos', '')
                            no_list = int(no_list)
                            maquina(f'Dejaré de escuchar durante {no_list} segundos')
                            sleep(no_list)
                            maquina('He vuelto, que necesitas?')
                        elif 'escribir un archivo' in text:
                            keyboard.press_and_release('win')
                            sleep(3)
                            keyboard.write('Word')
                            sleep(5)
                            keyboard.press_and_release('enter')
                            sleep(10)
                            keyboard.press_and_release('enter')
                            maquina('que desea escribir?')
                            while True:
                                with sr.Microphone() as escribir:
                                    audio5=r.listen(escribir)
                                    write=r.recognize_google(audio5, language="es-ES")
                                    write=write.lower() 
                                
                                if 'guardar archivo' in write:
                                    write = write.replace('guardar archivo', '')
                                    keyboard.press_and_release('ctrl+g')
                                    sleep(5)
                                    keyboard.press_and_release('enter')
                                    sleep(3)
                                    keyboard.press_and_release('enter')
                                    sleep(3)
                                    keyboard.press_and_release('down arrow')
                                    keyboard.press_and_release('enter')
                                    sleep(1)
                                    keyboard.press_and_release('supr')
                                    maquina('Que nombre desea ponerle al archivo?')

                                    with sr.Microphone() as escribir:
                                        audio5=r.listen(escribir)
                                        write=r.recognize_google(audio5, language="es-ES")
                                        write=write.lower()

                                    keyboard.write(write)
                                    sleep(5)
                                    keyboard.press_and_release('enter')
                                    maquina('archivo guardado')
                                    break

                                elif 'borrar texto' in write:
                                    keyboard.press_and_release('ctrl+z')
                                    write = write.replace(write, '')

                                elif 'escribir título' in write:
                                    write = write.replace('escribir título', '')
                                    keyboard.press_and_release('ctrl+t')
                                    keyboard.write(write)
                                    sleep(3)
                                    keyboard.press_and_release('enter')
                                    keyboard.press_and_release('ctrl+q')
                                    write = write.replace(write, '')

                                keyboard.write(write)
                                keyboard.write(' ')
                        elif 'cerrar ventana' in text:
                            keyboard.press_and_release('alt+F4')
            except:
                print('Hubo un error en la ejecución')
                maquina('Hubo un error en la ejecución, probablemente sea el micrófono')
                break
program()