from data import save_data, load_data
from listen import listen
from speak import speak
from weather import get_weather
from date_time import get_date, get_time
import objc
import spacy
import json
import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime

    
# try:
#     engine = pyttsx3.init()
# except ImportError:
#     print("pyttsx3 requires pyobjc on macOS, please ensure it is installed.")
#     raise
# except RuntimeError as e:
#     print(f"An error occurred while initializing pyttsx3: {e}")
#     raise

# nlp = spacy.load("en_core_web_sm")

# def process_command(command):
#     doc = nlp(command)
#     if any(token.lemma_ in ["time", "clock"] for token in doc):
#         return "time"
#     elif any(token.lemma_ in ["date", "day"] for token in doc):
#         return "date"
#     elif any(token.lemma_ in ["weather", "forecast"] for token in doc):
#         for ent in doc.ents:
#             if ent.label_ == "GPE":
#                 return ("weather", ent.text)
#         return "ask_city"
#     elif any(token.lemma_ in ["stop", "shutdown", "off"] for token in doc):
#         return "shutdown"
#     else:
#         return "unknown"



def greet():
    speak("Hello, how can I assist you today?")

def shutdown():
    speak("Shutting down. Goodbye!")

def main():
    greet()
    while True:
        command = listen().lower()
        if "time" in command:
            speak(f"The current time is {get_time()}")
        elif "date" in command:
            speak(f"Today's date is {get_date()}")
        elif "weather" in command:
            speak("Which city?")
            city = listen().lower()
            weather_info = get_weather(city)
            speak(weather_info)
        elif "shutdown" in command:
            shutdown()
            break
        else:
            speak("Sorry, I can not help with that yet.")

if __name__ == "__main__":
    main()
