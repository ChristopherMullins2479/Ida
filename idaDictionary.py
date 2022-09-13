from PyDictionary import PyDictionary
import pyttsx3
from IdaEars import IdaEars

idaSpeech = pyttsx3.init()
dict = PyDictionary()

def dictionary():
    idaSpeech.say('Ive opened my Dictionary What word do you want to look up')
    idaSpeech.runAndWait()

    wordEntered = IdaEars()
    meaning = dict.meaning(wordEntered)
    #print(meaning)

    idaSpeech.say('The Dictionary difination of '+wordEntered+' is ')
    idaSpeech.runAndWait()

    print(meaning)

    idaSpeech.say(meaning)
    idaSpeech.runAndWait()

def spellWord():
     idaSpeech.say('I can help you spell sir. What word do you want me to spell ?')
     idaSpeech.runAndWait()

     wordEntered = IdaEars()
     
     idaSpeech.say(wordEntered+' is spelled.')
     idaSpeech.runAndWait()

     for letter in wordEntered:
        idaSpeech.say(letter)
        idaSpeech.runAndWait()
