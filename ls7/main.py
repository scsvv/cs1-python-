import speech_recognition as sr
import webbrowser

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Somthig say")

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ru-Ru")
            print(f"You said: {text}")

            if "открой сайт":
                webbrowser.open("https://google.com")

            if "папа римский":
                break

        except sr.UnknownValueError:
            print("Oops")
        except sr.RequestError as e:
            print("Request Err")
