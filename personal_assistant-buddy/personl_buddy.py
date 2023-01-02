import speech_recognition as sr
import pyttsx3
import os
import requests
import subprocess
from AppOpener import run
from moviepy.editor import *
import pygame
import webbrowser
import wikipedia
import json

def call():

    print('Loading your personal assistant buddy...')

    engine=pyttsx3.init('sapi5') #initialize an instance
    voices=engine.getProperty('voices') #get the available voices
    engine.setProperty('voice',voices[0].id) #set the voices indexes 0 for male,1 for female
    rate=engine.getProperty('rate') #get available rates of voices
    engine.setProperty('rate',170) #set the voice rate
    volume=engine.getProperty('volume') #get the available volume of voices
    engine.setProperty('volume',0.5) #set the volume range from 0.1 to 1.0

    def speak(word):
        engine.say(word)
        engine.runAndWait()

    def verify():
        speak("hey buddy!! , please verify yourself before proceeding")
        access_code_1=20
        access_code_2=int(getCommands())
        if access_code_1 == access_code_2:
            speak("Access granted")
            speak("so tell me buddy , what's our plans for today!!")
            def works():
                while True:
                    process=getCommands().lower()
                    if process==0:
                        continue

                    if "wrap up" in process or "stop" in process or "ok bye buddy" in process:
                        speak("buddy is about to sleep")
                        print("Gud Bye, sir")
                        break

                    if "open application" in process or "open the app" in process:
                        speak("which application you would like to open..!!")
                        app=getCommands()
                        run(app)

                    if "open a video" in process or "video" in process:
                        speak("please say the name of the video , sir")
                        a1=getCommands().lower()
                        a2=rf'F:\Sanjay\motivation\{a1}.mp4'
                        pygame.display.set_caption('hello buddy')
                        vid=VideoFileClip(a2)
                        vid.preview()
                        pygame.quit()

                    if "open a website" in process or "website" in process:
                        speak("please say the name of the website , sir")
                        a1=getCommands().lower()
                        a2=rf'https://www.{a1}.com'
                        webbrowser.open_new_tab(a2)
                        speak(rf'{a1} is opening') 

                    if "wikipedia" in process or "wiki" in process:
                        speak("what would you like to know about sir!!")
                        a1=getCommands().lower()
                        answer=wikipedia.summary(a1,sentences=4)
                        speak("According to Wikipedia")
                        print(answer)
                        speak(answer)

                    if "weather" in process or "what's the weather" in process:
                        api_key="f401405a1ed200b69b78cb159c93af38"
                        base_url="https://api.openweathermap.org/data/2.5/weather?"
                        speak("what's the city name")
                        city_name=getCommands()
                        complete_url=base_url+"appid="+api_key+"&q="+city_name
                        response= requests.get(complete_url)
                        x=response.json()
                        if x["cod"]!="404":
                            y=x["main"]
                            current_temperature = y["temp"]
                            current_humidiy = y["humidity"]
                            z = x["weather"]
                            weather_description = z[0]["description"]
                            speak(" Temperature in kelvin unit is " +
                                    str(current_temperature) +
                                    "\n humidity in percentage is " +
                                    str(current_humidiy) +
                                    "\n description  " +
                                    str(weather_description))
                            print(" Temperature in kelvin unit = " +
                                    str(current_temperature) +
                                    "\n humidity (in percentage) = " +
                                    str(current_humidiy) +
                                    "\n description = " +
                                    str(weather_description))
                        else:
                            speak(" City is not found ")

                    if "Lock the screen" in process or "Sleep" in process:
                        speak("Your system is about to lock")
                        subprocess.call(["shutdown", "/l"]) #shutdown command

                    

                    



            works()

        else :
            speak("Access denied , you have 2 chances left")
            access_code_2=int(getCommands())
            if access_code_1 == access_code_2:
                speak("Access granted")
                works()
            else :
                speak("Access denied , you have 1 chance left")
                access_code_2=int(getCommands())
                if access_code_1 == access_code_2:
                    speak("Access granted")
                    works()
                else :
                    speak("Access denied , you are about to shutdown")
                    subprocess.call(["shutdown", "/l"]) #shutdown command


    def getCommands():
        command=sr.Recognizer()
        with sr.Microphone() as main_source:
            print("Waiting for you respone...")
            audio=command.listen(main_source)

            try:
                statement=command.recognize_google(audio,language='en-in')
                print(f"buddy say's:{statement}\n" )

            except Exception as e:
                speak("Sorry buddy ,please say that again")
                return "None"
            return statement
        
    speak("Loading your personal assistant buddy")
    verify()


    




