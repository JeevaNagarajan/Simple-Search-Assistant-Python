import speech_recognition as sr
import webbrowser

# create an instance of the recognizer class
r = sr.Recognizer()

# creating the instance of the Microphone class for using our microphone
mic = sr.Microphone()

with mic as source:

    print(" say something ")

    # adjust_for_ambient_noise() method of the Recognizer class is used to handle the ambient noise.
    r.adjust_for_ambient_noise(source)

    # listen() method captures input from the microphone
    # This method takes an audio source as its first argument and records input from the source until silence is detected.
    audio = r.listen(source)

    try:
        voice_data = r.recognize_google(audio)
        print(" you said : %s " %(voice_data))
        search_url = "https://www.google.com/search?q="+voice_data
        webbrowser.open_new_tab(search_url)

    except:
        print(" can't recognize your speech ")

