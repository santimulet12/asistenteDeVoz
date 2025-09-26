"""
Asistente de Voz Personal - Versión Optimizada 2025
Proyecto de Feria de Ciencias - Solo para Windows
Autor: Santiago
"""

import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyautogui
import keyboard
import logging
from datetime import datetime
from time import sleep
from googletrans import Translator
from typing import Optional, Dict, Any
import random

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VoiceAssistant:
    """Clase principal del asistente de voz"""
    
    def __init__(self, nombre: str = "santiago"):
        self.nombre = nombre.lower()
        self.recognizer = sr.Recognizer()
        self.traductor = Translator()
        self.running = True
        
        # Configuración del motor de voz
        self.engine = pyttsx3.init()
        self._configurar_voz()
        
        # Banco de chistes
        self.chistes = [
            "¿Por qué los programadores prefieren el modo oscuro? Porque la luz atrae bugs",
            "¿Qué le dice un bit a otro bit? Nos vemos en el bus",
            "¿Por qué las computadoras nunca tienen hambre? Porque ya tienen cookies",
            "¿Cuál es el colmo de un programador? Que su hijo sea Java y no le hable",
            "¿Por qué los desarrolladores odian las escaleras? Porque prefieren las funciones recursivas"
        ]
        
        # Comandos disponibles
        self.comandos = {
            'reproduce': self._reproducir_musica,
            'detener': self._detener_reproduccion,
            'hora': self._decir_hora,
            'chiste': self._contar_chiste,
            'mensaje': self._enviar_whatsapp,
            'busca': self._buscar_google,
            'cambiar de ventana': self._cambiar_ventana,
            'quiero que digas': self._repetir_texto,
            'cómo se dice': self._traducir,
            'abrir': self._abrir_aplicacion,
            'no escuches': self._pausa_temporal,
            'escribir un archivo': self._escribir_archivo,
            'cerrar ventana': self._cerrar_ventana,
            'ayuda': self._mostrar_ayuda,
            'salir': self._salir
        }
        
        # Saludo inicial
        self._saludar()

    def _configurar_voz(self) -> None:
        """Configura las propiedades de la voz del asistente"""
        try:
            voices = self.engine.getProperty('voices')
            if voices:
                self.engine.setProperty('voice', voices[0].id)
            self.engine.setProperty('rate', 145)
            self.engine.setProperty('volume', 0.9)
        except Exception as e:
            logger.error(f"Error configurando voz: {e}")

    def _saludar(self) -> None:
        """Saluda al usuario al iniciar"""
        saludo = f'Hola, yo soy tu asistente {self.nombre}. Di "ayuda" para ver todos los comandos disponibles.'
        self.hablar(saludo)

    def hablar(self, texto: str) -> None:
        """Hace que el asistente hable"""
        try:
            self.engine.say(texto)
            self.engine.runAndWait()
        except Exception as e:
            logger.error(f"Error al hablar: {e}")
            print(f"Asistente: {texto}")

    def escuchar(self) -> Optional[str]:
        """Escucha y reconoce comandos de voz"""
        try:
            with sr.Microphone() as source:
                print('🎤 Escuchando...')
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
            texto = self.recognizer.recognize_google(audio, language="es-ES")
            texto = texto.lower().strip()
            print(f'📝 Has dicho: "{texto}"')
            return texto
            
        except sr.WaitTimeoutError:
            print("⏰ Tiempo de espera agotado")
            return None
        except sr.UnknownValueError:
            print("❓ No pude entender lo que dijiste")
            return None
        except sr.RequestError as e:
            logger.error(f"Error del servicio de reconocimiento: {e}")
            self.hablar("Error de conexión con el servicio de reconocimiento de voz")
            return None
        except Exception as e:
            logger.error(f"Error inesperado al escuchar: {e}")
            return None

    def procesar_comando(self, texto: str) -> None:
        """Procesa el comando reconocido"""
        if not texto or self.nombre not in texto:
            return
            
        # Remover el nombre del texto
        comando_limpio = texto.replace(self.nombre, '').strip()
        
        # Buscar y ejecutar comando
        for comando, funcion in self.comandos.items():
            if comando in comando_limpio:
                try:
                    funcion(comando_limpio)
                    return
                except Exception as e:
                    logger.error(f"Error ejecutando comando '{comando}': {e}")
                    self.hablar(f"Hubo un error al ejecutar el comando {comando}")
                    return
        
        self.hablar("No reconocí ese comando. Di 'ayuda' para ver los comandos disponibles.")

    def _reproducir_musica(self, texto: str) -> None:
        """Reproduce música en YouTube"""
        cancion = texto.replace('reproduce', '').replace('play', '').strip()
        if cancion:
            self.hablar(f'Reproduciendo {cancion}')
            pywhatkit.playonyt(cancion)
        else:
            self.hablar("¿Qué canción quieres reproducir?")

    def _detener_reproduccion(self, texto: str) -> None:
        """Pausa/resume la reproducción"""
        keyboard.press_and_release('space')
        self.hablar("Reproducción pausada o reanudada")

    def _decir_hora(self, texto: str) -> None:
        """Dice la hora actual"""
        now = datetime.now()
        hora = now.strftime('%H:%M')
        self.hablar(f'Son las {hora}')

    def _contar_chiste(self, texto: str) -> None:
        """Cuenta un chiste aleatorio"""
        chiste = random.choice(self.chistes)
        self.hablar(f'{chiste}. ¡Ja ja ja ja! ¿No está genial?')

    def _enviar_whatsapp(self, texto: str) -> None:
        """Envía mensaje por WhatsApp Web"""
        try:
            self.hablar('Di lentamente el número de la persona a la cual quieres enviarle el mensaje')
            numero = self.escuchar()
            
            if not numero:
                self.hablar("No pude escuchar el número")
                return
                
            self.hablar('Ahora di el mensaje que quieres enviar')
            mensaje = self.escuchar()
            
            if not mensaje:
                self.hablar("No pude escuchar el mensaje")
                return
                
            # Limpiar número (mantener solo dígitos)
            numero_limpio = ''.join(filter(str.isdigit, numero))
            
            if len(numero_limpio) < 7:
                self.hablar("El número parece incorrecto")
                return
                
            self.hablar("Enviando mensaje...")
            webbrowser.open(f'https://web.whatsapp.com/send?phone=+549261{numero_limpio}')
            sleep(15)  # Esperar a que cargue WhatsApp Web
            pyautogui.write(mensaje)
            pyautogui.press('enter')
            self.hablar("Mensaje enviado")
            
        except Exception as e:
            logger.error(f"Error enviando WhatsApp: {e}")
            self.hablar("Hubo un error al enviar el mensaje")

    def _buscar_google(self, texto: str) -> None:
        """Realiza búsqueda en Google"""
        busqueda = texto.replace('busca', '').strip()
        if busqueda:
            self.hablar(f'Buscando {busqueda}')
            webbrowser.open(f'https://www.google.com/search?q={busqueda}')
        else:
            self.hablar("¿Qué quieres buscar?")

    def _cambiar_ventana(self, texto: str) -> None:
        """Cambia entre ventanas abiertas"""
        keyboard.press_and_release('alt+tab')
        self.hablar("Cambiando ventana")

    def _repetir_texto(self, texto: str) -> None:
        """Repite el texto solicitado"""
        repetir = texto.replace('quiero que digas', '').strip()
        if repetir:
            self.hablar(repetir)
        else:
            self.hablar("¿Qué quieres que diga?")

    def _traducir(self, texto: str) -> None:
        """Traduce texto a diferentes idiomas"""
        texto_limpio = texto.replace('cómo se dice', '').strip()
        
        idiomas = {
            'inglés': 'en',
            'francés': 'fr', 
            'portugués': 'pt',
            'alemán': 'de'
        }
        
        for idioma, codigo in idiomas.items():
            if idioma in texto_limpio:
                palabra = texto_limpio.replace(f'en {idioma}', '').strip()
                if palabra:
                    try:
                        traduccion = self.traductor.translate(palabra, dest=codigo)
                        self.hablar(f'En {idioma} se dice: {traduccion.text}')
                        return
                    except Exception as e:
                        logger.error(f"Error traduciendo: {e}")
                        self.hablar("Error al traducir")
                        return
        
        self.hablar("No reconocí el idioma o la palabra a traducir")

    def _abrir_aplicacion(self, texto: str) -> None:
        """Abre diferentes aplicaciones"""
        apps_web = {
            'youtube': 'https://www.youtube.com',
            'whatsapp': 'https://web.whatsapp.com',
            'instagram': 'https://www.instagram.com',
            'facebook': 'https://www.facebook.com'
        }
        
        apps_desktop = {
            'discord': 'discord',
            'pseudocódigo': 'pseint',
            'counter': 'Counter',
            'minecraft': 'TLauncher',
            'call of duty': 'Call of Duty Black Ops III',
            'visual studio code': 'visual studio code'
        }
        
        texto_limpio = texto.replace('abrir', '').strip()
        
        # Verificar aplicaciones web
        for app, url in apps_web.items():
            if app in texto_limpio:
                self.hablar(f'Abriendo {app}')
                webbrowser.open(url)
                return
        
        # Verificar aplicaciones de escritorio
        for app, nombre_app in apps_desktop.items():
            if app in texto_limpio:
                self.hablar(f'Abriendo {app}')
                self._abrir_app_desktop(nombre_app)
                return
        
        self.hablar("No reconocí esa aplicación")

    def _abrir_app_desktop(self, nombre_app: str) -> None:
        """Abre aplicación de escritorio usando el menú de Windows"""
        keyboard.press_and_release('win')
        sleep(2)
        keyboard.write(nombre_app)
        sleep(3)
        keyboard.press_and_release('enter')

    def _pausa_temporal(self, texto: str) -> None:
        """Pausa el asistente temporalmente"""
        self.hablar('¿Por cuántos segundos quieres que deje de escuchar?')
        
        respuesta = self.escuchar()
        if respuesta:
            try:
                # Extraer número de segundos
                segundos_str = ''.join(filter(str.isdigit, respuesta))
                if segundos_str:
                    segundos = int(segundos_str)
                    if 1 <= segundos <= 300:  # Límite de 5 minutos
                        self.hablar(f'Dejaré de escuchar durante {segundos} segundos')
                        sleep(segundos)
                        self.hablar('He vuelto. ¿Qué necesitas?')
                        return
                        
                self.hablar("Número de segundos inválido")
            except ValueError:
                self.hablar("No entendí el tiempo")
        else:
            self.hablar("No pude escuchar el tiempo")

    def _escribir_archivo(self, texto: str) -> None:
        """Abre Word y permite dictado"""
        try:
            # Abrir Word
            self.hablar("Abriendo Microsoft Word")
            self._abrir_app_desktop('Word')
            sleep(10)
            keyboard.press_and_release('enter')  # Documento en blanco
            sleep(5)
            
            self.hablar('¿Qué deseas escribir? Di "guardar archivo" cuando termines')
            
            while True:
                texto_dictado = self.escuchar()
                if not texto_dictado:
                    continue
                    
                if 'guardar archivo' in texto_dictado:
                    self._guardar_documento()
                    break
                elif 'borrar texto' in texto_dictado:
                    keyboard.press_and_release('ctrl+z')
                elif 'escribir título' in texto_dictado:
                    titulo = texto_dictado.replace('escribir título', '').strip()
                    if titulo:
                        keyboard.press_and_release('ctrl+a')
                        keyboard.write(titulo)
                        keyboard.press_and_release('enter')
                        keyboard.press_and_release('enter')
                else:
                    keyboard.write(texto_dictado + ' ')
                    
        except Exception as e:
            logger.error(f"Error en escribir archivo: {e}")
            self.hablar("Error al escribir archivo")

    def _guardar_documento(self) -> None:
        """Guarda el documento de Word"""
        try:
            keyboard.press_and_release('ctrl+s')
            sleep(3)
            
            self.hablar('¿Qué nombre quieres darle al archivo?')
            nombre = self.escuchar()
            
            if nombre:
                keyboard.write(nombre)
                sleep(2)
                keyboard.press_and_release('enter')
                self.hablar('Archivo guardado exitosamente')
            else:
                keyboard.press_and_release('escape')
                self.hablar('Guardado cancelado')
                
        except Exception as e:
            logger.error(f"Error guardando: {e}")
            self.hablar("Error al guardar archivo")

    def _cerrar_ventana(self, texto: str) -> None:
        """Cierra la ventana actual"""
        keyboard.press_and_release('alt+f4')
        self.hablar("Ventana cerrada")

    def _mostrar_ayuda(self, texto: str) -> None:
        """Muestra los comandos disponibles"""
        ayuda = """
        Comandos disponibles:
        - Reproduce [canción]: Reproduce música en YouTube
        - Detener: Pausa la reproducción
        - Hora: Te dice la hora actual
        - Chiste: Cuenta un chiste
        - Mensaje: Envía mensaje por WhatsApp
        - Busca [término]: Busca en Google
        - Cambiar de ventana: Alterna entre ventanas
        - Quiero que digas [texto]: Repite el texto
        - Cómo se dice [palabra] en [idioma]: Traduce palabras
        - Abrir [aplicación]: Abre aplicaciones
        - No escuches: Pausa temporal del asistente
        - Escribir un archivo: Abre Word para dictado
        - Cerrar ventana: Cierra ventana actual
        - Salir: Termina el programa
        """
        print(ayuda)
        self.hablar("He mostrado todos los comandos en pantalla")

    def _salir(self, texto: str) -> None:
        """Termina el programa"""
        self.hablar("Hasta luego. ¡Fue un placer ayudarte!")
        self.running = False

    def ejecutar(self) -> None:
        """Bucle principal del asistente"""
        logger.info("Asistente de voz iniciado")
        
        while self.running:
            try:
                texto = self.escuchar()
                if texto:
                    self.procesar_comando(texto)
                    
            except KeyboardInterrupt:
                self.hablar("Programa interrumpido por el usuario")
                break
            except Exception as e:
                logger.error(f"Error inesperado: {e}")
                self.hablar("Hubo un error inesperado. Continuando...")
                
        logger.info("Asistente de voz finalizado")

def main():
    """Función principal"""
    print("=" * 60)
    print("🎤 ASISTENTE DE VOZ PERSONAL - VERSIÓN OPTIMIZADA 2025")
    print("=" * 60)
    print("📋 Funciones disponibles:")
    print("   • Reproducción de música en YouTube")
    print("   • Información de hora y chistes")
    print("   • Envío de mensajes por WhatsApp")
    print("   • Búsquedas en Google")
    print("   • Traducciones a múltiples idiomas")
    print("   • Apertura de aplicaciones")
    print("   • Creación de documentos Word")
    print("   • Y mucho más...")
    print("=" * 60)
    print("💡 Di 'Santiago ayuda' para ver todos los comandos")
    print("💡 Di 'Santiago salir' para terminar el programa")
    print("=" * 60)
    
    try:
        asistente = VoiceAssistant()
        asistente.ejecutar()
    except Exception as e:
        logger.error(f"Error fatal: {e}")
        print("❌ Error fatal al inicializar el asistente")

if __name__ == "__main__":
    main()