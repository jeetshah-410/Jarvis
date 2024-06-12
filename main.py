import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as kit
import os


eng = pyttsx3.init('sapi5')
voice = eng.getProperty('voices')
eng.setProperty('voices', voice[0].id)


def say(audio: object):

    eng.say(audio)
    eng.runAndWait()


def takeCommand():

    com = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")

        com.energy_threshold = 300  # Min audio energy
        com.pause_threshold = 1.2       # seconds before speaking audio
        com.dynamic_energy_threshold = True
        com.operation_timeout = None
        com.phrase_threshold = 0.4   # seconds before commanding
        com.non_speaking_duration = 0.5

        audio = com.listen(source)

    try:
        print("Recognizing.....")
        command = com.recognize_google(audio, language='en-in')
        print(f"User said: {command}")

    except Exception:
        say("I am unable to recognize, try again please!")

        return "None"

    return command


def intro():

    hrs = int(datetime.datetime.now().hour)

    if 0 <= hrs < 12:
        say("Good Morning!")

    elif hrs >= 12 and hrs < 18:
        say("Good Afternoon")

    else:
        say("Good Evening!")

    say("I am JARVIS sir, command")


if __name__ == "__main__":

    intro()

    while True:
        command = takeCommand().lower()

        if 'jarvis wikipedia' in command:
            say("Copy That")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            say("According to wikipedia...")
            print(results)
            say(results)

        elif 'jarvis open google' in command:
            say("Copy that: opening google")
            webbrowser.open("google.com")

        elif 'jarvis open youtube' in command:
            say("Copy that: opening youtube")
            webbrowser.open("youtube.com")

        elif 'jarvis open spotify' in command:
            say("Copy that: opening spotify")
            webbrowser.open("spotify.com")

        elif 'jarvis play' in command:
            say("Copy that")
            kit.playonyt(command)

        elif 'jarvis open whats app' in command:
            say("Copy that: opening")
            webbrowser.open("whatsapp.com")

        elif 'jarvis time' in command:
            say("Copy that: opening")
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            say(Time)


        elif 'jarvis open code' in command:
            say("Copy that: opening")
            path = "C:\\Users\\jeets\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'jarvis open game' in command:
            say("Copy that: opening Valorant")
            valo = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(valo)

        elif 'open powerpoint' in command:
            say("Copy that: opening office")
            ppt = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(ppt)

        elif 'jarvis sleep' in command:
            say("Sleeping, bye!")
            break   