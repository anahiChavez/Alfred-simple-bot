import speech_recognition as sr  
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from time import time

# Bot name
name = 'alfred'
start_time =  time()

listener = sr.Recognizer()
engine = pyttsx3.init()

#Get voices and set one of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listening function
def listen():
    try:
        with sr.Microphone() as source:
            print("\n\n\nListening...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

# Actions performed
def run():
    rec = listen()
    if 'play' in rec: 
        music = rec.replace('play', '')
        speak('Playing' + music)
        pywhatkit.playonyt(music)
    elif "Turn off" in rec:
        speak("See you later")
    elif 'time' in rec:
        timeCur = datetime.datetime.now().strftime('%I:%M %p')
        speak ('It is ' + timeCur)
    elif 'what is' in rec:
        order = rec.replace('what is', '')
        info = wikipedia.summary(order, 1)
        speak(info)
    elif 'means' in rec:
        order1 = rec.replace('means', '')
        info1 = wikipedia.summary(order1, 1)
        speak(info1)
    else:
        print('\nPlease, try again')

run()