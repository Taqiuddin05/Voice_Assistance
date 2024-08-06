import warnings
import pyttsx3 as p #to convert text to speech
import speech_recognition as sr #to convert speech to text

from selenium_web import *
from YTauto import *
from news import*

import randfacts

from jokes import *
from weather import *
import datetime

warnings.filterwarnings("ignore")

va = p.init() # va is instance, init gets the current driver info we are using
rate = va.getProperty('rate') # rate of the voice
va.setProperty('rate', 180) # changing the rate
voices = va.getProperty('voices') # list of voices which windows offer
va.setProperty('voice', voices[1].id) # setting voice, 0-male, 1-female
def speak(text):
    va.say(text)
    va.runAndWait()#computer waits untill the sentence gets finished

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return ("morning")
    elif hour>=12 and hour>16:
        return ("afternoon")
    else:
        return ("evening")
today_date = datetime.datetime.now()
r = sr.Recognizer() #to retrieve voice from microphone
speak("Hello sir, good" + wishme() + ", i'm your voice assistant, jexi")
speak("today is" + today_date.strftime("%d") + "of" + today_date.strftime("%B") +", and its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("temperature in Hyderabad is" + str(temp()) + "degree celsius, "+"and with " + str(des()))
speak("how are you doing sir?")

with sr.Microphone() as source:
    r.energy_thresold = 10000 #sensitivity
    r.adjust_for_ambient_noise(source, 1.2) #removes noise
    print("listening..")
    audio = r.listen(source)
    text = r.recognize_google(audio) #converts to text
    print(text)

if "what" and "about" and "you" in text:
    speak("i am having a great day sir")
speak("how can i help you sir?")
with sr.Microphone() as source:
    r.energy_thresold = 10000 # sensitivity
    r.adjust_for_ambient_noise(source, 1.2) # removes noise
    print("listening..")
    audio = r.listen(source)
    text2 = r.recognize_google(audio) # converts to text
print(text2)

if "information" in text2:
    speak("you need information related to which topic?")
    with sr.Microphone() as source:
        r.energy_thresold = 10000  # sensitivity
        r.adjust_for_ambient_noise(source, 1.2)  # removes noise
        print("listening..")
        audio = r.listen(source)
        infor = r.recognize_google(audio)  # converts to text
    print("searching {} in wikipedia".format(infor))
    speak("searching {} in wikipedia".format(infor)) #{} is infor variable
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" and "music" in text2:
    speak("what do you want me to play ?")
    with sr.Microphone() as source:
        r.energy_thresold = 10000  # sensitivity
        r.adjust_for_ambient_noise(source, 1.2)  # removes noise
        print("listening..")
        audio = r.listen(source)
        vid = r.recognize_google(audio)  # converts to text
    print("playing {} on youtube".format(vid))
    speak("playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("sure, i will read news for you sir")
    speak("sure, i will read news for you sir")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" in text2:
    speak("sure sir,")
    x = randfacts.get_fact() #random fact is stored in x
    print("did you know that," + x)
    speak("did you know that," + x)

elif "joke" or "jokes" in text2:
    speak("sure sir, get ready for some chuckles")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
    speak("hahaha wasn't that funny")

speak("thank you for using me and have a great day sir ")
print(" ")
print("thank you for using me :) ")









