import pyttsx3
from IdaEars import IdaEars

idaSpeech = pyttsx3.init()

def mathsSum():
     idaSpeech.say("Please enter your math problem")
     idaSpeech.runAndWait()

     sumEntered = IdaEars()
     answer = eval(sumEntered)
     
     idaSpeech.say('The answer to'+sumEntered+' is')
     idaSpeech.runAndWait()

     idaSpeech.say(answer)
     idaSpeech.runAndWait()