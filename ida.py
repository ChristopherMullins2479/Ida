from moreHelpOptions import yesOptions
from idaJokes import joke
from idaMaths import mathsSum
from idaWeather import weatherSearch
from idaInfo import whoIsIda
import pyttsx3

idaSpeech = pyttsx3.init()

idaIntroduction = ("Hello my name is Ida. I am your personal assistant.\n")
idaSpeech.say(idaIntroduction)
print(idaIntroduction)
idaSpeech.runAndWait()

needHelp = True
while(needHelp == True):
    needHelp = True
    idaSpeech.say("How can i help you today sir ?")
    idaSpeech.runAndWait()
    userInput = input("How can i help you today sir ?\n")

    idaSpeech.say("Serching for " + userInput)
    idaSpeech.runAndWait()

    if('weather' in userInput or 'Weather' in userInput):
        weatherSearch()

    if('joke' in userInput or 'Joke' in userInput):
        joke()
    
    if('sum' in userInput or '-' in userInput or 'Maths' in userInput or 'maths' in userInput or 'Sum' in userInput or 'math' in userInput or 'Math' in userInput):
        mathsSum()

    if('who are you' in userInput ):
        whoIsIda()
    
    if('goodbye' in userInput or 'Goodbye' in userInput or 'bye' in userInput or 'Bye' in userInput ):
        exit
        

    idaSpeech.say("Do you require more help ?")
    idaSpeech.runAndWait()
    needMoreHelp = input("\nDo you require more help ?\n")

    if(needMoreHelp in yesOptions):
        needHelp = True
    else:
        needHelp = False
        idaSpeech.say("Goodbye Sir")
        idaSpeech.runAndWait()


