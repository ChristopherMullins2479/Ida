from moreHelpOptions import yesOptions
from idaJokes import joke
from idaMaths import mathsSum
from idaWeather import weatherSearch
from idaDictionary import dictionary, spellWord
from idaInfo import whoIsIda
from IdaEars import IdaEars
import pyttsx3
import speech_recognition as sr

idaSpeech = pyttsx3.init()
IdaListen = sr.Recognizer() 

def startIda():
    wakeUpCommand = IdaEars()
    print(wakeUpCommand)
    wakeUpCommand = wakeUpCommand.lower()
    print(wakeUpCommand)
    if('wake up' in wakeUpCommand or 'hey ruby' in wakeUpCommand):
        idaIntroduction = ("Hello Sir.\n")
        idaSpeech.say(idaIntroduction)
        print(idaIntroduction)
        idaSpeech.runAndWait()

        needHelp = True
        while(needHelp == True):
            needHelp = True
            idaSpeech.say("How can i help you today sir ?")
            idaSpeech.runAndWait()
            userInput = IdaEars()

            if('weather' in userInput or 'Weather' in userInput):
                weatherSearch()

            if('joke' in userInput or 'Joke' in userInput):
                joke()
            
            if('sum' in userInput or '-' in userInput or 'Maths' in userInput or 'maths' in userInput or 'Sum' in userInput or 'math' in userInput or 'Math' in userInput):
                mathsSum()

            if('who are you' in userInput or 'about yourself' in userInput ):
                whoIsIda()
            
            if('goodbye' in userInput or 'Goodbye' in userInput or 'bye' in userInput or 'Bye' in userInput ):
                exit
            
            if('dictionary' in userInput or 'Dictionary' in userInput):
                dictionary()

            if('spell' in userInput and 'word' in userInput):
                spellWord()
                

            idaSpeech.say("Do you require more help ?")
            idaSpeech.runAndWait()
            needMoreHelp = IdaEars()

            if(needMoreHelp in yesOptions):
                needHelp = True
            else:
                needHelp = False
                idaSpeech.say("Goodbye Sir")
                idaSpeech.runAndWait()
                IdaEars()
    else:
        startIda()

startIda()
