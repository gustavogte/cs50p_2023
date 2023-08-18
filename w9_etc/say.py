# pip install pyttsx3
# pip install cowsay
# change: /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pyttsx3/drivers/nsss.py
# self = super(NSSpeechDriver, self).init()
# ==> self = objc.super(NSSpeechDriver, self).init()
# /Library/Frameworks/Python.framework/Versions//3.10/bin/cowsay (si esta la libreria, pero no en current)
# por eso no la marca aunque si la ejecuta
# /Library/Frameworks/Python.framework/Versions/Current/lib (aquí no esta)

import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
