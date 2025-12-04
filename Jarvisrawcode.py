import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os


#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS("Hello")
    tts.save("temp.mp3")


# Initialize pygame mixer
    pygame.mixer.init()

# Load your MP3 file
    pygame.mixer.music.load("your_file.mp3")

# Play the music
    pygame.mixer.music.play()

# Keep the program running while the music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    os.remove("temp.mp3")
    
    
    
def aiProcess(command):
    client = OpenAI(api_key="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"
    )

    completion = client.chat.completion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud, Give short responses "},
        {"role":"user","content":command}
    ]
    )
    return completion.choices[0].message
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("hhtps://youtube.com")
    elif c.lower().startwith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:#Let AI handle the request
        output = aiProcess(c)
        speak_old(output)
        
        
if __name__ == "__main__":
    speak_old("Initialising jarvis....")
    while True:
        #Listen forn the wake word "JARVIS"
        #Obtain audio from the microphone
        r = sr.Recognizer()
        
        #Reconize speech using google
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2 )
            word = r.recognize_google(audio)
            if(word.lower() == "Jarvis"):
                speak_old("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
        except Exception as e:
            print("Error;{0}".format(0))
        
    
    