from moreHelpOptions import yesOptions
import pyttsx3
import pyjokes

idaSpeech = pyttsx3.init()

def joke():

    myJoke = pyjokes.get_joke(language="en", category="all")

    idaSpeech.say('Heres a joke')
    idaSpeech.runAndWait()

    idaSpeech.say(myJoke)
    idaSpeech.runAndWait()

    idaSpeech.say('He HeeeHeeeHeeeHeee')
    idaSpeech.runAndWait()

def weatherSearch():
    idaSpeech.say('What city would you like to check the weather for')
    idaSpeech.runAndWait()
    
    cityWeatherChosen = input("What city would you like to check the weather for ?\n")
    idaSpeech.say('looking up the weather in'+cityWeatherChosen)
    idaSpeech.runAndWait()
    idaSpeech.say('In' + cityWeatherChosen+ ' it is cloudy with a chance of Rain')
    idaSpeech.runAndWait()



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

    idaSpeech.say("Do you require more help ?")
    idaSpeech.runAndWait()
    needMoreHelp = input("\nDo you require more help ?\n")

    if(needMoreHelp in yesOptions):
        needHelp = True
    else:
        needHelp = False
        idaSpeech.say("Goodbye Sir")
        idaSpeech.runAndWait()


