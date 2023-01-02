from personl_buddy import call
from personl_buddy import *

# the concept I want is same as the google assistant,which my PA has to awake when I say the name of the assisatant.


# engine=pyttsx3.init('sapi5') #initialize an instance
# voices=engine.getProperty('voices') #get the available voices
# engine.setProperty('voice',voices[0].id) #set the voices indexes 0 for male,1 for female
# rate=engine.getProperty('rate') #get available rates of voices
# engine.setProperty('rate',170) #set the voice rate
# volume=engine.getProperty('volume') #get the available volume of voices
# engine.setProperty('volume',0.5) #set the volume range from 0.1 to 1.0

# def speak(word):
#     engine.say(word)
#     engine.runAndWait()


# def getCommand():
#         command=sr.Recognizer()
#         with sr.Microphone() as main_source:
#             print("Waiting for you respone...")
#             audio=command.listen(main_source)

#             try:
#                 statement=command.recognize_google(audio,language='en-in')
#                 print(f"buddy say's:{statement}\n" )

#             except Exception as e:
#                 speak("Sorry buddy ,please say that again")
#                 return "None"
#             return statement


# names=("hey buddy","buddy","time to work buddy")
# a1=getCommand().lower()

# if a1 in names:
#     call()



import webbrowser
import speech_recognition as sr

# Set up the recognizer
r = sr.Recognizer()

# Start listening for commands
with sr.Microphone() as source:
    print("Listening for command...")
    audio = r.listen(source)

# Try to recognize the command
try:
    command = r.recognize_google(audio)
    print(f"You said: {command}")
    
    # Open the website if the command is "open website"
    if "open website" in command:
        website = command.split()[-1]
        webbrowser.open(website)
        print(f"Opening {website}...")
    else:
        print("Sorry, I didn't understand that command.")
except sr.UnknownValueError:
    print("Sorry, I didn't catch that. Could you repeat it please?")
except sr.RequestError as e:
    print("Sorry, my speech recognition service is down. {0}".format(e))
