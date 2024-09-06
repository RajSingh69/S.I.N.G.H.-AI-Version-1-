import pyttsx3 #Python text to speech version 3
import webbrowser #Imports the web browser
import smtplib # Used to send an email to a client from SMTP (Simple Mail Transfer Protocol)
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha #Tool used for computing answers and providing knowledge, as well as doing analysis reports
import os #Used to get files from operating system
import sys #System specific parameters and functions
#import subprocesses
import cmd



engine = pyttsx3.init('sapi5') #Speech sysntesis voice in python text to speech
client = wolframalpha.Client

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[len(voices)-1].id) #sets the voice

def speak(audio): #Uses audio output from the SAPI5 voice
    print('S.I.N.G.H. : ' + audio) #Says SINGH and then what you said
    engine.say(audio)#Takes the audio input
    engine.runAndWait()#Waits for a command


def greetMe(): #Gets the date and time, uses this algorithm to work out if its morning or evening, based on a certain time frame
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')



greetMe()
#speak('Hello Sir, I am your digital assistant S.I.N.G.H.!')
speak('How may I help you?')

def myCommand():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query

        



if __name__ == '__main__':
    while True:
        query = myCommand()
        query = query.lower()
        print(query)

        if "what are you?" or "who are you" in query:
            speak('I am a personalised artificial intelligence system created by Raj Bhamra on Sunnday 29th September 2019')

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')


        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open cmd' in query:
            speak("Very good Raj")
            ("%windir%\system32\cmd.exe").open
            cmd.open



        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')



        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'insult me' in query:
            insults = ['Prick', 'fat lesbiannnnnnnn', 'Wanker', 'Penguin Molester']
            speak(random.choice(insults))



        

        #if "what are you?" or "who are you" in query:
        #        speak('I am a personalised artificial intelligence system created by Raj Bhamra on Sunnday 29th September 2019')

        if "what can you do" in query:
            speak("I am currently able to do a small ist of things, as this is early stages of my development. I can open google, open youtube, insult you, complement you and search things on wikipedia")
    
        if "what can you do in the future" in query:
            speak("Hopefully, if all goes to plan, i will be able to email people, buy things on amazon and check computer diagnostics from the command prompt")


        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')





        elif 'nothing' in query or 'abort' in query or 'stop' or 'fuck off' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

           

        elif 'hello' in query:
            speak('Hello Sir')



        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

                                    

#        elif 'play music' in query:
#            music_folder = Your_music_folder_path
#            music = [music1, music2, music3, music4, music5]
#            random_music = music_folder + random.choice(music) + '.mp3'
#            os.system(random_music)
#            speak('Okay, here is your music! Enjoy!')

            



        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        

        speak('Next Command! Sir!')

        


