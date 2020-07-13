import speech_recognition as sr
from Speaker import*


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = ""
        try:
            text = r.recognize_google(audio)
            print("You Said: ", text)
        except sr.UnknownValueError:
            voice_assist("Sorry, I did not get that")
    return text.lower()
