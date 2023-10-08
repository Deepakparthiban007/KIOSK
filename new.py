import pyttsx3 as p
import speech_recognition as sr

engine= p.init()
engine.say("hello i am your health assistant")
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer()

speak("how can i help you")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)


speak("how long do you have this problem")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

speak("what you ate last night")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

speak("are you experinecing any body pain")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)



