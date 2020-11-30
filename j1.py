import pyttsx3
import datetime
import wikipedia
import webbrowser

# import google
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) shows available voices
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if (hour>=4 and hour<12):
        speak("Good Morning!")
    elif(hour>=12 and hour<16):
        speak("Good Afternoon!")
    elif(hour>=16 and hour<=20):
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am Jarvis Please tell me how may I help you")
    

def takeCommand():
# to take microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in') 
        print(f"User Said: {query}\n")

    except Exception:
        # print(e)
        print("Say that again please...")
        return 'None'
    return query




if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()    
    #logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching in Wikipedia....")
            query=query.replace('wikipedia' ,"")
            results=wikipedia.summary(query,sentences=2)
            try:
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak('Please Try Again')    
            except wikipedia.exceptions.PageError:
                speak('Please Try Again')
                



        # if 'google' in query:
        #     speak("Searching on Google....")
        #     query=query.replace('google' ,"")
        #     results=wikipedia.summary(query,sentences=2)
        #     speak("According to google")
        #     speak(results)
        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'google' in query:
            query = query.replace("google", "")
            chrome_path = r'C:\Users\Dhundiraj\AppData\Local\Google\Chrome\User Data\PepperFlash\32.0.0.453\pepflashplayer.dll %s'
            for url in query(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            print("This is what I found according to your search")
            speak("This is what I found according to your search")