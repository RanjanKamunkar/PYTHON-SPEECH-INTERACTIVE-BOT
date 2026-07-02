import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime


r = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# startup speech
speak("Hello sir, this is your Jarvis speaking.")

while True:
    try:
        # listening for wake word
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)

        # wake word 
        if "jarvis" in text.lower():
            speak("yes sir")

            # listenong commandas
            with sr.Microphone() as source:
                print("Jarvis active...")
                audio = r.listen(source)

            command = r.recognize_google(audio)
            print("Command:", command)

            if "how are you" in command.lower():
                speak("I am fine sir")

            elif "who is Harsh" in command.lower():
                speak("harsh is a first year student of computer engineering at  vidyavardhi's college of engineering and technology")
            elif "who is Suhas "in command.lower():
                speak("suhas is a first year student of computer engineering at  vidyavardhi's college of engineering and technology")
            elif "who is Akshat" in command.lower():
                speak("akshat is a first year student of computer engineering at  vidyavardhi's college of engineering and technology")
            elif "who is Ranjan" in command.lower():
                speak("ranjan is a first year student of computer engineering at  vidyavardhi's college of engineering and technology")
            elif "who is Mayur" in command.lower():
                speak("mayur is a first year student of computer engineering at  vidyavardhi's college of engineering and technology")


            elif "what is your name" in command.lower():
                speak("My name is Jarvis. I am a chatbot made by first year students of Vidyavardhinis college of engineering")

                

            elif "open youtube" in command.lower():
                speak("Opening youtube")
                webbrowser.open("https://youtube.com")

            elif "show me price of sensex" in command.lower():
                speak("showing details of sunsex")
                webbrowser.open("https://www.google.com/search?q=sensex&rlz=1C1VDKB_enIN1187IN1187&oq=sensex+&gs_lcrp=EgZjaHJvbWUqBwgAEAAYjwIyBwgAEAAYjwIyDQgBEAAYgwEYsQMYgAQyDQgCEAAYgwEYsQMYgAQyDQgDEAAYgwEYsQMYgAQyDQgEEAAYgwEYsQMYgAQyDQgFEAAYgwEYsQMYgAQyDQgGEAAYgwEYsQMYgAQyDQgHEAAYgwEYsQMYgAQyBwgIEAAYgAQyCggJEAAYsQMYgATSAQk5MjY0ajBqMTWoAgiwAgHxBXYOENSUrQrQ&sourceid=chrome&ie=UTF-8")

            elif "open google" in command.lower():
                speak("Opening google")
                webbrowser.open("https://google.com")

            elif "show me Nifty" in command.lower():
                speak("showing details of nifty")
                webbrowser.open("https://www.google.com/search?q=nifty&rlz=1C1VDKB_enIN1187IN1187&oq=nifty&gs_lcrp=EgZjaHJvbWUyFAgAEEUYORhDGIMBGLEDGIAEGIoFMhIIARAAGEMYgwEYsQMYgAQYigUyEggCEAAYQxiDARixAxiABBiKBTINCAMQABiDARixAxiABDIMCAQQABhDGIAEGIoFMhIIBRAAGEMYgwEYsQMYgAQYigUyDQgGEAAYgwEYsQMYgAQyDQgHEAAYgwEYsQMYgAQyCggIEAAYsQMYgAQyEAgJEAAYgwEYsQMYgAQYigXSAQk2NDM2ajBqMTWoAgywAgHxBUJMwmi-lzBz&sourceid=chrome&ie=UTF-8")

            elif " what time is it" in command.lower():
                time = datetime.datetime.now().strftime("%H:%M")
                speak("The time is " + time)    

            elif "play song" in command.lower():
                speak("playing song sir")
                webbrowser.open("https://www.youtube.com/watch?v=o0LydWpBQts&list=RDo0LydWpBQts&start_radio=1&pp=ygUNYmVsaWV2ZXIgc29uZ6AHAdIHCQnbCgGHKiGM7w%3D%3D")

            elif "exit" in command.lower():
                speak("Goodbye sir")
                break

    except sr.UnknownValueError:
        print(" I Could not understand audio, speak clearly")

    except Exception as e:
        print("Error:", e)