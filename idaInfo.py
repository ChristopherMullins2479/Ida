import pyttsx3

idaSpeech = pyttsx3.init()

def whoIsIda():
    idaDOB = '12/09/2022'

    idaSpeech.say('Hello my name is Ruby. I am your personal assistant, I was created on '+idaDOB)
    idaSpeech.runAndWait()