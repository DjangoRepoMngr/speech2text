import speech_recognition as sr

# Load audio file
filename = r"C:\Users\APA\Desktop\speech-test\voice.mp3"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio = r.record(source)

# Transcribe audio
try:
    text = r.recognize_google(audio, language="fa-IR")
    print("Transcribed text: " + text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error; {0}".format(e))
