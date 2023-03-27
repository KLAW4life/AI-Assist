import pyttsx3 #install the Text to Speech (TTS) library for Python 2 and 3
import datetime

engine = pyttsx3.init()
voice = engine.getProperty('voices') #get the available voices
# engine.setProperty('rate', 135) 
# engine.setProperty('volume', 0.8) 
# engine.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
# engine.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
# engine.setProperty('voice', 'english_rp+f3')


def speak(audio):
    engine.say(audio) #say method for passing text to be spoken
    engine.runAndWait() #run and process the voice command

def time():
    Time = datetime.datetime.now().strftime("%H:&M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

date()