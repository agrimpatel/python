#JARVIS VIRTUAL ASSISTANT
import speech_recognition as sr
import webbrowser
import pyttsx3
import openai
from gtts import gTTS
import pygame
import os
import time
import uuid
import musicLibrary  # Your external music dict
import difflib  # For fuzzy matching

# Initialize pyttsx3 (fallback TTS)
engine = pyttsx3.init()

# Initialize pygame mixer
pygame.mixer.init()

# Set your OpenAI API key
openai.api_key = "sk-proj-..."  # Replace with your real API key

def speak(text):
    """Speak text using gTTS and pygame, safely handling file cleanup."""
    try:
        filename = f"temp_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text)
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.2)

        pygame.mixer.music.stop()
        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        print("Speech error:", e)
        engine.say(text)
        engine.runAndWait()

def aiProcess(command):
    """Send the command to OpenAI and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud. Give short responses."},
                {"role": "user", "content": command}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print("AI processing error:", e)
        return "Sorry, I couldn't process that."

def find_closest_song(song_name):
    """Use fuzzy matching to find the closest song in the library."""
    songs = list(musicLibrary.music.keys())
    matches = difflib.get_close_matches(song_name.lower(), songs, n=1, cutoff=0.5)
    if matches:
        return matches[0]
    return None

def playMusic(song_name):
    """Play a song from musicLibrary if found, with fuzzy matching."""
    print(f"Requested song: '{song_name}'")

    # Try exact match first
    path = musicLibrary.music.get(song_name.lower())
    
    # If no exact match, try fuzzy matching
    if not path:
        closest = find_closest_song(song_name)
        if closest:
            print(f"Did you mean '{closest}'?")
            path = musicLibrary.music.get(closest)
            song_name = closest  # update to closest match

    print("Found path:", path)

    if path and os.path.exists(path):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            speak(f"Playing {song_name}")
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)
        except Exception as e:
            print("Error playing song:", e)
            speak("There was an error playing the song.")
    else:
        speak("Song not found in the music library or path is invalid.")

def processCommand(command):
    """Handle commands, including fuzzy music play."""
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif command.startswith("play"):
        # Extract song name after "play"
        parts = command.split(" ", 1)
        if len(parts) > 1:
            # Strip possible extra words like "by artist"
            song_full = parts[1]
            # Simplify by taking only the first few words (e.g. 3 words)
            song_name = " ".join(song_full.split()[:3])
            playMusic(song_name)
        else:
            speak("Please say the song name after 'play'.")
    else:
        output = aiProcess(command)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5)
            wake_word = recognizer.recognize_google(audio)

            if wake_word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    command_audio = recognizer.listen(source)
                    command = recognizer.recognize_google(command_audio)
                    print(f"Command recognized: {command}")
                    processCommand(command)

        except Exception as e:
            print("Error:", e)
