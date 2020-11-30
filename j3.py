import pyttsx3
import speech_recognition as sr 
import datetime
import time
import webbrowser
import os
import smtplib
from googlesearch import search
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#defining key points
keys = ["google", "wikipedia", "youtube","maps"]
qs =['what','when','where','why','who','which','how']


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if (hour>=4 and hour<12):
        speak("Good Morning DJ!")
    elif(hour>=12 and hour<16):
        speak("Good Afternoon DJ!")
    elif(hour>=16 and hour<=20):
        speak("Good Evening DJ!")
    else:
        speak("Good Night DJ!")
    speak("I am Jarvis")
    speak("Please tell me how may I help you")


    time.sleep(1) # Sleep for 3 seconds

    print("Waiting for your command...")
    speak("Waiting for your command...")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)
        
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()    

        if 'wikipedia' in query:
            speak("Searching in Wikipedia....")
            query=query.replace('wikipedia' ,"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak('Opening You Tube')
            webbrowser.open('youtube.com')


        else:
            for i in qs:
                if i in query:
                    print("Searching Google...")
                    speak('Searching Google...')
                    query = query.replace("google", "")
                    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                        webbrowser.open("https://google.com/search?q=%s" % query)
                    print("This is what I found according to your search")
                    speak("This is what I found according to your search")
                    break

