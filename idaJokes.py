import pyjokes
import pyttsx3

idaSpeech = pyttsx3.init()

#ida will tell a joke 
def joke():

    myJoke = pyjokes.get_joke(language="en", category="all")

    idaSpeech.say('Heres a joke')
    idaSpeech.runAndWait()

    idaSpeech.say(myJoke)
    idaSpeech.runAndWait()

    idaSpeech.say('HeHeeeHeeeHeeeHeee')
    idaSpeech.runAndWait()