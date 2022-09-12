import pyttsx3

idaSpeech = pyttsx3.init()

def mathsSum():
     idaSpeech.say("Please enter your math problem")
     idaSpeech.runAndWait()

     sumEntered = input("Please enter your math problem\n")
     answer = eval(sumEntered)
     
     idaSpeech.say('The answer to'+sumEntered+' is')
     idaSpeech.runAndWait()

     idaSpeech.say(answer)
     idaSpeech.runAndWait()