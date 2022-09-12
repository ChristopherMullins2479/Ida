from moreHelpOptions import yesOptions
import pyttsx3

idaSpeech = pyttsx3.init()

def weatherSearch():
    idaSpeech.say('it is raining in Galway')
    idaSpeech.runAndWait()

idaIntroduction = ("Hello my name is Ida. I am your personal assistant.\n")
idaSpeech.say(idaIntroduction)
print(idaIntroduction)
idaSpeech.runAndWait()

needHelp = True
while(needHelp == True):
    idaSpeech.say("How may i asist you ?")
    idaSpeech.runAndWait()
    userInput = input("How may i asist you ?\n")

    idaSpeech.say("Serching for " + userInput)
    idaSpeech.runAndWait()

    if('weather' in userInput or 'Weather' in userInput):
        weatherSearch()

    idaSpeech.say("Do you require more help ?")
    idaSpeech.runAndWait()
    needMoreHelp = input("\nDo you require more help ?\n")

    if(needMoreHelp in yesOptions):
        needHelp = True
    else:
        needHelp = False
        idaSpeech.say("Goodbye Sir")
        idaSpeech.runAndWait()


