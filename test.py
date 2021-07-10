import speech_recognition
import pyttsx3
import schedule
import time,os,string
import playsound
from gtts import gTTS 

# while(1):
	# sp = speech_recognition.Recognizer();
	# text = ''
	# with speech_recognition.Microphone() as mic:
	#     sp.adjust_for_ambient_noise(mic, duration=0.2)
	#     audio =sp.record(mic, duration=3)
	# try:
	#     text = sp.recognize_google(audio,language="vi-VI");
	# except:
	#     text = '';
	#     print(text);

T = pyttsx3.init();
voices = T.getProperty('voices')
print(voices)
voice_VN_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
# T.setProperty('voice',voices[1].id)
T.setProperty('voice',voice_VN_id)
# e = gTTS(text,tld = 'com.vn',lang = 'vi')
# e.save('voice.mp3')
# playsound.playsound('voice.mp3')
# os.remove('voice.mp3')
T.say("Xin chào các bạn")
T.runAndWait()