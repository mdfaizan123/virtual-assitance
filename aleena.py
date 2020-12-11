import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")


    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello i am aleena. how i can help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeninig...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizer...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('peopletalk7838@gmail.com','People@123')
    server.sendmail('peopletalk7838@gmail.com',to,content)
    server.close()



if __name__ =="__main__":
        wishMe()
        while True:
            query = takeCommand().lower()

            if 'search' in query:
                if 'wikipedia' in query:
                    speak("Searching Wikipedia")
                    query=query.replace('wikipedia',"")
                    results= wikipedia.summary(query, sentences=2)
                    print(results)
                    speak("According to wikipedia")
                    speak(results)

                elif 'youtube' in query:
                    query=query.replace('in youtube',"")
                    query=query.replace('youtube',"")
                    query=query.replace('search ',"")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

                elif 'google' in query:
                    query=query.replace('in google',"")
                    query=query.replace('google',"")
                    query=query.replace('search ',"")
                    
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                
            elif 'open' in query:
                if 'youtube' in query:
                    webbrowser.open("https://www.youtube.com")

                elif 'google' in query:
                    webbrowser.open("https://google.com")

                elif 'stackoverflow' in query:
                    webbrowser.open("https://stackoverflow.com")

                elif 'facebook' in query:
                    webbrowser.open("https://www.facebook.com/")

                elif 'instagram' in query:
                    webbrowser.open("https://instagram.com")

                elif "open chatbot" in query:
                    print("now chatbot active")
                    speak("now chatbot active")
                    app = Flask(__name__)
                    english_bot = ChatBot("Chaterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
                    trainer=ChatterBotCorpusTrainer(english_bot)
                    trainer.train("chatterbot.corpus.english")

                    
                    while True:
                        userText=takeCommand().lower()
                        print(userText)  #user input
                        print(str(english_bot.get_response(userText)))  #bot response
                        speak(str(english_bot.get_response(userText)))



            elif 'play' in query:
                if 'youtube' in  query:
                    webbrowser.open("https://www.youtube.com/watch?v=PHskP9wglJ8&list=RDPHskP9wglJ8&index=1")

                elif 'music' in query:
                    music_dr = "D:\song"
                    songs = os.listdir(music_dr)
                    total_song=len(songs)
                    list1=range(0,total_song)
                    random1=random.choice(list1)
                    print(random1)
                    os.startfile(os.path.join(music_dr,songs[random1]))

                elif 'song' in query:
                    music_dr = "D:\song"
                    songs = os.listdir(music_dr)
                    total_song=len(songs)
                    list1=range(0,total_song)
                    random1=random.choice(list1)
                    print(random1)
                    os.startfile(os.path.join(music_dr,songs[random1]))

            elif 'time' in query:
                strTime=datetime.datetime.now().strftime("%H:%m:%S:")
                print(f"The time is {strTime}")
                speak(f"The time is {strTime}")

            elif 'email to nadeem' in query:
                try:
                    speak('what should i say?')
                    content = takeCommand()
                    to = "mdnadeemhasan999  @gmail.com"
                    sendEmail(to,content)
                    print("Email has been sent!")
                    speak("Email has been sent!")

                except Exception as e:
                    print(e)
                    print("sorry message sending failed")
                    speak("sorry message sending failed")

            
            

            elif 'shutdown my computer' in query:
                os.system("shutdown /s /t 2")
            
            elif 'shutdown my laptop' in query:
                os.system("shutdown /s /t 2")

            elif 'restart my computer' in query:
                os.system("shutdown /r /t 2")

            elif 'restart my laptop' in query:
                os.system("shutdown /r /t 2")

            

            elif 'stop listening' in query:
                exit()

            elif 'nadeem' in query:
                speak("nadeem is good guy")