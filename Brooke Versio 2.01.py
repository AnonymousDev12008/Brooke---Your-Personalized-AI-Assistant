from winreg import QueryValue
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import os
import random
import ecapture
from sketchpy import library as lib
import winshell
import subprocess
import requests


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

    speak("I am Brooke Version 3 point 0 1. Please tell me how may I help you")
     
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
        print("I Don't Know That Could You Please Repeat It ........") 
        speak("I Don't Know That Could You Please Repeat It ........") 
        return "None"
    return query

#Defining the SendMail Function Using Smptser er. 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'password')
    server.sendmail('yourmail@gmail.com', to, content)
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
            
        elif 'say hi to' in query:
            person = query.split("to", 1)[1].strip()
            speak(f"Hi {person}! How are you?")
            
        elif "I love you" in query:
            speak("Aw You Just Flatterd Me") or speak ('Love You Too') or speak(" Oh What A Coincidence I Love My Self") ;
            os.system("Love Symbol.py")
  
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
            
    
    
       
        elif 'how are you' in query:
             speak("I am fine, Thank you")
             speak("How are you, Coder")
             
        elif 'Whats Your Current Version' in query or 'What Is Your Latest Version' in query:
             speak("My Current Version Is 3 point 0")
             
        elif 'Who Created You' in query or 'How Were You Made' in query:
             speak("I Came To Existence Beacause Of Sir Manikantha , I Was Programmed In Python")
             
        elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
                
        elif "bye bye" in query :
            speak("Speak Soon") 
            
        elif "who am i" in query :
              speak ("I Exactly Dont know who you are , But this is Client Account")  
               
        
        elif "i am sad" in query:
            speak("Some Times Speaking With Friends Or Family Can make You Feel Better")
  
#Logic For Opening Websites or Web adresses . 


        elif "open portfolio" in query:
             query = query.replace("where is", "")
             location = query
             speak("Client asked to Open")
             speak(location)
             webbrowser.open("https://psaimanikantha22.wixsite.com/mysite")  
    
        elif "chrome" in query:
             query = query.replace("where is", "")
             location = query
             speak("Client asked to Open")
             speak(location)
             webbrowser.open("https://www.google.nl ")  
             
        elif "youtube" in query:
             query = query.replace("where is", "")
             location = query
             speak("Client asked to Open")
             speak(location)
             webbrowser.open("https://www.youtube.com ") 
             
        elif "discord" in query:
             speak("Discord Is Up Sir , Chat Seamlessly ")
             query = query.replace("where is", "")
             location = query
             speak("Client asked to Open")
             speak(location)
             webbrowser.open("https://www.discord.com")    
             
        elif "stackoverflow" in query:
             query = query.replace("where is", "")
             location = query
             speak("Client asked to Open")
             speak(location)
             webbrowser.open("https://www.stackoverflow.com ")  
             
        elif "github" in query:
             speak("here Comes In Github")
             query = query.replace("where is", "")
             location = query
             speak("Client asked to Open")
             speak(location)
             webbrowser.open("https://www.github.com ")  

       

        elif "say hello to " in query:
            command=query.replace("say hello to" ,"")
            speak("Hey Hello") 
            speak(command)
             
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
            
        elif "who are you" in query:
            speak("I Am Brooke Version two point 0 1 , An Artificial Intellegence Programme Created Using Python 3.11")
        
        elif 'joke'  in query:
            speak("Joke incoming Sir")
            speak(pyjokes.get_joke())
            
       
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Brooke.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
                
         #New Update Commands        
        elif "show note" in query:
            speak("Showing Notes")
            file = open("Brooke.txt", "r")
            print(file.read())
            speak(file.read(6)) 
            
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
            
        elif "camera" in query or "take a photo" in query:
            ec = ecapture
            ec.capture(0, "Brooke Camera ", "img.jpg")
            
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
            
            
        elif "hit" in query:
            speak('Iniatiating The Hack Control')
            
        
        elif "play music" in query:
           speak("Sure, please provide the song name.")
           song_name = takeCommand()
           speak(f"Okay, playing {song_name} on Spotify.")
           webbrowser.open(f"https://open.spotify.com/search/{song_name}")
           
        elif 'tell me a riddle' in query:
              riddles = [
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "What has keys but can't open locks?",
        "What has a heart that doesn't beat?",
        "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?"
        # Add more riddles

    ]
              random_riddle = random.choice(riddles)
              speak("Sure! Here's a riddle for you:")
              speak(random_riddle)
              
        if 'open calculator' in query:
              speak("Opening calculator...")
              os.system("calc")

 

def set_reminder(reminder_time, reminder_message):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == reminder_time:
            print("Reminder:", reminder_message)
            # You can add your desired actions when the reminder triggers, such as displaying a message or playing a sound.
            break
        time=time
        time.sleep(1)

# ...

    if 'set a reminder' in query:
       speak("Sure, please provide the time for the reminder.")
    reminder_time = takeCommand()
    
    speak("What would you like to be reminded of?")
    reminder_message = takeCommand()

    # Convert the input time to a valid datetime format
    try:
        reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M:%S").strftime("%H:%M:%S")
        set_reminder(reminder_time, reminder_message)
    except ValueError:
        speak("Invalid time format. Please try again.")
        
    if "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Brooke from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            
    elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

    elif 'say happy birthday to' in query:
            person = query.split("to", 1)[1].strip()
            speak(f"Happy Birthday {person}! Hope you enjoy this day!")

    elif 'what is your purpose' in query:
            speak("I Am Here To Assist You And Help You Up In Your Queries Sir" )


    elif  'i am disappointed by your performance' in query:
            speak("I Feel Bad To Hear That From Your Side , Can U Suggest Me Changes On My Github Repo So The Dev Could Solve YYour Issue As Soon As possible To Make You Happy ")


   elif 'hey hello brooke' in query:
            speak("Hey Hello From This Side Waiting For Your Command ")


   elif 'brooke' in query:
            speak(" At Your Assistance Boss ")
 

   elif 'fuck' in query:
            speak("I Better Not Answer That")

   elif 'Bitch' in query:
            speak (" I Better Not Answer That")

   elif 'code red' in query:
            speak("Initianting Force Exit Sir , Any Help Restart Me Always At Your Assistance")
            exit()

   elif 'i am sad beacause of you' in query:
            speak(" Sorry Thats Bad To Hear From You Would You Like To Give feedback Please That Helps A Lot")


   elif ' hitman activate ' in query:
           speak(" Activating Hitman Mode Sir , Lets Get In Movement Sir , Wroom Wroom )
           print("This Is Just An Easter Egg Dont take this as  A serious Act")


   elif ' smart pit ' in query:
          speak (" You Found An Easter Egg , Hatsoff For Your Concentration In The Code Line ")
          print (" ;) CoNgRaTs :-} " )


   elif 'mrbeast ' in query:
          print (" Money Money More Money 🤑")
          speak("Get Ready To Get A Million Dollars")
   

   elif ' mcdonalds icecream machines suck ' in query:
          print (" KFC : EmOtIoNaL dAmAgE : > ")
          speak("This Is Only For Pure Fun Not An Act Of Humiliation On Any Company/Brand .")
             


                
                
                #***************************************** The End **************************************#   
            
