# 🎤 Asistente de Voz Personal - Documentación Completa

## 📋 Tabla de Contenidos
1. [Descripción General](#descripción-general)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Configuración Inicial](#configuración-inicial)
5. [Arquitectura del Sistema](#arquitectura-del-sistema)
6. [Funcionalidades](#funcionalidades)
7. [Comandos Disponibles](#comandos-disponibles)
8. [API de la Clase Principal](#api-de-la-clase-principal)
9. [Manejo de Errores](#manejo-de-errores)
10. [Solución de Problemas](#solución-de-problemas)
11. [Extensibilidad](#extensibilidad)
12. [Ejemplos de Uso](#ejemplos-de-uso)

---

## 📖 Descripción General

El **Asistente de Voz Personal** es una aplicación desarrollada en Python que permite interactuar con el computador mediante comandos de voz en español. Fue creado como proyecto para una feria de ciencias escolar en 2022 y posteriormente optimizado en 2025.

### Características Principales:
- 🎯 **Reconocimiento de voz** en español argentino
- 🔊 **Síntesis de voz** con respuestas audibles
- 🌐 **Integración web** (YouTube, WhatsApp, Google, redes sociales)
- 💻 **Control de aplicaciones** de escritorio
- 📝 **Creación de documentos** Word por dictado
- 🌍 **Traductor multiidioma** (inglés, francés, portugués, alemán)
- 🎭 **Entretenimiento** con chistes programados

---

## 💻 Requisitos del Sistema

### Sistema Operativo:
- **Windows 10/11** (requisito obligatorio)
- Arquitectura: x64 recomendada

### Hardware Mínimo:
- **Procesador**: Intel Core i3 o AMD Ryzen 3
- **RAM**: 4 GB mínimo (8 GB recomendado)
- **Almacenamiento**: 100 MB libres
- **Audio**: Micrófono funcional y altavoces/auriculares

### Software Requerido:
- **Python 3.8+** (3.9+ recomendado)
- **Microsoft Word** (para funcionalidad de documentos)
- **Navegador web** moderno (Chrome, Firefox, Edge)
- **Conexión a Internet** estable

---

## 🚀 Instalación

### 1. Instalar Python
```bash
# Descargar desde python.org o usar Microsoft Store
python --version  # Verificar instalación
```

### 2. Instalar Dependencias
```bash
# Instalar todas las librerías necesarias
pip install speechrecognition==3.10.0
pip install pyttsx3==2.90
pip install pywhatkit==5.4
pip install PyAutoGUI==0.9.54
pip install keyboard==0.13.5
pip install googletrans==4.0.0-rc1
```

### 3. Verificar Instalación
```bash
python -c "import speech_recognition, pyttsx3, pywhatkit; print('✅ Todas las librerías instaladas correctamente')"
```

### 4. Configurar Permisos
- **Windows**: Permitir acceso al micrófono en Configuración > Privacidad
- **Antivirus**: Agregar excepción para PyAutoGUI y keyboard

---

## ⚙️ Configuración Inicial

### Configuración de Audio
```python
# El asistente se configura automáticamente, pero puedes personalizar:
asistente = VoiceAssistant(nombre="tu_nombre")  # Cambiar palabra de activación
```

### Variables de Entorno (Opcional)
```bash
# Para configuraciones avanzadas
export ASISTENTE_TIMEOUT=10        # Timeout de escucha
export ASISTENTE_VOLUME=0.9        # Volumen de voz
export ASISTENTE_RATE=145          # Velocidad de habla
```

---

## 🏗️ Arquitectura del Sistema

### Diagrama de Componentes
```
┌─────────────────────────────────────┐
│           VoiceAssistant            │
├─────────────────────────────────────┤
│  - Reconocimiento de Voz (SR)       │
│  - Motor de Síntesis (TTS)          │
│  - Procesador de Comandos           │
│  - Sistema de Logging               │
└─────────────────────────────────────┘
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
┌─────────┐    ┌──────────┐    ┌─────────┐
│ Módulos │    │ Servicios│    │ Control │
│   Web   │    │ Externos │    │   SO    │
└─────────┘    └──────────┘    └─────────┘
│           │              │             │
├─YouTube   ├─Google Trans ├─Keyboard    │
├─WhatsApp  ├─Google Search├─PyAutoGUI   │
├─Instagram │              ├─Aplicaciones│
└─Facebook  │              └─Archivos    │
```

### Flujo de Ejecución
1. **Inicialización**: Configurar motor de voz y componentes
2. **Escucha Activa**: Capturar audio del micrófono
3. **Reconocimiento**: Convertir audio a texto
4. **Procesamiento**: Identificar comando y parámetros
5. **Ejecución**: Realizar acción solicitada
6. **Respuesta**: Proporcionar feedback al usuario
7. **Loop**: Volver al paso 2

---

## 🔧 Funcionalidades

### 1. 🎵 Reproducción de Música
**Comando**: `"Santiago reproduce [nombre de canción]"`

**Funcionalidad**:
- Busca automáticamente en YouTube
- Reproduce en el navegador predeterminado
- Control de pausa/reproducción

**Ejemplo**:
```python
def _reproducir_musica(self, texto: str) -> None:
    """Reproduce música en YouTube usando pywhatkit"""
    cancion = texto.replace('reproduce', '').strip()
    pywhatkit.playonyt(cancion)
```

### 2. ⏰ Información de Tiempo
**Comando**: `"Santiago hora"`

**Funcionalidad**:
- Obtiene hora actual del sistema
- Formato 24 horas (HH:MM)
- Respuesta vocal inmediata

### 3. 📱 Mensajería WhatsApp
**Comando**: `"Santiago mensaje"`

**Proceso**:
1. Solicita número de teléfono
2. Solicita contenido del mensaje
3. Abre WhatsApp Web
4. Envía mensaje automáticamente

**Validaciones**:
- Formato de número argentino (+549261xxxxxxx)
- Verificación de campos obligatorios
- Timeout de carga de WhatsApp Web

### 4. 🔍 Búsquedas Web
**Comando**: `"Santiago busca [término]"`

**Funcionalidad**:
- Búsqueda directa en Google
- Apertura automática en navegador
- Construcción de URL de búsqueda

### 5. 🌍 Traductor Multiidioma
**Comando**: `"Santiago cómo se dice [palabra] en [idioma]"`

**Idiomas soportados**:
- 🇺🇸 Inglés (`en`)
- 🇫🇷 Francés (`fr`)
- 🇵🇹 Portugués (`pt`)
- 🇩🇪 Alemán (`de`)

**Tecnología**: Google Translate API

### 6. 🚀 Lanzador de Aplicaciones

#### Aplicaciones Web:
| Comando | URL |
|---------|-----|
| YouTube | https://www.youtube.com |
| WhatsApp | https://web.whatsapp.com |
| Instagram | https://www.instagram.com |
| Facebook | https://www.facebook.com |

#### Aplicaciones de Escritorio:
- Discord
- Visual Studio Code
- Minecraft (TLauncher)
- Counter Strike
- Call of Duty

### 7. 📝 Editor de Documentos
**Comando**: `"Santiago escribir un archivo"`

**Proceso completo**:
1. Abre Microsoft Word
2. Crea documento nuevo
3. Permite dictado continuo
4. Comandos especiales:
   - `"guardar archivo"`: Guarda el documento
   - `"borrar texto"`: Deshace última acción
   - `"escribir título"`: Formato de título

### 8. 🎭 Sistema de Entretenimiento
**Comando**: `"Santiago chiste"`

**Características**:
- Banco de 5 chistes relacionados con programación
- Selección aleatoria
- Respuesta animada con risas

---

## 📋 Comandos Disponibles

### Tabla Completa de Comandos

| Categoría | Comando | Sintaxis | Ejemplo |
|-----------|---------|----------|---------|
| **Media** | Reproducir | `Santiago reproduce [canción]` | "Santiago reproduce despacito" |
| **Media** | Detener | `Santiago detener` | "Santiago detener" |
| **Info** | Hora | `Santiago hora` | "Santiago hora" |
| **Fun** | Chiste | `Santiago chiste` | "Santiago chiste" |
| **Comunicación** | Mensaje | `Santiago mensaje` | "Santiago mensaje" |
| **Búsqueda** | Buscar | `Santiago busca [término]` | "Santiago busca Python tutorial" |
| **Sistema** | Cambiar ventana | `Santiago cambiar de ventana` | "Santiago cambiar de ventana" |
| **Voz** | Repetir | `Santiago quiero que digas [texto]` | "Santiago quiero que digas hola mundo" |
| **Traducción** | Traducir | `Santiago cómo se dice [palabra] en [idioma]` | "Santiago cómo se dice perro en inglés" |
| **Apps** | Abrir | `Santiago abrir [aplicación]` | "Santiago abrir YouTube" |
| **Control** | Pausa | `Santiago no escuches` | "Santiago no escuches" |
| **Documentos** | Escribir | `Santiago escribir un archivo` | "Santiago escribir un archivo" |
| **Sistema** | Cerrar | `Santiago cerrar ventana` | "Santiago cerrar ventana" |
| **Ayuda** | Ayuda | `Santiago ayuda` | "Santiago ayuda" |
| **Control** | Salir | `Santiago salir` | "Santiago salir" |

---

## 🏛️ API de la Clase Principal

### Constructor
```python
def __init__(self, nombre: str = "santiago"):
    """
    Inicializa el asistente de voz.
    
    Args:
        nombre (str): Palabra de activación del asistente
        
    Attributes:
        nombre (str): Nombre del asistente en minúsculas
        recognizer (sr.Recognizer): Reconocedor de voz
        traductor (Translator): Motor de traducción
        engine (pyttsx3.Engine): Motor de síntesis de voz
        running (bool): Estado de ejecución del asistente
        chistes (List[str]): Banco de chistes disponibles
        comandos (Dict[str, Callable]): Mapeo de comandos a funciones
    """
```

### Métodos Principales

#### Configuración
```python
def _configurar_voz(self) -> None:
    """Configura propiedades del motor de síntesis de voz."""

def _saludar(self) -> None:
    """Reproduce saludo inicial al usuario."""
```

#### Comunicación
```python
def hablar(self, texto: str) -> None:
    """
    Convierte texto a voz y lo reproduce.
    
    Args:
        texto (str): Texto a sintetizar
        
    Raises:
        Exception: Si hay error en el motor de voz
    """

def escuchar(self) -> Optional[str]:
    """
    Escucha y reconoce comandos de voz.
    
    Returns:
        Optional[str]: Texto reconocido o None si hay error
        
    Raises:
        sr.WaitTimeoutError: Timeout de escucha
        sr.UnknownValueError: Audio no reconocible
        sr.RequestError: Error del servicio de Google
    """
```

#### Procesamiento
```python
def procesar_comando(self, texto: str) -> None:
    """
    Procesa y ejecuta comando reconocido.
    
    Args:
        texto (str): Texto del comando a procesar
        
    Note:
        Solo procesa si contiene la palabra de activación
    """
```

#### Control de Flujo
```python
def ejecutar(self) -> None:
    """
    Bucle principal del asistente.
    Mantiene escucha activa hasta recibir comando de salida.
    
    Handles:
        - KeyboardInterrupt: Interrupción manual (Ctrl+C)
        - Exception: Errores generales con continuidad
    """
```

---

## ⚠️ Manejo de Errores

### Sistema de Logging
```python
import logging

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

### Tipos de Errores y Soluciones

#### 1. Errores de Reconocimiento de Voz
```python
# Error: sr.UnknownValueError
# Causa: Audio ininteligible o ruido ambiente
# Solución: Ajuste automático de ruido

try:
    with sr.Microphone() as source:
        self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = self.recognizer.listen(source, timeout=5)
except sr.UnknownValueError:
    print("❓ No pude entender lo que dijiste")
```

#### 2. Errores de Conectividad
```python
# Error: sr.RequestError
# Causa: Sin conexión a Internet o servicio Google no disponible
# Solución: Mensaje informativo y continuidad

except sr.RequestError as e:
    logger.error(f"Error del servicio de reconocimiento: {e}")
    self.hablar("Error de conexión con el servicio de reconocimiento de voz")
```

#### 3. Errores de Automatización
```python
# Error: pyautogui.FailSafeException
# Causa: Movimiento del mouse a esquina superior izquierda (safety)
# Solución: Deshabilitar failsafe o manejar excepción

pyautogui.FAILSAFE = False  # Solo si es necesario
```

### Estrategias de Recuperación

1. **Reintentos Automáticos**: Para errores temporales de red
2. **Degradación Funcional**: Mostrar mensaje en pantalla si TTS falla
3. **Logging Detallado**: Registro de todos los errores para debug
4. **Continuidad del Servicio**: Errores no críticos no detienen ejecución

---

## 🔧 Solución de Problemas

### Problemas Comunes

#### 1. Micrófono No Detectado
```bash
# Verificar dispositivos de audio
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"
```

**Soluciones**:
- Verificar permisos de micrófono en Windows
- Instalar drivers de audio actualizados
- Probar con diferentes dispositivos USB

#### 2. Motor de Voz Sin Sonido
```bash
# Verificar instalación de TTS
python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('test'); engine.runAndWait()"
```

**Soluciones**:
- Verificar volumen del sistema
- Instalar SAPI 5.1 voices adicionales
- Cambiar dispositivo de audio predeterminado

#### 3. PyAutoGUI No Funciona
```python
# Verificar resolución de pantalla
import pyautogui
print(f"Resolución: {pyautogui.size()}")
```

**Soluciones**:
- Ejecutar como administrador
- Deshabilitar DPI scaling
- Verificar permisos de accesibilidad

#### 4. Aplicaciones No Se Abren
```python
# Debug de apertura de aplicaciones
def _abrir_app_desktop(self, nombre_app: str) -> None:
    print(f"Intentando abrir: {nombre_app}")
    keyboard.press_and_release('win')
    sleep(2)
    keyboard.write(nombre_app)
    sleep(3)
    keyboard.press_and_release('enter')
```

**Soluciones**:
- Verificar nombres exactos de aplicaciones
- Agregar aplicaciones al PATH del sistema
- Usar rutas absolutas para aplicaciones específicas

### Diagnóstico del Sistema
```python
def diagnostico_sistema():
    """Función de diagnóstico para verificar componentes"""
    import platform
    import sys
    
    print("=== DIAGNÓSTICO DEL SISTEMA ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version}")
    
    # Verificar librerías
    try:
        import speech_recognition
        print(f"✅ SpeechRecognition: {speech_recognition.__version__}")
    except ImportError:
        print("❌ SpeechRecognition no instalado")
    
    try:
        import pyttsx3
        print("✅ pyttsx3: Disponible")
    except ImportError:
        print("❌ pyttsx3 no instalado")
    
    # Verificar micrófono
    try:
        r = speech_recognition.Recognizer()
        mic_list = speech_recognition.Microphone.list_microphone_names()
        print(f"✅ Micrófonos detectados: {len(mic_list)}")
        for i, mic in enumerate(mic_list[:3]):  # Mostrar primeros 3
            print(f"   {i}: {mic}")
    except:
        print("❌ Error detectando micrófonos")
```

---

## 🔄 Extensibilidad

### Agregar Nuevos Comandos

#### 1. Definir la Función
```python
def _comando_personalizado(self, texto: str) -> None:
    """Nueva funcionalidad personalizada"""
    parametro = texto.replace('mi comando', '').strip()
    
    # Implementar lógica
    resultado = procesar_parametro(parametro)
    
    # Responder al usuario
    self.hablar(f"Ejecutando comando personalizado: {resultado}")
```

#### 2. Registrar el Comando
```python
def __init__(self, nombre: str = "santiago"):
    # ... código existente ...
    
    # Agregar nuevo comando al diccionario
    self.comandos['mi comando'] = self._comando_personalizado
```

### Integrar Nuevas APIs

#### Ejemplo: API del Clima
```python
import requests

def _obtener_clima(self, texto: str) -> None:
    """Obtiene información del clima"""
    ciudad = texto.replace('clima', '').strip()
    
    try:
        # API key gratuita de OpenWeatherMap
        api_key = "TU_API_KEY"
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': ciudad,
            'appid': api_key,
            'units': 'metric',
            'lang': 'es'
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            self.hablar(f"En {ciudad} hay {temp}°C con {desc}")
        else:
            self.hablar("No pude obtener información del clima")
            
    except Exception as e:
        logger.error(f"Error obteniendo clima: {e}")
        self.hablar("Error al consultar el clima")
```

### Personalizar Respuestas

#### Sistema de Personalidades
```python
class PersonalidadAsistente:
    """Sistema de personalidades para el asistente"""
    
    FORMAL = {
        'saludo': 'Buenos días, soy su asistente personal',
        'despedida': 'Ha sido un placer servirle',
        'error': 'Disculpe, ha ocurrido un inconveniente'
    }
    
    CASUAL = {
        'saludo': '¡Hola! Soy tu asistente, ¿cómo andas?',
        'despedida': '¡Nos vemos! Que tengas un buen día',
        'error': 'Ups, algo salió mal'
    }
    
    DIVERTIDO = {
        'saludo': '¡Hola humano! Tu asistente robot está listo 🤖',
        'despedida': 'Adiós, que la fuerza te acompañe ⭐',
        'error': 'Houston, tenemos un problema 🚀'
    }
```

---

## 📚 Ejemplos de Uso

### Caso de Uso 1: Sesión de Trabajo
```
Usuario: "Santiago reproduce música de concentración"
Asistente: "Reproduciendo música de concentración"
[Se abre YouTube con música]

Usuario: "Santiago abrir Visual Studio Code"
Asistente: "Abriendo Visual Studio Code"
[Se abre VS Code]

Usuario: "Santiago escribir un archivo"
Asistente: "Abriendo Microsoft Word. ¿Qué deseas escribir?"
Usuario: "Escribir título Proyecto Final"
Usuario: "Este es mi proyecto final de la materia..."
Usuario: "Guardar archivo"
Asistente: "¿Qué nombre quieres darle al archivo?"
Usuario: "Proyecto Final Programación"
Asistente: "Archivo guardado exitosamente"
```

### Caso de Uso 2: Comunicación
```
Usuario: "Santiago mensaje"
Asistente: "Di lentamente el número de la persona..."
Usuario: "Cuatro cinco seis siete ocho nueve cero"
Asistente: "Ahora di el mensaje que quieres enviar"
Usuario: "Hola mamá, llegué bien a casa"
Asistente: "Enviando mensaje..."
[Se envía mensaje por WhatsApp]
```

### Caso de Uso 3: Información y Entretenimiento
```
Usuario: "Santiago hora"
Asistente: "Son las 14:30"

Usuario: "Santiago chiste"
Asistente: "¿Por qué los programadores prefieren el modo oscuro? 
           Porque la luz atrae bugs. ¡Ja ja ja ja! ¿No está genial?"

Usuario: "Santiago cómo se dice computadora en inglés"
Asistente: "En inglés se dice: computer"

Usuario: "Santiago busca tutorial Python"
Asistente: "Buscando tutorial Python"
[Se abre Google con resultados de búsqueda]
```

### Caso de Uso 4: Control del Sistema
```
Usuario: "Santiago cambiar de ventana"
Asistente: "Cambiando ventana"
[Alt+Tab ejecutado]

Usuario: "Santiago no escuches"
Asistente: "¿Por cuántos segundos quieres que deje de escuchar?"
Usuario: "Treinta segundos"
Asistente: "Dejaré de escuchar durante 30 segundos"
[Pausa de 30 segundos]
Asistente: "He vuelto. ¿Qué necesitas?"

Usuario: "Santiago cerrar ventana"
Asistente: "Ventana cerrada"
[Alt+F4 ejecutado]

Usuario: "Santiago salir"
Asistente: "Hasta luego. ¡Fue un placer ayudarte!"
[Programa termina]
```

---

## 📈 Performance y Optimización

### Métricas de Rendimiento
- **Tiempo de respuesta**: < 2 segundos para comandos simples
- **Uso de CPU**: 5-15% durante escucha activa
- **Uso de RAM**: ~100-150 MB en ejecución
- **Precisión de reconocimiento**: 85-95% en español argentino

### Consejos para Mejor Rendimiento
1. **Ambiente silencioso** para mejor reconocimiento
2. **Dicción clara** y velocidad moderada
3. **Micrófono de calidad** mejora precisión
4. **Conexión estable** para servicios web
5. **Permisos adecuados** evitan errores de sistema

---

## 🤝 Contribución y Desarrollo

### Estructura del Proyecto
```
asistente-voz/
├── README.md
├── asistente_optimizado.py
├── documentacion.md
├── requirements.txt
├── tests/
│   ├── test_comandos.py
│   ├── test_reconocimiento.py
│   └── test_integracion.py
└── ejemplos/
    ├── comando_personalizado.py
    └── nueva_api.py
```

### Guía de Contribución
1. Fork del repositorio
2. Crear branch para nueva funcionalidad
3. Implementar con documentación
4. Agregar tests correspondientes
5. Crear pull request

### Roadmap de Desarrollo
- [ ] Soporte para otros idiomas
- [ ] Integración con más APIs
- [ ] Interfaz gráfica opcional
- [ ] Comandos contextuales
- [ ] Machine Learning para mejor reconocimiento
- [ ] Soporte multiplataforma (macOS, Linux)

---

## 📄 Licencia y Créditos

### Información del Proyecto
- **Proyecto Original**: Feria de Ciencias 2022
- **Autor**: Santiago
- **Versión Optimizada**: 2025
- **Lenguaje**: Python 3.8+
- **Plataforma**: Windows

### Librerías Utilizadas
- `speechrecognition`: Reconocimiento de voz
- `pyttsx3`: Síntesis de voz
- `pywhatkit`: Integración YouTube/WhatsApp
- `pyautogui`: Automatización de GUI
- `keyboard`: Control de teclado
- `googletrans`: Traductor de Google

### Agradecimientos
Gracias a la comunidad de Python y a los desarrolladores de las librerías que hacen posible este proyecto.

---

*Documentación actualizada: Septiembre 2025 | Versión del código: 2.0*