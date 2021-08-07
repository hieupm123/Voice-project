from general_web import *

general = general_web()
output_check = general.lay_ten_nguoi_dung()

speech = speech_and_say();

def speech_catch_error():
    text_catch = 'Có gì đó không đúng bạn vui lòng xem lại yêu cầu của mình'
    speech.say_VN_by_Microsoft(text_catch)

class youtube(object):
    trinhduyet = None
    def mo_trinh_duyet(self):
        try:
            options = webdriver.ChromeOptions()
            PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
            PATH1 = PATH[:9] + output_check + PATH[9:]
            options.add_argument("user-data-dir=" + PATH1)
            self.trinhduyet = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
            self.trinhduyet.get("https://www.youtube.com")
            self.trinhduyet.maximize_window() 
            time.sleep(3)
        except:
            pass  

    def home(self):
        try:
            self.trinhduyet.get('https://www.youtube.com/')
            time.sleep(2)
        except:
                pass

    def chon_video(self,a=1):
        try:
            chon_video_o_trang_chu = self.trinhduyet.find_elements_by_id('content')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_video_o_trang_chu[a]).click(chon_video_o_trang_chu[a]).perform()
        except:
            pass

class video_kham_pha(youtube):
    def trending(self):
        try:
            self.trinhduyet.get('https://www.youtube.com/feed/trending')
        except:
            pass

    def music(self):
        try:
            self.trinhduyet.get('https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ')
        except:
            pass

    def gaming(self):
        try:
            self.trinhduyet.get('https://www.youtube.com/gaming')
        except:
            pass
        
    def sports(self):
        try:
            self.trinhduyet.get('https://www.youtube.com/channel/UCEgdi0XIXXZ-qJOFPf4JSKw')
        except:
            pass

class search_youtube(youtube):

    def find_video(self,nhap=''):
        try:
            nhan = self.trinhduyet.find_element_by_xpath('//*[@id="search"]')
            nhan.send_keys(nhap)
            nhan.send_keys(Keys.RETURN)
        except:
            pass

    def chon_video(self,a = 1):
        try:
            chon = self.trinhduyet.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon[a-1]).click(chon[a-1]).perform()
        except:
            pass


#Thao tac video 

class video(youtube):

    def phong_to_nho(self):
        try:
            pause_phong_to_nho = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_phong_to_nho).perform()
            sleep(1)
            phong_to_nho = self.trinhduyet.find_element_by_class_name('ytp-fullscreen-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phong_to_nho).click(phong_to_nho).perform()
        except:
            pass

    def bat_tat_che_do_rap_chieu_phim(self):
        try:
            pause_che_do_rap_chieu_phim = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_che_do_rap_chieu_phim).perform()
            sleep(1)
            che_do_rap_chieu_phim = self.trinhduyet.find_element_by_class_name('ytp-size-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(che_do_rap_chieu_phim).click(che_do_rap_chieu_phim).perform()
        except:
            pass

    def bat_tat_phu_de(self):
        try:
            pause_phu_de = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_phu_de).perform()
            sleep(1)
            phu_de = self.trinhduyet.find_element_by_class_name('ytp-subtitles-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_de).click(phu_de).perform()
        except:
            pass

    def bat_tat_tu_dong_phat(self):
        try:
            pause_tu_dong_phat = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_tu_dong_phat).perform()
            sleep(1)
            tu_dong_phat = self.trinhduyet.find_element_by_class_name('ytp-autonav-toggle-button-container')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tu_dong_phat).click(tu_dong_phat).perform()
        except:
            pass

    def tat_mo_tam_dung_video(self):
        try:
            pause_pause_video = self.trinhduyet.find_element_by_class_name('video-stream')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(pause_pause_video).click(pause_pause_video).perform()
        except:
            pass

    def next_video(self):
        try:
            pause_video_tiep_theo = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_video_tiep_theo).perform()
            sleep(1)
            video_tiep_theo = self.trinhduyet.find_element_by_class_name('ytp-next-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(video_tiep_theo).click(video_tiep_theo).perform()
        except:
            pass

    def bat_tat_loa_video(self):
        try:
            pause_am_luong = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_am_luong).perform()
            sleep(1)
            am_luong = self.trinhduyet.find_element_by_class_name('ytp-mute-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(am_luong).click(am_luong).perform()
        except:
            pass

    def bat_tat_cai_dat(self):
        try:
            pause_cai_dat = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_cai_dat).perform()
            time.sleep(1)
            cai_dat = self.trinhduyet.find_element_by_class_name('ytp-settings-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cai_dat).click(cai_dat).perform()
        except:
            pass

    def chat_luong_video(self,index = 3):
        try:
            self.bat_tat_cai_dat();
            # Sử lí giọng nói để lấy chất lượng video
            quality = ['144p','240p','360p','480p','720p','1080p','1440p']
            use = self.trinhduyet.find_element_by_xpath("//div[contains(text(),'Quality')]")
            self.trinhduyet.execute_script("arguments[0].click();",use)
            time.sleep(2)
            ans = quality[index]
            Xpath_quality = "//span[contains(string(),'" + ans + "')]"
            print(Xpath_quality)
            use = self.trinhduyet.find_element_by_xpath(Xpath_quality)
            self.trinhduyet.execute_script("arguments[0].click();",use)
            time.sleep(3)
        except:
            pass

class trinh_phat_thu_nho(youtube):
    def bat_trinh_phat_thu_nho(self):
        try:
            pause_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_trinh_phat_thu_nho).perform()
            sleep(1)
            bat_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(bat_trinh_phat_thu_nho).click(bat_trinh_phat_thu_nho).perform()
        except:
            pass

    def next_video(self):
        try:
            pause_video_tiep_theo_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_video_tiep_theo_trinh_phat_thu_nho).perform()
            sleep(1)
            video_tiep_theo_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-next-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(video_tiep_theo_trinh_phat_thu_nho).click(video_tiep_theo_trinh_phat_thu_nho).perform()
        except:
            pass

    def tat_mo_tam_dung_video(self):
        try:
            pause_dung_video_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_dung_video_trinh_phat_thu_nho).perform()
            sleep(1)
            dung_video_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-play-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(dung_video_trinh_phat_thu_nho).click(dung_video_trinh_phat_thu_nho).perform()
        except:
            pass

    def tat_trinh_phat_thu_nho(self):
        try:
            pause_tat_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_tat_trinh_phat_thu_nho).perform()
            sleep(1)
            tat_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-expand-watch-page-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tat_trinh_phat_thu_nho).click(tat_trinh_phat_thu_nho).perform()            
        except:
            pass