import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import smtplib
import os
import random
import urllib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning !")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("I am your Assistant Sir. Tell me how may i help you.")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold = 1.0
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-US')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query
def sendEmail(to,content):
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('__________@gmail.com','_______')
    server.sendmail('yashsunil.gupta@gmail.com',to,content)
    server.close()
                

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            print(results)
            speak("According to wikipedia")
            speak(results)
        elif 'I love you' in query:
            result="I love you too baby"
            speak(result)
            
            
            
            
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open twitter' in query:
            webbrowser.open('twitter.com')
            
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
            
        elif 'open hackerrank' in query:
            webbrowser.open('hackerrank.com')
        
        elif 'open amazon' in query:
            webbrowser.open('amazon.com')
            
        elif 'cricket score' in query:
            webbrowser.open('cricbuzz.com')
            
        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')

        
        
        
        elif 'play music' in query:
            
            music_dir='Z:\\music'
            songs= os.listdir(music_dir)
            n=random.randint(1,len(songs))
            print(songs)
            os.startfile(os.path.join(music_dir,songs[n]))
        
        
        
        
        
        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
            
            
            
            
            
        elif 'open picasa' in query:
            code_path= "C:\\Program Files (x86)\\Google\\Picasa3\\Picasa3.exe"
            os.startfile(code_path)
        elif 'email yash' in query:
            try:
                speak("What should I send yash ?")
                content=takeCommand()
                to = "yashsunil.gupta@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to YASH")
            except Exception as e:
                print(e)
                speak("Sorry my friend yash ..I can't send you email")
        elif 'email mayank' in query:
            try:
                speak("What should I send yash ?")
                content=takeCommand()
                to = "mayankunnao8@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to Mayank")
            except Exception as e:
                print(e)
                speak("Sorry my friend Yash ..I can't send Mayank an email")
                
