import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import requests
import json
import turtle
from sketchpy import library as lib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning User!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon User!")   

    else:
        speak("Good Evening User!")  

    speak("I am Brooke Version 2 point 0 1 . Please tell me how may I help you")
     
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
        print(f"U: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        speak("Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif "I love you" in query:
            speak("Aw You Just Flatterd Me") or speak ('Love You Too') or speak(" Oh What A Coincidence I Love My Self") ;
            os.system("Love Symbol.py")
  
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
            
        elif 'how are you' in query:
             speak("I am fine, Thank you")
             speak("How are you, Coder")
             
        elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
                
        elif "bye bye" in query :
            speak("Speak Soon") 
            
        elif "who am i" in query :
              speak ("I Exactly Dont know who you are , But this is Client Account")  
               
            
        elif 'play music' in query:
            music_dir = "C:\\Users\manik\OneDrive\Documents\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif "i am sad" in query:
            speak("Some Times Speaking With Friends Or Family Can make You Feel Better")
      
        elif "chrome" in query:
             query = query.replace("where is", "")
             location = query
             speak("User asked to Open")
             speak(location)
             webbrowser.open("https://www.google.nl ")  
             
        elif "youtube" in query:
             query = query.replace("where is", "")
             location = query
             speak("User asked to Open")
             speak(location)
             webbrowser.open("https://www.youtube.com ") 
             
        elif "discord" in query:
             query = query.replace("where is", "")
             location = query
             speak("User asked to Open")
             speak(location)
             webbrowser.open("https://www.spotify.app")    
             
        elif "stackoverflow" in query:
             query = query.replace("where is", "")
             location = query
             speak("User asked to Open")
             speak(location)
             webbrowser.open("https://www.stackoverflow.com ")  
             
        elif "github" in query:
             query = query.replace("where is", "")
             location = query
             speak("User asked to Open")
             speak(location)
             webbrowser.open("https://www.github.com ")  

        elif "spotify" in query:
             query = query.replace("where is", "")
             location = query
             speak("User asked to Open")
             speak(location)
             webbrowser.open("https://www.spotify.com ") 

        elif "say hello to " in query:
            command=query.replace("say hello to" ,"")
            speak("Hey Hello") 
            speak(command)
             
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        elif "who created you" in query:
            speak("I Was created By a Intellegent programmer Mr. Manikantha.  I Was Created in Python 3.11")
            
        elif "who are you" in query:
            speak("I Am Brooke Version two point 0 1 , An Artificial Intellegence Programme Created Using Python 3.11")
        
        elif 'joke'  in query:
            speak("Joke incoming Sir")
            speak(pyjokes.get_joke())
            
    
        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "YourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my Dear Coder. I am not able to send this email")
                
                
                #***************************************** The End **************************************#   
                
                
