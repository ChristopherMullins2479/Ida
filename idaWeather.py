import pyttsx3
from IdaEars import IdaEars

idaSpeech = pyttsx3.init()

#ida will check the weather
def weatherSearch():
    idaSpeech.say('What city would you like to check the weather for')
    idaSpeech.runAndWait()
    
    cityWeatherChosen = IdaEars()
    idaSpeech.say('looking up the weather in'+cityWeatherChosen)
    idaSpeech.runAndWait()
    idaSpeech.say('In' + cityWeatherChosen+ ' it is cloudy with a chance of Rain')
    idaSpeech.runAndWait()