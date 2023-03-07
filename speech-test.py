import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as the audio source
with sr.Microphone() as source:
    print("Speak now:")
    audio = r.listen(source)

# recognize the speech using the Persian language
try:
    text = r.recognize_google(audio, language = "fa-IR")
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I did not understand what you said.")
except sr.RequestError as e:
    print(f"Error connecting to the Google Speech Recognition service: {e}")