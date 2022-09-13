import speech_recognition as sr

ear = sr.Recognizer()

def IdaEars():
    with sr.Microphone() as source:
        print("Listening...")
        audio = ear.listen(source)

        text = ear.recognize_google(audio)
        return(text)