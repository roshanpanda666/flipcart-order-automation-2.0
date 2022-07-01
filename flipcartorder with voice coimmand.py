import pyautogui
import time
import pyttsx3
import speech_recognition as sr
import os
while True:
    r = sr.Recognizer()


    def speak(command):
                
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()


    with sr.Microphone() as source3:
        #speak("waiting for command")
        print("listening.......")
        audio2 = r.listen(source3)
        Text=r.recognize_google(audio2)
        print(Text)

        if "Flipkart" in Text:
            speak("order, in progress")

            time.sleep(1)
            print(pyautogui.position())
            pyautogui.moveTo(901,1056)
            pyautogui.click(button="left")
            pyautogui.moveTo(933,522)
            pyautogui.click(button="left")
            pyautogui.write("flipkart")
            pyautogui.press("enter")
            pyautogui.moveTo(244,398)
            time.sleep(2)
            pyautogui.click(button="left")
            pyautogui.moveTo(801,172)
            time.sleep(2)
            pyautogui.click(button="left")
            
            with sr.Microphone() as source3:
            #speak("waiting for command")
                speak("what do you want to order")
                audio2 = r.listen(source3)
                order=r.recognize_google(audio2)
                print(order)

            pyautogui.write(order)
            pyautogui.press("enter")
            pyautogui.moveTo(560,578)
            time.sleep(2)
            pyautogui.click(button="left")
            pyautogui.moveTo(600,873)
            time.sleep(2)
            pyautogui.click(button="left")
            time.sleep(2)
            pyautogui.moveTo(460,556)
            pyautogui.click(button="left")
            time.sleep(2)
            pyautogui.scroll(-5000)
            pyautogui.moveTo(1014,735)
            speak("say yes, to conform the order")
            speak("say no, to cancel the order")

            with sr.Microphone() as source3:
            
                print("listening.......")
                audio2 = r.listen(source3)
                conform=r.recognize_google(audio2)
                print(Text)
             
            if "no" in conform:
                speak("ok , canceling the order")

            if "yes" in conform:
                os.startfile("D:\\Pictures\\Chala_Ja_Bsdk_Clip_Chala_Ja_Bhos_(getmp3.pro).mp3")