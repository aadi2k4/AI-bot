import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
# pip install speechrecognition 
# pip install pyaudio
# pip install setuptools
# pip install pocketsphinx


engine = pyttsx3.init()
newsapi = "a8d1fda43b19471893618f98fa5cc63d"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif "open facebook" in c.lower():
          webbrowser.open("https://facebook.com")
     elif "open linkedin" in c.lower():
          webbrowser.open("https://linkedin.com")
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
     elif c.lower().startswith("play"):
          song = c.lower().split(" ")[1]
          link = musiclibrary.music[song]
          webbrowser.open(link)
     elif "news" in c.lower():
        url = "https://newsapi.org/v2/top-headlines"
        api_key = "a8d1fda43b19471893618f98fa5cc63d"
        params = {
            'country': 'us',
            'apiKey': api_key
        }
        # https://newsapi.org/v2/top-headlines?country=us&apiKey=a8d1fda43b19471893618f98fa5cc63d
        # Sending the request
        r = requests.get(url, params=params)
        if r.status_code == 200:
            # Parse the response as JSON
            data = r.json()
            titles = [article['title'] for article in data.get('articles', [])]

            speak(titles)

     else:
        #Let OpenAI handle the request
        pass
        
if __name__ ==  "__main__":
    speak("Initializing Jarvis...")
    r = sr.Recognizer()
    while True:
        #Listen for the wake word Jarvis
        # Obtain audio from the microphone


            
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)  # Adjust for background noise

                    audio = r.listen(source,timeout=5)
                    print("recognizing..")
                word = r.recognize_google(audio)
                print(word)
                if(word.lower()=="jarvis"):
                    speak("Yes, I am Jarvis")
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        r.adjust_for_ambient_noise(source)  # Adjust for background noise

                        audio = r.listen(source,timeout=5)
                        command = r.recognize_google(audio)

                        processCommand(command)
            except Exception as e:
                print("Error; {0}".format(e))


 