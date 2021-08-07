import speech_recognition
import pyttsx3
import schedule
import time,os,string
import playsound
from gtts import gTTS 

# sau này chúng ta sẽ phát triển cái database riêng chứa các nội dung text
# phát triển chương trình sau random text đồng nghĩa phù hợp 

class speech_and_say:
    def init(self):
        name = ''
        language = 1
        self.say('My voice language defaut is English you can talk to me if you want to change this')
        self.say('What your name')
        name = self.speech_none_pause();
        if(name == ''):
            self.say('Your name relly difficult, i will break this babe')
        else:
            self.say('Ok i know your name' + name);

    def say_VN_by_Google(self,text):
        try:
            e = gTTS(text,tld = 'com.vn',lang = 'vi')
            e.save('voice.mp3')
            playsound.playsound('voice.mp3')
            os.remove('voice.mp3')
        except:
            pass
            
    def say_VN_by_Microsoft(self, text):
        e = pyttsx3.init()
        voice_VN_id = ""
        try:
            voice_VN_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
            e.setProperty('voice',voice_VN_id)
        except:
            self.say_VN_by_google(text)
            return
        e.say(text)
        e.runAndWait()
        
    def speech_none_pause(self):
        text = '';
        sp = speech_recognition.Recognizer();
        with speech_recognition.Microphone() as mic:
            sp.adjust_for_ambient_noise(mic, duration=0.2)
            audio = sp.record(mic, duration=3)
        try:
            text = sp.recognize_google(audio,language="vi-VI");
        except:
            pass;
        return text;

    def speech_with_pause(self):
        sp = speech_recognition.Recognizer();
        with speech_recognition.Microphone() as mic:
            audio = sp.listen(mic)
        try:
            text = sp.recognize_google(audio,language="vi-VI");
        except:
            text = ''
        return text

    def say(self,text):
        e = pyttsx3.init();
        e.say(text)
        e.runAndWait()

    def pause(self, defaut):
        ok = 0
        def change():
            self.ok = 1

        if(language == 0):
            speech_time_up = 'Đến thời gian nghỉ tay rồi'
            schedule.hour.do(self.say(speech_time_up + self.name) and change)
        else:
            speech_time_up = 'Time to relax I come back with you' 
            schedule.hour.do(self.say_VN_by_Microsoft(speech_time_up + self.name) and change)

        schedule.run_pending()
		
        while(self.ok != 0):
            text = self.speech_with_pause();
            if('On' or 'on' or 'bật' in text):
                self.say();
                break
            elif('Tắt' or 'off' or 'off' in text):
            	exit()
            time.sleep(1)
            
            



