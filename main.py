import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

listener = sr.Recognizer()
player = pyttsx3.init()


def listen():
    with sr.Microphone() as input_device:
        print("I am ready, Listening ....")
        player.say('I am ready, Listening ....')
        player.runAndWait()
        voice_content = listener.listen(input_device,phrase_time_limit=8)
        text_command = listener.recognize_google(voice_content,language='en_IN')
        text_command = text_command.lower()
        print(text_command)

    return text_command


def talk(text):
    player.say(text)
    player.runAndWait()


def run_voice_bot():
     command = listen()
     if "hp" in command:
        command = command.replace("hp","")
        if "what is" in command:
            command = command.replace("what is", "")
            info = wikipedia.summary(command, 5)
            talk(info)
        elif "who is" in command:
            command = command.replace("who is", "")
            info = wikipedia.summary(command, 5)
            talk(info)
        elif "play" in command:
            command = command.replace("play", "")
            pywhatkit.playonyt(command)
        else:
            talk("Sorry, I am unable to find what you looking for")


run_voice_bot()
