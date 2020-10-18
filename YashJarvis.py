import pyttsx3
import win32com.client
import win32api
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices)



