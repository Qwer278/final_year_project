import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 6:
        speak("Good night!")
    elif hour >= 6 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening! sir")

    speak("hey siri here can you Please tell me how may I help you")
    print("hey siri here can you Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...>>>")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'open notepad' in query:
            print("opening notepad")
            speak("dear sir your notepad is going to open ")
            npath = "C:\\Windows\\system32"
            os.startfile(npath)
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'play the music' in query:
            speak("playing the song")
            music = "C:\\Users\\HP\Videos\\songs"
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))
        elif 'open youtube' in query:
            print("opening YOUTUBE")
            webbrowser.open("www.youtube.com")
        elif 'open facebook' in query:
            print("Opening Facebook")
            webbrowser.open("www.facebook.com")

        elif "siri off" in query:
            import sys

            speak("thank you sir, have a good day ")
            sys.exit()

        elif 'close Whatsapp' in query:
            speak("closing the whats app")
            os.system("taskkill /f/im    file path")

        elif 'shut down laptop' in query:
            print("shutting down the laptop")
            speak("sir your system is going to be shut down")
            os.system("shutdown /s /t 5")

        elif 'restart the laptop' in query:
            speak("laptop is going to be restart sir")
            os.system("shutdown /r /t 5")

        elif 'sleep the laptop' in query:
            speak("laptop is going to be sleep")
            print("sleeping")
            os.system("rundll32.exe.powrprof.dll,SetSuspendState 0,1,0")

        elif 'set an alarm' in query:
            al = int(datetime.datetime.now().hour)

