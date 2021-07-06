import speech_recognition
import pyttsx3
import os,sys,string
import webbrowser
def speech():
    sp = speech_recognition.Recognizer();
    with speech_recognition.Microphone() as mic:
        sp.adjust_for_ambient_noise(mic, duration=0.2)
        audio =sp.record(mic, duration=3)
    try:
        text = sp.recognize_google(audio);
    except:
        text = "xexe";
    return text;
def speech1():
    sp = speech_recognition.Recognizer();
    with speech_recognition.Microphone() as mic:
        # sp.adjust_for_ambient_noise(mic, duration=0.2)
        # audio =sp.record(mic, duration=3)
        audio = sp.listen(mic);
    try:
        text = sp.recognize_google(audio);
    except:
        text = "xexe";
    return text;
def say(text):
    e = pyttsx3.init();
    e.say(text)
    e.runAndWait()

def pause():
    while(1):
        text = speech1();
        print(text);
        if("On" in text or "on" in text):
            break;

def google():
    say("Your web you want")
    web = speech()
    while(web == "xexe"):
        say("Try again");
        web = speech()
    say("Google find" + web)
    url = "https://www.google.com/search?q=" + web;
    webbrowser.get().open(url);

def facebook():
    say("Welcome to facebook relax baby");
    url = "https://www.facebook.com/home.php"
    webbrowser.get().open(url);
    while(1):

def zalo():
    say("Zalo for boss");
    url = "https://chat.zalo.me/?null"
    webbrowser.get().open(url)

def youtube():
    say("Find in youtube");
    url = "https://www.youtube.com/"
    webbrowser.get().open(url)

def edit():
    say("Time code");
    os.system("start D:\\Project\\Subl")
    pause();

say("Welcome boss");
while(1):
    text = speech();
    if("Find" or "find" or "Google" in text):
        google();
    elif("Facebook" in text):
        facebook();
    elif("P" or "p" in text):
        say("Pause")
        pause();
    elif(("edit" or "Edit") in text):
        edit();
    elif(("Z" or "z") in text):
        zalo();
    elif(("Youtube" or "youtube") in text):
        youtube();
    else:
        say("See you soon");
        exit();