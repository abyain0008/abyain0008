introcom=["august",'hey august','augy']
introres=['yes sir','what can i do for you','sir']
time=["tell me the time","what is the time","time"]
date1=["what is the date","tell me the date","date"]
weather=["what is the weather","how is the climate","weather","temprature today"]
remind=['save the event','remind this','remind me something','save']
whatsapp=['whatsapp','open whatsapp','connect my whatsapp']
call=['tell me what i did to tell you remind',"remind me","recover"]
import random as rd
import datetime as dt
from datetime import date
import webbrowser as wb
import pyttsx3
import os
from pocketsphinx import LiveSpeech
url='https://www.google.com/search?q='
weatherurl='https://weather.com/en-IN/weather/today'
f=open("D:/reminder file.txt",'x')
while(1):
   
   for phrase in LiveSpeech():
       q=input(phrase)
       print(q)
       engine=pyttsx3.init()
       engine.setProperty('rate',125)
       engine.setProperty('volume',1.0)
       voices=engine.getProperty("voices")
       engine.setProperty('voice',voices[1].id)
       if (q in introcom): 
          engine.say(rd.choice(introres))
          engine.runAndWait()
       elif (q in time):
          now=str(dt.datetime.now())
          engine.say(now)
          engine.runAndWait()
       elif (q in date1):
          today=str(dt.date.today())
          engine.say(today)
          engine.runAndWait()
       elif (q in weather):
          wb.open(weatherurl)
       elif (q in remind):
           print("sir tell me the event need to be saved")
           for phrase in LiveSpeech():
               m=input(phrase)
               print("you said",m)
               f=open("D:/reminder file.txt",'a')
               print(f.write(m))
               break
       elif(q in call):
           f=open("D:/reminder file.txt",'r')
           read=f.read()
           engine.say(read)
           engine.runAndWait()
           f.close()
           os.remove("D:/reminder file .txt")

       elif (q in whatsapp):
          print("scan the comming qr code")
          wb.open("https://web.whatsapp.com/")    
       else:
          wb.open(url+q)
    
