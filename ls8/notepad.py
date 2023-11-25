import speech_recognition as sr
import pyautogui
import time


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-EN")
        return text.lower()
    except sr.UnknownValueError:
        return " "


pyautogui.press('win')
time.sleep(1)

pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)

while True:
    text = recognize_speech()
    if 'end' in text:
        break
    pyautogui.write(text)


pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('example.txt')
pyautogui.press('enter')

pyautogui.hotkey('alt', 'f4')
